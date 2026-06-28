import os
import glob
from bs4 import BeautifulSoup
import re

base_path = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype/crm-frontend"
html_files = glob.glob(os.path.join(base_path, "*.html"))
exclude_files = ["index.html", "reset-password.html"]

# 1. Add Register Modal to index.html
index_path = os.path.join(base_path, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    soup_idx = BeautifulSoup(f, "html.parser")

register_link = soup_idx.find(lambda tag: tag.name == "a" and "Đăng ký ngay" in tag.text)
if register_link:
    register_link['id'] = 'btn-open-register'

register_modal = """
<!-- Register Modal -->
<div id="register-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm transition-opacity">
    <div class="bg-surface-container-lowest rounded-xl shadow-lg w-full max-w-md p-lg transform transition-all">
        <div class="flex justify-between items-center mb-md border-b border-outline-variant pb-sm">
            <h3 class="text-headline-sm font-bold text-on-surface">Đăng ký tài khoản</h3>
            <button type="button" id="btn-close-register" class="text-outline hover:text-on-surface">
                <span class="material-symbols-outlined">close</span>
            </button>
        </div>
        <form id="form-register" class="space-y-md">
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Họ và tên *</label>
                <input type="text" id="reg-name" required class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" placeholder="Nguyễn Văn A">
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Email *</label>
                <input type="email" id="reg-email" required class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" placeholder="email@myancorp.com">
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Mật khẩu *</label>
                <input type="password" id="reg-password" required class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" placeholder="Tối thiểu 6 ký tự">
            </div>
            <div class="pt-md flex justify-end gap-sm">
                <button type="button" id="btn-cancel-register" class="px-md py-2 border border-outline-variant rounded-lg text-on-surface hover:bg-surface-variant font-medium">Hủy</button>
                <button type="submit" id="btn-submit-register" class="px-md py-2 bg-primary text-white rounded-lg hover:opacity-90 font-medium">Đăng ký</button>
            </div>
        </form>
    </div>
</div>
"""
if not soup_idx.find(id="register-modal"):
    soup_idx.body.append(BeautifulSoup(register_modal, "html.parser"))

with open(index_path, "w", encoding="utf-8") as f:
    f.write(str(soup_idx))

# Add register logic to index.html manually via string replace to not mess up script
with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

reg_logic = """
            // 5. Đăng ký tài khoản
            const btnOpenReg = document.getElementById('btn-open-register');
            const regModal = document.getElementById('register-modal');
            const btnCloseReg = document.getElementById('btn-close-register');
            const btnCancelReg = document.getElementById('btn-cancel-register');
            const formReg = document.getElementById('form-register');
            
            if(btnOpenReg && regModal) {
                const closeReg = () => { regModal.classList.add('hidden'); formReg.reset(); };
                btnOpenReg.addEventListener('click', (e) => { e.preventDefault(); regModal.classList.remove('hidden'); });
                btnCloseReg.addEventListener('click', closeReg);
                btnCancelReg.addEventListener('click', closeReg);
                
                formReg.addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const name = document.getElementById('reg-name').value;
                    const email = document.getElementById('reg-email').value;
                    const pwd = document.getElementById('reg-password').value;
                    
                    const btnSubmit = document.getElementById('btn-submit-register');
                    const origText = btnSubmit.innerText;
                    btnSubmit.innerText = 'Đang xử lý...';
                    btnSubmit.disabled = true;
                    
                    const { data, error } = await supabase.auth.signUp({
                        email: email,
                        password: pwd,
                        options: {
                            data: { full_name: name }
                        }
                    });
                    
                    if (error) {
                        alert('Lỗi đăng ký: ' + error.message);
                    } else {
                        alert('Đăng ký thành công! Bạn có thể đăng nhập ngay.');
                        closeReg();
                    }
                    btnSubmit.innerText = origText;
                    btnSubmit.disabled = false;
                });
            }
"""
if "btn-open-register" not in idx_content and "regModal" not in idx_content:
    idx_content = idx_content.replace("});\n        </script></body></html>", reg_logic + "\n        });\n        </script></body></html>")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)

