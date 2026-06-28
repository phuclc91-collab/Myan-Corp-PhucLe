import os
import re
from bs4 import BeautifulSoup

out_dir = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype"
supabase_url = "https://wooyxavsxyqiutpxqatp.supabase.co"
supabase_anon = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Indvb3l4YXZzeHlxaXV0cHhxYXRwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI1OTMwMDcsImV4cCI6MjA5ODE2OTAwN30.3ATEaYxPVMKN8ZR_iCwvL-980mE8uaF2CH59W1kvqUU"

# Create supabase-config.js
config_js = f"""
const supabaseUrl = '{supabase_url}';
const supabaseKey = '{supabase_anon}';
const supabase = supabase.createClient(supabaseUrl, supabaseKey);
"""
with open(os.path.join(out_dir, "supabase-config.js"), "w", encoding="utf-8") as f:
    f.write(config_js)

files = ["index.html", "dashboard.html", "customers.html", "pipeline.html", "tasks.html", "payments.html", "settings.html"]

for file in files:
    path = os.path.join(out_dir, file)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # Inject Supabase CDN and config script at the end of body or head
    head = soup.find('head')
    if head:
        cdn_script = soup.new_tag("script", src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2")
        head.append(cdn_script)
        config_script = soup.new_tag("script", src="supabase-config.js")
        head.append(config_script)

    if file == "index.html":
        # Auth logic
        auth_script_content = """
        document.addEventListener('DOMContentLoaded', () => {
            const form = document.querySelector('form');
            if(form) {
                form.addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const email = document.getElementById('email').value;
                    const password = document.getElementById('password').value;
                    const btn = form.querySelector('button[type="submit"]');
                    const originalText = btn.innerText;
                    btn.innerText = 'Đang xử lý...';
                    
                    const { data, error } = await supabase.auth.signInWithPassword({
                        email: email,
                        password: password,
                    });
                    
                    if (error) {
                        alert('Lỗi đăng nhập: ' + error.message);
                        btn.innerText = originalText;
                    } else {
                        btn.innerText = 'Đăng nhập thành công!';
                        setTimeout(() => { window.location.href = 'dashboard.html'; }, 500);
                    }
                });
            }
        });
        """
        script_tag = soup.new_tag("script")
        script_tag.string = auth_script_content
        soup.body.append(script_tag)

        # Remove the previous inline script replacement that I did earlier
        script_tags = soup.find_all("script")
        for s in script_tags:
            if s.string and "btn.innerText = 'Đăng nhập thành công!'" in s.string and "form.addEventListener" not in s.string:
                s.decompose()

    else:
        # Auth guard for other pages
        guard_script = """
        document.addEventListener('DOMContentLoaded', async () => {
            const { data: { session } } = await supabase.auth.getSession();
            if (!session) {
                window.location.href = 'index.html';
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
        });
        """
        script_tag = soup.new_tag("script")
        script_tag.string = guard_script
        soup.body.append(script_tag)

    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))

print("Supabase connected to all files successfully.")
