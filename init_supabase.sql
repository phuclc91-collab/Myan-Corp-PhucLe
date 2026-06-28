-- ==========================================
-- BẬT CÁC EXTENSION CẦN THIẾT
-- ==========================================
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ==========================================
-- 1. TẠO BẢNG: PROFILES & TEAMS
-- ==========================================
CREATE TABLE profiles (
  id uuid PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email text UNIQUE NOT NULL,
  full_name text NOT NULL,
  role text NOT NULL CHECK (role IN ('admin', 'manager', 'sales')) DEFAULT 'sales',
  status text NOT NULL CHECK (status IN ('active', 'inactive')) DEFAULT 'active',
  created_at timestamptz DEFAULT now()
);

CREATE TABLE teams (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  name text NOT NULL,
  description text,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE team_members (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  team_id uuid REFERENCES teams(id) ON DELETE CASCADE,
  user_id uuid REFERENCES profiles(id) ON DELETE CASCADE,
  is_leader boolean DEFAULT false,
  created_at timestamptz DEFAULT now(),
  UNIQUE(team_id, user_id)
);

-- ==========================================
-- 2. TẠO BẢNG: PIPELINE & LEADS
-- ==========================================
CREATE TABLE pipeline_stages (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  name text NOT NULL,
  probability integer NOT NULL CHECK (probability >= 0 AND probability <= 100),
  "order" integer NOT NULL,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE leads (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  name text NOT NULL,
  company_name text,
  phone text UNIQUE NOT NULL,
  email text,
  expected_value numeric(15,2) DEFAULT 0,
  actual_value numeric(15,2),
  stage_id uuid REFERENCES pipeline_stages(id),
  assigned_to uuid REFERENCES profiles(id),
  created_by uuid REFERENCES profiles(id),
  notes text,
  is_deleted boolean DEFAULT false,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

-- ==========================================
-- 3. TẠO BẢNG: TAGS & LISTS
-- ==========================================
CREATE TABLE lead_tags (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  name text NOT NULL UNIQUE,
  color text,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE lead_tag_mapping (
  lead_id uuid REFERENCES leads(id) ON DELETE CASCADE,
  tag_id uuid REFERENCES lead_tags(id) ON DELETE CASCADE,
  PRIMARY KEY (lead_id, tag_id)
);

CREATE TABLE lead_lists (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  name text NOT NULL,
  description text,
  criteria jsonb,
  created_by uuid REFERENCES profiles(id),
  created_at timestamptz DEFAULT now()
);

-- ==========================================
-- 4. TẠO BẢNG: TASKS, SUBSCRIPTIONS & LOGS
-- ==========================================
CREATE TABLE tasks (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  lead_id uuid REFERENCES leads(id) ON DELETE CASCADE,
  title text NOT NULL,
  description text,
  due_date timestamptz NOT NULL,
  priority text NOT NULL CHECK (priority IN ('cao', 'trung_binh', 'thap')) DEFAULT 'trung_binh',
  status text NOT NULL CHECK (status IN ('chua_lam', 'dang_lam', 'da_xong', 'qua_han')) DEFAULT 'chua_lam',
  assigned_to uuid REFERENCES profiles(id),
  created_by uuid REFERENCES profiles(id),
  created_at timestamptz DEFAULT now()
);

CREATE TABLE subscriptions (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  lead_id uuid REFERENCES leads(id) ON DELETE CASCADE,
  plan_name text NOT NULL,
  amount numeric(15,2) NOT NULL,
  start_date date NOT NULL,
  end_date date,
  status text NOT NULL CHECK (status IN ('active', 'past_due', 'canceled', 'completed')) DEFAULT 'active',
  created_at timestamptz DEFAULT now()
);

CREATE TABLE activity_logs (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id uuid REFERENCES profiles(id),
  action text NOT NULL,
  entity_type text NOT NULL,
  entity_id uuid NOT NULL,
  details jsonb,
  created_at timestamptz DEFAULT now()
);

-- ==========================================
-- 5. TẠO CHỈ MỤC (INDEXES)
-- ==========================================
CREATE INDEX idx_leads_phone ON leads(phone);
CREATE INDEX idx_leads_email ON leads(email);
CREATE INDEX idx_leads_assigned_to ON leads(assigned_to);
CREATE INDEX idx_leads_stage_id ON leads(stage_id);
CREATE INDEX idx_leads_is_deleted ON leads(is_deleted);
CREATE INDEX idx_tasks_assigned_to ON tasks(assigned_to);
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_due_date ON tasks(due_date);
CREATE INDEX idx_team_members_user_id ON team_members(user_id);
CREATE INDEX idx_team_members_team_id ON team_members(team_id);

-- ==========================================
-- 6. TẠO TRIGGER TỰ ĐỘNG TẠO PROFILE KHI CÓ USER MỚI
-- ==========================================
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER SET search_path = public
AS $$
BEGIN
  INSERT INTO public.profiles (id, email, full_name, role)
  VALUES (
    NEW.id,
    NEW.email,
    COALESCE(NEW.raw_user_meta_data->>'full_name', split_part(NEW.email, '@', 1)),
    'sales'
  );
  RETURN NEW;
END;
$$;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE PROCEDURE public.handle_new_user();

-- ==========================================
-- 7. TẠO CÁC HÀM SECURITY DEFINER ĐỂ PHÂN QUYỀN
-- ==========================================
CREATE OR REPLACE FUNCTION get_user_role() RETURNS text AS $$
  SELECT role FROM profiles WHERE id = auth.uid();
$$ LANGUAGE sql SECURITY DEFINER STABLE;

CREATE OR REPLACE FUNCTION is_accessible_by_manager(target_user_id uuid) RETURNS boolean AS $$
BEGIN
  RETURN EXISTS (
    SELECT 1 FROM team_members 
    WHERE user_id = target_user_id 
    AND team_id IN (
      SELECT team_id FROM team_members WHERE user_id = auth.uid()
    )
  );
END;
$$ LANGUAGE plpgsql SECURITY DEFINER STABLE;

-- ==========================================
-- 8. THIẾT LẬP ROW LEVEL SECURITY (RLS) POLICIES
-- ==========================================
ALTER TABLE leads ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Admin full access" ON leads FOR ALL TO authenticated USING (get_user_role() = 'admin');
CREATE POLICY "Manager team access" ON leads FOR ALL TO authenticated USING (get_user_role() = 'manager' AND is_accessible_by_manager(assigned_to));
CREATE POLICY "Sales own access" ON leads FOR ALL TO authenticated USING (get_user_role() = 'sales' AND assigned_to = auth.uid());

ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Admin tasks access" ON tasks FOR ALL TO authenticated USING (get_user_role() = 'admin');
CREATE POLICY "Manager tasks access" ON tasks FOR ALL TO authenticated USING (get_user_role() = 'manager' AND is_accessible_by_manager(assigned_to));
CREATE POLICY "Sales tasks access" ON tasks FOR ALL TO authenticated USING (get_user_role() = 'sales' AND assigned_to = auth.uid());

ALTER TABLE subscriptions ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Admin sub access" ON subscriptions FOR ALL TO authenticated USING (get_user_role() = 'admin');

-- ==========================================
-- 9. DỮ LIỆU MẪU (SEED DATA)
-- ==========================================
INSERT INTO pipeline_stages (id, name, probability, "order") VALUES
('11111111-1111-1111-1111-111111111111', 'Tiếp cận', 10, 1),
('22222222-2222-2222-2222-222222222222', 'Tư vấn', 30, 2),
('33333333-3333-3333-3333-333333333333', 'Báo giá', 50, 3),
('44444444-4444-4444-4444-444444444444', 'Thương thảo', 80, 4),
('55555555-5555-5555-5555-555555555555', 'Thành công', 100, 5);

INSERT INTO lead_tags (id, name, color) VALUES
('66666666-6666-6666-6666-666666666666', 'VIP', '#10B981'),
('77777777-7777-7777-7777-777777777777', 'Đại lý', '#F59E0B'),
('88888888-8888-8888-8888-888888888888', 'Khách lẻ', '#3B82F6');

INSERT INTO teams (id, name) VALUES 
('99999999-9999-9999-9999-999999999999', 'Phòng Bán Hàng Doanh Nghiệp (B2B)'),
('12345678-1234-1234-1234-123456789012', 'Phòng Bán Hàng Cá Nhân (B2C)');
