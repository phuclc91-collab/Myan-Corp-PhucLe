import os
from bs4 import BeautifulSoup

file_path = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype/crm-frontend/settings.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# 1. Add ID to Table Body
tbody = soup.find("tbody")
if tbody:
    tbody['id'] = 'user-table-body'
    tbody.clear()

# 2. Add ID to Add User button
add_btn = soup.find(lambda tag: tag.name == "button" and "Thêm nhân sự" in tag.text)
if add_btn:
    add_btn['id'] = 'btn-add-user'

# 3. Inject Modal HTML
modal_html = """
<!-- Create User Modal (Mockup) -->
<div class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm transition-opacity" id="user-modal">
    <div class="bg-surface-container-lowest rounded-xl shadow-lg w-full max-w-md p-lg transform transition-all">
        <div class="flex justify-between items-center mb-md border-b border-outline-variant pb-sm">
            <h3 class="text-headline-sm font-bold text-on-surface">Thêm nhân sự mới</h3>
            <button class="text-outline hover:text-on-surface" id="btn-close-user-modal" type="button">
                <span class="material-symbols-outlined">close</span>
            </button>
        </div>
        <form class="space-y-md" id="form-add-user">
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Họ và tên *</label>
                <input class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" placeholder="VD: Nguyễn Văn A" required="" type="text"/>
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Email *</label>
                <input class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" placeholder="VD: a.nguyen@myancorp.vn" required="" type="email"/>
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Vai trò *</label>
                <select class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20">
                    <option value="sales" selected>Sales</option>
                    <option value="manager">Manager</option>
                    <option value="admin">Admin</option>
                </select>
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Mật khẩu khởi tạo *</label>
                <input class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" required="" type="password" placeholder="******"/>
                <p class="text-[11px] text-outline mt-1">* Tính năng Tạo tài khoản qua Admin Dashboard đang ở chế độ Prototype. Nhân sự có thể tự tạo tài khoản qua luồng Đăng ký để bảo mật mật khẩu.</p>
            </div>
            <div class="pt-md flex justify-end gap-sm">
                <button class="px-md py-2 border border-outline-variant rounded-lg text-on-surface hover:bg-surface-variant font-medium" id="btn-cancel-user-modal" type="button">Hủy</button>
                <button class="px-md py-2 bg-primary text-white rounded-lg hover:opacity-90 font-medium" type="submit">Lưu thông tin</button>
            </div>
        </form>
    </div>
</div>
"""
main_tag = soup.find('main')
if main_tag:
    main_tag.append(BeautifulSoup(modal_html, 'html.parser'))

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

# 4. Replace Script block via string manipulation
with open(file_path, "r", encoding="utf-8") as f:
    raw_html = f.read()

start_idx = raw_html.find("<script>\n        document.querySelectorAll('tr').forEach(row => {")
end_idx = raw_html.find("</script></body></html>")