# 2. Update Header in all internal HTMLs
for html_file in html_files:
    filename = os.path.basename(html_file)
    if filename in exclude_files:
        continue
    
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # Find profile text container (e.g. text-right)
    text_right = soup.find("div", class_=lambda c: c and "text-right" in c)
    if text_right:
        p_tags = text_right.find_all("p")
        if len(p_tags) >= 2:
            p_tags[0]['id'] = "header-user-name"
            p_tags[1]['id'] = "header-user-role"
    
    # Find avatar img and add id
    # avatar usually next to text_right, inside 'group' div
    group_div = soup.find("div", class_=lambda c: c and "cursor-pointer group" in c)
    if group_div:
        img = group_div.find("img")
        if img:
            img['id'] = "header-user-avatar"
            
        # Append logout button next to avatar
        if not group_div.find(id="btn-logout"):
            logout_html = """<button id="btn-logout" title="Đăng xuất" class="ml-2 w-8 h-8 rounded-full bg-error/10 text-error flex items-center justify-center hover:bg-error/20 transition-colors"><span class="material-symbols-outlined text-[18px]">logout</span></button>"""
            group_div.append(BeautifulSoup(logout_html, "html.parser"))
            
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(str(soup))

# 3. Add global logic to supabase-config.js
config_path = os.path.join(base_path, "supabase-config.js")
with open(config_path, "r", encoding="utf-8") as f:
    config_content = f.read()

global_logic = """

// Global Auth Guard & Profile Fetcher
document.addEventListener('DOMContentLoaded', async () => {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const isPublicPage = currentPage === 'index.html' || currentPage === 'reset-password.html';

    const { data: { session }, error: sessionError } = await supabase.auth.getSession();
    
    // Auth Guard
    if (!isPublicPage && !session) {
        window.location.href = 'index.html';
        return;
    }

    if (session) {
        // Render Profile
        const nameEl = document.getElementById('header-user-name');
        const roleEl = document.getElementById('header-user-role');
        const avatarEl = document.getElementById('header-user-avatar');
        
        if (nameEl || roleEl) {
            const { data: profile } = await supabase.from('profiles').select('full_name, role').eq('id', session.user.id).single();
            if (profile) {
                if (nameEl) nameEl.innerText = profile.full_name || 'Người dùng';
                if (roleEl) {
                    const roleMap = { 'admin': 'Quản trị viên', 'manager': 'Trưởng nhóm', 'sales': 'NV Kinh doanh' };
                    roleEl.innerText = roleMap[profile.role] || profile.role;
                }
                if (avatarEl) {
                    // Create Initials
                    const name = profile.full_name || 'U';
                    const parts = name.trim().split(' ');
                    const initials = parts.length >= 2 ? (parts[0][0] + parts[parts.length-1][0]).toUpperCase() : name.substring(0,2).toUpperCase();
                    
                    // Replace img with div
                    const newAvatar = document.createElement('div');
                    newAvatar.className = 'w-10 h-10 rounded-full bg-primary flex items-center justify-center text-white font-bold text-label-md border-2 border-primary-fixed';
                    newAvatar.innerText = initials;
                    avatarEl.parentNode.replaceChild(newAvatar, avatarEl);
                }
            }
        }
        
        // Logout Event
        const btnLogout = document.getElementById('btn-logout');
        if (btnLogout) {
            btnLogout.addEventListener('click', async () => {
                await supabase.auth.signOut();
                window.location.href = 'index.html';
            });
        }
    }
});
"""
if "Global Auth Guard" not in config_content:
    with open(config_path, "a", encoding="utf-8") as f:
        f.write(global_logic)

print("Applied Auth Guard, Logout, Registration, and Profile rendering successfully.")
