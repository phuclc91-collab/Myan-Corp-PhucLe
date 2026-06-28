# THIẾT KẾ NỀN TẢNG KỸ THUẬT SUPABASE CRM - MYAN CORP

Dựa trên PRD và Design Brief, dưới đây là thiết kế kiến trúc Backend hoàn chỉnh cho CRM Myan Corp sử dụng Supabase.

---

## 1. Danh sách các bảng cần có (Tables)

Hệ thống được thiết kế tối giản nhưng bao quát toàn bộ yêu cầu, bao gồm các bảng sau:
1. `profiles`: Lưu trữ thông tin người dùng (nhân viên, trưởng nhóm, admin) và vai trò (Role).
2. `teams`: Lưu thông tin các phòng ban/đội nhóm kinh doanh.
3. `team_members`: Bảng trung gian ánh xạ nhân viên vào các nhóm (một người có thể thuộc nhóm, có người làm trưởng nhóm).
4. `pipeline_stages`: Định nghĩa các giai đoạn trong Kanban (Tiếp cận, Tư vấn, Báo giá, Thương thảo, Thành công).
5. `leads`: Kết hợp hồ sơ khách hàng và cơ hội bán hàng vào chung một bảng (theo cấu trúc yêu cầu) để quản lý trơn tru quy trình.
6. `lead_tags`: Các nhãn phân loại khách hàng (Khách lẻ, Đại lý, VIP).
7. `lead_tag_mapping`: Bảng trung gian gán nhiều nhãn cho một `lead`.
8. `lead_lists`: Lưu trữ các danh sách khách hàng được gom nhóm hoặc lọc sẵn.
9. `tasks`: Quản lý công việc và nhắc nhở liên quan đến từng `lead`.
10. `subscriptions`: Quản lý hợp đồng dịch vụ / đăng ký / thanh toán.
11. `activity_logs`: Bảng Audit ghi nhận mọi lịch sử thao tác của người dùng.

---

## 2 & 3. SQL Schema hoàn chỉnh và Quan hệ (Relationships)

```sql
-- Bật extension tạo UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ==========================================
-- 1. PROFILES & TEAMS
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
  is_leader boolean DEFAULT false, -- Đánh dấu nếu là Trưởng nhóm của team này
  created_at timestamptz DEFAULT now(),
  UNIQUE(team_id, user_id)
);

-- ==========================================
-- 2. PIPELINE & LEADS
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
  is_deleted boolean DEFAULT false, -- Xóa mềm (Soft delete)
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

-- ==========================================
-- 3. TAGS & LISTS
-- ==========================================
CREATE TABLE lead_tags (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  name text NOT NULL UNIQUE,
  color text, -- Mã màu HEX (vd: #10B981)
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
  criteria jsonb, -- Bộ lọc động lưu dưới dạng JSON
  created_by uuid REFERENCES profiles(id),
  created_at timestamptz DEFAULT now()
);

-- ==========================================
-- 4. TASKS, SUBSCRIPTIONS & LOGS
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
  entity_type text NOT NULL, -- vd: 'lead', 'task'
  entity_id uuid NOT NULL,
  details jsonb,
  created_at timestamptz DEFAULT now()
);
```

---

## 4. Các Indexes (Chỉ mục) tối ưu hóa truy vấn

Để đảm bảo hiệu năng truy vấn dưới 200ms theo như yêu cầu trong PRD:

```sql
-- Tìm kiếm khách hàng theo sđt hoặc email thường xuyên xảy ra
CREATE INDEX idx_leads_phone ON leads(phone);
CREATE INDEX idx_leads_email ON leads(email);

-- Index để tối ưu RLS và lọc dữ liệu trên màn hình làm việc
CREATE INDEX idx_leads_assigned_to ON leads(assigned_to);
CREATE INDEX idx_leads_stage_id ON leads(stage_id);
CREATE INDEX idx_leads_is_deleted ON leads(is_deleted);

-- Tối ưu hóa truy vấn công việc (Tasks)
CREATE INDEX idx_tasks_assigned_to ON tasks(assigned_to);
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_due_date ON tasks(due_date);

-- Tối ưu cho kiểm tra phân quyền nhóm
CREATE INDEX idx_team_members_user_id ON team_members(user_id);
CREATE INDEX idx_team_members_team_id ON team_members(team_id);
```