if start_idx != -1 and end_idx != -1:
    new_script = """<script>
document.addEventListener('DOMContentLoaded', async () => {
    const { data: { session } } = await supabase.auth.getSession();
    if (!session) {
        window.location.href = 'index.html';
        return;
    }
    
    // Hook up logout
    const logoutLinks = document.querySelectorAll('a, button');
    logoutLinks.forEach(link => {
        if (link.innerText && link.innerText.includes('Đăng xuất')) {
            link.addEventListener('click', async (e) => {
                e.preventDefault();
                await supabase.auth.signOut();
                window.location.href = 'index.html';
            });
            if (link.tagName === 'BUTTON') link.removeAttribute('onclick');
            if (link.tagName === 'A') link.setAttribute('href', '#');
        }
    });

    const tbody = document.getElementById('user-table-body');

    window.updateRole = async (userId, newRole) => {
        try {
            const { error } = await supabase.from('profiles').update({ role: newRole }).eq('id', userId);
            if(error) throw error;
        } catch(err) {
            alert('Lỗi cập nhật vai trò: ' + err.message);
        }
    };

    window.toggleStatus = async (userId, el) => {
        const newStatus = el.checked ? 'active' : 'inactive';
        try {
            const { error } = await supabase.from('profiles').update({ status: newStatus }).eq('id', userId);
            if(error) throw error;
        } catch(err) {
            alert('Lỗi cập nhật trạng thái: ' + err.message);
            el.checked = !el.checked; // Revert visually
        }
    };

    const loadUsers = async () => {
        try {
            if (tbody) tbody.innerHTML = '<tr><td colspan="6" class="text-center py-10 text-outline">Đang tải dữ liệu...</td></tr>';
            
            const { data, error } = await supabase.from('profiles').select('*').order('created_at', { ascending: false });
            if (error) throw error;

            if (!data || data.length === 0) {
                if (tbody) tbody.innerHTML = '<tr><td colspan="6" class="text-center py-10 text-outline">Không có tài khoản nào.</td></tr>';
                return;
            }

            if (tbody) {
                tbody.innerHTML = data.map(user => {
                    const isChecked = user.status === 'active' ? 'checked' : '';
                    
                    // Handle default avatars based on role or name
                    const initial = user.full_name ? user.full_name.charAt(0).toUpperCase() : 'U';
                    const avatarColors = {
                        'admin': 'bg-error-container text-error',
                        'manager': 'bg-primary-container text-primary',
                        'sales': 'bg-tertiary-container text-tertiary'
                    };
                    const colorCls = avatarColors[user.role] || 'bg-secondary-container text-secondary';
                    
                    const avatarHtml = `<div class="w-10 h-10 rounded-full flex items-center justify-center font-bold border border-outline-variant ${colorCls}">${initial}</div>`;

                    return `
                    <tr class="hover:bg-surface-container-lowest transition-colors">
                        <td class="px-lg py-4">
                            <div class="flex items-center gap-3">
                                ${avatarHtml}
                                <div>
                                    <p class="font-body-md font-semibold text-on-background">${user.full_name}</p>
                                    <p class="text-[11px] text-outline">ID: ${user.id.substring(0,8)}</p>
                                </div>
                            </div>
                        </td>
                        <td class="px-lg py-4 font-body-sm text-on-surface-variant">${user.email}</td>
                        <td class="px-lg py-4">
                            <select onchange="updateRole('${user.id}', this.value)" class="bg-surface-container-low border-none rounded-lg text-body-sm py-1.5 px-3 focus:ring-1 focus:ring-primary w-32 cursor-pointer">
                                <option value="admin" ${user.role === 'admin' ? 'selected' : ''}>Admin</option>
                                <option value="manager" ${user.role === 'manager' ? 'selected' : ''}>Manager</option>
                                <option value="sales" ${user.role === 'sales' ? 'selected' : ''}>Sales</option>
                            </select>
                        </td>
                        <td class="px-lg py-4">
                            <span class="text-body-sm text-on-surface-variant">Myan Corp</span>
                        </td>
                        <td class="px-lg py-4 text-center">
                            <label class="switch">
                                <input type="checkbox" onchange="toggleStatus('${user.id}', this)" ${isChecked}>
                                <span class="slider"></span>
                            </label>
                        </td>
                        <td class="px-lg py-4 text-right">
                            <button class="text-outline hover:text-primary transition-colors">
                                <span class="material-symbols-outlined">more_vert</span>
                            </button>
                        </td>
                    </tr>
                    `;
                }).join('');
            }
        } catch(err) {
            console.error('Load users error:', err);
            if (tbody) tbody.innerHTML = '<tr><td colspan="6" class="text-center py-10 text-error">Lỗi tải dữ liệu.</td></tr>';
        }
    };

    // Modal Logic
    const btnAdd = document.getElementById('btn-add-user');
    const modal = document.getElementById('user-modal');
    const btnClose = document.getElementById('btn-close-user-modal');
    const btnCancel = document.getElementById('btn-cancel-user-modal');
    const formAdd = document.getElementById('form-add-user');

    if(btnAdd && modal) btnAdd.addEventListener('click', () => modal.classList.remove('hidden'));
    
    const closeModal = () => {
        if(modal) modal.classList.add('hidden');
        if(formAdd) formAdd.reset();
    };

    if(btnClose) btnClose.addEventListener('click', closeModal);
    if(btnCancel) btnCancel.addEventListener('click', closeModal);
    
    if(formAdd) {
        formAdd.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Bản prototype: Tính năng thêm nhân sự trực tiếp qua Admin Panel đang được giả lập. Vui lòng sử dụng tính năng "Đăng ký" tại trang Login để nhân sự tự tạo tài khoản.');
            closeModal();
        });
    }

    loadUsers();
});
"""
    raw_html = raw_html[:start_idx] + new_script + raw_html[end_idx:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(raw_html)

print("Settings module updated successfully.")
