import os
from bs4 import BeautifulSoup
import re

base_path = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype/crm-frontend"
index_path = os.path.join(base_path, "index.html")
reset_path = os.path.join(base_path, "reset-password.html")

# --- Modifying index.html ---
with open(index_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find 'Quên mật khẩu?' link
forgot_link = soup.find(lambda tag: tag.name == "a" and "Quên mật khẩu" in tag.text)
if forgot_link:
    forgot_link['id'] = 'btn-forgot-pwd'

# Modal HTML
modal_html = """
<!-- Forgot Password Modal -->
<div id="forgot-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm transition-opacity">
    <div class="bg-surface-container-lowest rounded-xl shadow-lg w-full max-w-md p-lg transform transition-all">
        <div class="flex justify-between items-center mb-md border-b border-outline-variant pb-sm">
            <h3 class="text-headline-sm font-bold text-on-surface">Quên mật khẩu</h3>
            <button type="button" id="btn-close-forgot-modal" class="text-outline hover:text-on-surface">
                <span class="material-symbols-outlined">close</span>
            </button>
        </div>
        <p class="text-body-sm text-on-surface-variant mb-4">Vui lòng nhập email đã đăng ký của bạn. Chúng tôi sẽ gửi một liên kết để bạn đặt lại mật khẩu.</p>
        <form id="form-forgot-pwd" class="space-y-md">
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs" for="forgot-email">Email</label>
                <input type="email" id="forgot-email" required class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" placeholder="Nhập email của bạn">
            </div>
            <div class="pt-md flex justify-end gap-sm">
                <button type="button" id="btn-cancel-forgot-modal" class="px-md py-2 border border-outline-variant rounded-lg text-on-surface hover:bg-surface-variant font-medium">Hủy</button>
                <button type="submit" id="btn-submit-forgot-modal" class="px-md py-2 bg-primary text-white rounded-lg hover:opacity-90 font-medium">Gửi liên kết</button>
            </div>
        </form>
    </div>
</div>
"""
modal_soup = BeautifulSoup(modal_html, 'html.parser')

# Check if forgot modal already exists
if not soup.find(id="forgot-modal"):
    # Append right before the last script tag if possible, or append to body
    soup.body.append(modal_soup)

# We need to update the JS in the last script tag. We will use Regex on the raw HTML for precision rather than BS4 which can mangle scripts.
with open(index_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add logic to JS
js_logic = """
            // 4. Lắng nghe sự kiện Quên mật khẩu
            const btnForgot = document.getElementById('btn-forgot-pwd');
            const forgotModal = document.getElementById('forgot-modal');
            const btnCloseForgot = document.getElementById('btn-close-forgot-modal');
            const btnCancelForgot = document.getElementById('btn-cancel-forgot-modal');
            const formForgot = document.getElementById('form-forgot-pwd');
            
            if(btnForgot && forgotModal) {
                const closeForgotModal = () => {
                    forgotModal.classList.add('hidden');
                    if(formForgot) formForgot.reset();
                };
                
                btnForgot.addEventListener('click', (e) => {
                    e.preventDefault();
                    forgotModal.classList.remove('hidden');
                });
                
                btnCloseForgot.addEventListener('click', closeForgotModal);
                btnCancelForgot.addEventListener('click', closeForgotModal);
                
                formForgot.addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const email = document.getElementById('forgot-email').value;
                    const btnSubmit = document.getElementById('btn-submit-forgot-modal');
                    const originalText = btnSubmit.innerText;
                    btnSubmit.innerText = 'Đang gửi...';
                    btnSubmit.disabled = true;
                    
                    const { data, error } = await supabase.auth.resetPasswordForEmail(email, {
                        redirectTo: window.location.origin + '/Myan_CRM_Prototype/crm-frontend/reset-password.html'
                    });
                    
                    if(error) {
                        alert('Lỗi: ' + error.message);
                    } else {
                        alert('Đã gửi liên kết! Vui lòng kiểm tra hộp thư email của bạn.');
                        closeForgotModal();
                    }
                    btnSubmit.innerText = originalText;
                    btnSubmit.disabled = false;
                });
            }
"""
if "btn-forgot-pwd" not in html and "forgotModal" not in html:
    html = html.replace("});\n        </script></body></html>", js_logic + "\n        });\n        </script></body></html>")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)


# --- Creating reset-password.html based on index.html ---
# We will read the base index.html and remove the login forms, replacing it with a reset form
with open(index_path, "r", encoding="utf-8") as f:
    reset_html = f.read()

# Remove the Forgot modal in reset_html
r_soup = BeautifulSoup(reset_html, "html.parser")
forgot_modal = r_soup.find(id="forgot-modal")
if forgot_modal:
    forgot_modal.decompose()

# Change Title
if r_soup.title:
    r_soup.title.string = "Đặt lại mật khẩu - Myan Corp CRM"

# Replace standard form
form = r_soup.find("form", class_="space-y-lg")
if form:
    form.clear()
    form['id'] = 'form-reset-password'
    
    form_content = """
    <div class="text-center mb-6">
        <h3 class="font-headline-sm text-headline-sm text-on-surface font-bold">Tạo mật khẩu mới</h3>
        <p class="text-body-sm text-on-surface-variant mt-2">Vui lòng nhập mật khẩu mới bảo mật cho tài khoản của bạn.</p>
    </div>
    <div class="space-y-xs">
        <label for="new-password" class="block font-label-md text-label-md text-on-surface-variant">Mật khẩu mới</label>
        <input type="password" id="new-password" name="new-password" required class="w-full px-md py-sm rounded-lg border border-outline-variant bg-surface-container-lowest font-body-md text-body-md focus:outline-none transition-all" placeholder="Nhập mật khẩu mới">
    </div>
    <div class="space-y-xs">
        <label for="confirm-password" class="block font-label-md text-label-md text-on-surface-variant">Xác nhận mật khẩu</label>
        <input type="password" id="confirm-password" name="confirm-password" required class="w-full px-md py-sm rounded-lg border border-outline-variant bg-surface-container-lowest font-body-md text-body-md focus:outline-none transition-all" placeholder="Nhập lại mật khẩu mới">
    </div>
    <button type="submit" class="w-full py-sm rounded-lg bg-primary text-white font-label-md text-label-md hover:bg-primary-fixed-variant transition-colors shadow-sm">
        Cập nhật mật khẩu
    </button>
    """
    form.append(BeautifulSoup(form_content, "html.parser"))

# Remove Google button and Divider
btn_google = r_soup.find(id="btn-google-login")
if btn_google:
    btn_google.decompose()
divider = r_soup.find(lambda tag: tag.name == "span" and tag.text == "Hoặc")
if divider and divider.parent:
    divider.parent.decompose()
login_links = r_soup.find(lambda tag: tag.name == "div" and tag.find(lambda t: t.name == "a" and "Quên mật khẩu" in t.text))
if login_links:
    login_links.decompose()
create_acc_link = r_soup.find(lambda tag: tag.name == "div" and tag.find(lambda t: t.name == "a" and "Đăng ký ngay" in t.text))
if create_acc_link:
    create_acc_link.decompose()
h2_heading = r_soup.find("h2", string="Đăng nhập hệ thống")
if h2_heading:
    h2_heading.decompose()

# Replace scripts completely for reset page
scripts = r_soup.find_all("script")
last_script = scripts[-1] if scripts else None
if last_script:
    last_script.string = """
document.addEventListener('DOMContentLoaded', async () => {
    // Auth Guard - Supabase sẽ tự động cập nhật session từ URL Hash khi được chuyển hướng từ email
    
    // Đợi một chút để Supabase JS xử lý hash URL
    setTimeout(async () => {
        const { data: { session } } = await supabase.auth.getSession();
        if (!session) {
            alert('Đường dẫn không hợp lệ hoặc đã hết hạn.');
            window.location.href = 'index.html';
            return;
        }
    }, 1000);

    const form = document.getElementById('form-reset-password');
    if(form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const newPassword = document.getElementById('new-password').value;
            const confirmPassword = document.getElementById('confirm-password').value;
            
            if(newPassword !== confirmPassword) {
                alert('Mật khẩu không khớp!');
                return;
            }
            if(newPassword.length < 6) {
                alert('Mật khẩu phải có ít nhất 6 ký tự!');
                return;
            }
            
            const btn = form.querySelector('button[type="submit"]');
            const originalText = btn.innerText;
            btn.innerText = 'Đang cập nhật...';
            btn.disabled = true;
            
            const { data, error } = await supabase.auth.updateUser({
                password: newPassword
            });
            
            if (error) {
                alert('Lỗi cập nhật mật khẩu: ' + error.message);
                btn.innerText = originalText;
                btn.disabled = false;
            } else {
                alert('Mật khẩu đã được cập nhật thành công!');
                window.location.href = 'dashboard.html';
            }
        });
    }
});
"""

with open(reset_path, "w", encoding="utf-8") as f:
    f.write(str(r_soup))

print("Modified index.html and created reset-password.html successfully.")
