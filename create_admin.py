import urllib.request
import urllib.parse
import json

SUPABASE_URL = "https://wooyxavsxyqiutpxqatp.supabase.co"
SERVICE_ROLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Indvb3l4YXZzeHlxaXV0cHhxYXRwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MjU5MzAwNywiZXhwIjoyMDk4MTY5MDA3fQ.VaHut6mNzQmsYK9FgRX8hIdcZTKjH4UZO9jdNxok9bo"

headers = {
    "apikey": SERVICE_ROLE_KEY,
    "Authorization": f"Bearer {SERVICE_ROLE_KEY}",
    "Content-Type": "application/json"
}

email = "admin@myancorp.com"
password = "AdminPassword123!"

# 1. Create User
create_user_url = f"{SUPABASE_URL}/auth/v1/admin/users"
create_user_data = {
    "email": email,
    "password": password,
    "email_confirm": True,
    "user_metadata": {
        "full_name": "Admin MyanCorp"
    }
}
req1 = urllib.request.Request(create_user_url, data=json.dumps(create_user_data).encode('utf-8'), headers=headers, method='POST')

try:
    with urllib.request.urlopen(req1) as response:
        user_res = json.loads(response.read().decode('utf-8'))
        print("Created User:", user_res.get('id'))
except urllib.error.HTTPError as e:
    err = e.read().decode('utf-8')
    print("Error creating user (might already exist):", err)

# 2. Give it a bit of time for trigger to fire
import time
time.sleep(2)

# 3. Update profile role to admin
update_role_url = f"{SUPABASE_URL}/rest/v1/profiles?email=eq.{urllib.parse.quote(email)}"
update_role_data = {
    "role": "admin"
}
req2 = urllib.request.Request(update_role_url, data=json.dumps(update_role_data).encode('utf-8'), headers=headers, method='PATCH')

try:
    with urllib.request.urlopen(req2) as response:
        print("Updated Role. Response Code:", response.getcode())
except urllib.error.HTTPError as e:
    err = e.read().decode('utf-8')
    print("Error updating role:", err)

