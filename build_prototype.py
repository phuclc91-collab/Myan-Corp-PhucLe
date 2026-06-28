import os
import shutil
import re
from bs4 import BeautifulSoup

base_dir = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/DESIGN-STITCH"
out_dir = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

files = [
    ("stitch_giao_di_n_auth_myan_crm", "index.html"),
    ("stitch_giao_di_n_auth_myan_crm (1)", "dashboard.html"),
    ("stitch_giao_di_n_auth_myan_crm (2)", "customers.html"),
    ("stitch_giao_di_n_auth_myan_crm (3)", "pipeline.html"),
    ("stitch_giao_di_n_auth_myan_crm (4)", "tasks.html"),
    ("stitch_giao_di_n_auth_myan_crm (5)", "payments.html"),
    ("stitch_giao_di_n_auth_myan_crm (6)", "settings.html")
]

# Map menu names to files
menu_map = {
    "Tổng quan": "dashboard.html",
    "Khách hàng": "customers.html",
    "Cơ hội bán hàng": "pipeline.html",
    "Công việc": "tasks.html",
    "Thanh toán": "payments.html",
    "Cài đặt": "settings.html"
}

for folder, out_name in files:
    in_path = os.path.join(base_dir, folder, "code.html")
    out_path = os.path.join(out_dir, out_name)
    
    if not os.path.exists(in_path):
        print(f"File not found: {in_path}")
        continue
        
    with open(in_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace login script in index.html
    if out_name == "index.html":
        # simple regex to replace button action
        html = re.sub(
            r"btn\.innerText = 'Đăng nhập thành công!';.*",
            r"btn.innerText = 'Đăng nhập thành công!'; setTimeout(() => { window.location.href = 'dashboard.html'; }, 500);",
            html,
            flags=re.DOTALL
        )
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Update sidebar links
    for a in soup.find_all('a'):
        text = a.get_text().strip()
        for k, v in menu_map.items():
            if k in text:
                a['href'] = v
                break
                
    # Also fix any logout buttons
    for button in soup.find_all(['button', 'a']):
        text = button.get_text().strip()
        if "Đăng xuất" in text:
            if button.name == 'a':
                button['href'] = 'index.html'
            else:
                button['onclick'] = "window.location.href='index.html'"
                
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Prototype built successfully in", out_dir)