---

## 5. Trigger và Function tự động tạo Profile

Để đảm bảo "Mỗi người dùng chỉ có một hồ sơ chính trong bảng profiles", chúng ta sử dụng cơ chế Native Trigger của Postgres lắng nghe sự kiện từ bảng `auth.users` của Supabase.

```sql
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER SET search_path = public
AS $$
BEGIN
  -- Insert dữ liệu vào profiles. Nếu email bị trùng thì có thể handle gracefully
  INSERT INTO public.profiles (id, email, full_name, role)
  VALUES (
    NEW.id,
    NEW.email,
    -- Lấy full_name từ metadata (nếu sign in bằng Google OAuth), hoặc tách từ email
    COALESCE(NEW.raw_user_meta_data->>'full_name', split_part(NEW.email, '@', 1)),
    'sales' -- Mặc định tạo tài khoản đều là sales (cấp thấp nhất)
  );
  RETURN NEW;
END;
$$;

-- Kích hoạt trigger ngay khi auth.users có dòng mới
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE PROCEDURE public.handle_new_user();
```

---

## 6. Cách lưu Role & Security Definer

Vai trò (`role`) được lưu trữ trong cột `role` của bảng `profiles`.
Để đảm bảo các quy tắc truy cập ngang hàng (RLS) hoạt động trơn tru và không bị lỗi đệ quy vòng (Infinite Recursion) khi JOIN bảng phân quyền, ta sử dụng các **hàm Security Definer** để Postgres thực thi với quyền vượt quyền để tra cứu vai trò:

```sql
-- Hàm lấy vai trò hiện tại của User đang đăng nhập
CREATE OR REPLACE FUNCTION get_user_role() RETURNS text AS $$
  SELECT role FROM profiles WHERE id = auth.uid();
$$ LANGUAGE sql SECURITY DEFINER STABLE;

-- Hàm kiểm tra xem user_id mục tiêu có nằm trong cùng nhóm với user đang đăng nhập không
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
```

---

## 7. Row Level Security (RLS) Policies

Bảo mật Row Level Security để cô lập dữ liệu theo vai trò (Admin, Trưởng Nhóm, Sales).

```sql
-- ==========================================
-- BẢNG LEADS
-- ==========================================
ALTER TABLE leads ENABLE ROW LEVEL SECURITY;

-- 1. Admin thấy toàn bộ
CREATE POLICY "Admin full access" ON leads FOR ALL TO authenticated
USING (get_user_role() = 'admin');

-- 2. Manager chỉ thấy của nhân viên thuộc nhóm mình
CREATE POLICY "Manager team access" ON leads FOR ALL TO authenticated
USING (
  get_user_role() = 'manager' 
  AND is_accessible_by_manager(assigned_to)
);

-- 3. Sales chỉ thấy khách hàng được phân công cho mình
CREATE POLICY "Sales own access" ON leads FOR ALL TO authenticated
USING (
  get_user_role() = 'sales' 
  AND assigned_to = auth.uid()
);

-- (Các bảng `tasks`, `subscriptions` áp dụng y hệt policy của bảng `leads`)
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Admin tasks access" ON tasks FOR ALL TO authenticated USING (get_user_role() = 'admin');
CREATE POLICY "Manager tasks access" ON tasks FOR ALL TO authenticated USING (get_user_role() = 'manager' AND is_accessible_by_manager(assigned_to));
CREATE POLICY "Sales tasks access" ON tasks FOR ALL TO authenticated USING (get_user_role() = 'sales' AND assigned_to = auth.uid());
```

---

## 8. Seed Data Mẫu (Cho Myan Corp)

Sử dụng tập dữ liệu trong Design Brief để nạp mẫu:

