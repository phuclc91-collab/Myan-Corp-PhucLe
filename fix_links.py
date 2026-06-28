import os
from bs4 import BeautifulSoup

files = [
    "dashboard.html",
    "customers.html",
    "pipeline.html",
    "tasks.html",
    "payments.html",
    "settings.html"
]

base_dir = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype/crm-frontend"

def get_link_by_text(text, html_str):
    t = text.lower()
    if 'tổng quan' in t or 'overview' in t or 'dashboard' in t: return 'dashboard.html'
    if 'khách hàng' in t or 'customers' in t or 'group' in t: return 'customers.html'
    if 'cơ hội' in t or 'sales' in t or 'pipeline' in t or 'trending_up' in t: return 'pipeline.html'
    if 'công việc' in t or 'tasks' in t or 'task' in t: return 'tasks.html'
    if 'thanh toán' in t or 'payments' in t: return 'payments.html'
    if 'cài đặt' in t or 'settings' in t: return 'settings.html'
    if 'hồ sơ cá nhân' in t or 'tài khoản' in t or 'danh mục' in t: return 'settings.html'
    return None

for file_name in files:
    path = os.path.join(base_dir, file_name)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    
    soup = BeautifulSoup(html, "html.parser")
    # For sidebar/nav links
    asides = soup.find_all("aside")
    for aside in asides:
        links = aside.find_all("a")
        for a in links:
            text = a.get_text()
            icon_span = a.find("span", class_="material-symbols-outlined")
            icon_text = icon_span.get_text() if icon_span else ""
            
            target_href = get_link_by_text(text, str(a))
            if not target_href and icon_text:
                target_href = get_link_by_text(icon_text, str(a))
            
            if target_href:
                a['href'] = target_href

    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    
    print(f"Fixed links in {file_name}")