```sql
-- 1. Seed Stages (Bảng Kanban)
INSERT INTO pipeline_stages (id, name, probability, "order") VALUES
('11111111-1111-1111-1111-111111111111', 'Tiếp cận', 10, 1),
('22222222-2222-2222-2222-222222222222', 'Tư vấn', 30, 2),
('33333333-3333-3333-3333-333333333333', 'Báo giá', 50, 3),
('44444444-4444-4444-4444-444444444444', 'Thương thảo', 80, 4),
('55555555-5555-5555-5555-555555555555', 'Thành công', 100, 5);

-- 2. Seed Lead Tags
INSERT INTO lead_tags (id, name, color) VALUES
('aaaa1111-aaaa-1111-aaaa-111111111111', 'VIP', '#10B981'),
('bbbb2222-bbbb-2222-bbbb-222222222222', 'Đại lý', '#F59E0B'),
('cccc3333-cccc-3333-cccc-333333333333', 'Khách lẻ', '#3B82F6');

-- 3. Seed Teams
INSERT INTO teams (id, name) VALUES 
('team1111-team-1111-team-111111111111', 'Phòng Bán Hàng Doanh Nghiệp (B2B)'),
('team2222-team-2222-team-222222222222', 'Phòng Bán Hàng Cá Nhân (B2C)');
```

*(Lưu ý: Bạn cần có `profiles` ID hợp lệ từ `auth.users` để có thể Insert vào bảng `leads` do vướng khóa ngoại `assigned_to`).*

---

## 9. Mô tả Flow Xác Thực và Định Danh

- **Đăng ký / Đăng nhập Email + Mật khẩu:** Client gửi email/password lên Supabase. Supabase tạo tài khoản trong `auth.users`. Sau đó, trigger `handle_new_user()` tự động sinh ra một hồ sơ (profile) duy nhất bên public schema.
- **Đăng nhập bằng Social (Google OAuth):** 
  - Nếu email của tài khoản Google **đã tồn tại** trong hệ thống, cấu hình Supabase tính năng **"Link identity automatically"** sẽ tự động gắn kết (link) Provider Identity này vào `auth.users.id` gốc (của phương thức Email/Mật khẩu trước đó). 
  - Do `auth.users.id` không thay đổi, **hệ thống không tạo trùng Profile**. Vai trò (Role) và mọi dữ liệu cũ vẫn bám chặt theo người dùng này.
- **Reset Password:** Người dùng nhập Email, Supabase gửi link hoặc OTP. Sau khi xác nhận, người dùng đổi mật khẩu trực tiếp qua hàm API mà không chạm vào bảng `profiles` (do mật khẩu được hash an toàn ở schema `auth`).

---

## 10. Mô tả cơ chế phân quyền (Authorization Logic)

Bảo mật được thiết lập ở tầng Database (RLS). Khi có một Request từ Frontend (gọi bằng Supabase Client/Token):

1. **Token Identification:** Access Token chứa `sub` (tức là `auth.uid()`).
2. **Postgres Tra Cứu (Get User Role):** Hệ thống gọi hàm `get_user_role()` (đã định nghĩa ở trên) để đọc cột `role` từ bảng `profiles`.
3. **Thực thi Policy:**
   - **Nếu là `admin`**: Điều kiện `get_user_role() = 'admin'` thỏa mãn `TRUE`. Admin xem được toàn bộ.
   - **Nếu là `manager`**: Hàm `is_accessible_by_manager(assigned_to)` được gọi. Nó đếm xem chủ nhân của record (`assigned_to`) có tham gia chung bất kỳ Team nào với `auth.uid()` hay không. Nếu có, dữ liệu được hiển thị (Trưởng nhóm chỉ thấy khách của nhóm mình).
   - **Nếu là `sales`**: Policy ép chặt `assigned_to = auth.uid()`. Không cần JOIN. Cực kỳ nhanh. Sale chỉ thấy dữ liệu họ đứng tên.

Bằng cách chặn RLS ngay tại tầng DB, kể cả khi Hacker có lấy được API URL để tự gọi bằng Postman, họ cũng chỉ lấy được lượng dữ liệu giống hệt trên UI của họ, không bao giờ lấy được của công ty.
