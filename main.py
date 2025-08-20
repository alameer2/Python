import subprocess
import http.server
import socketserver
import threading
import os

# ---------- 1) تحديد الرابط ----------
url = "https://ak.sv"   # ← غيّر الرابط للموقع اللي تبغاه
output_folder = "my_website_copy"

# ---------- 2) تحميل الموقع ----------
if not os.path.exists(output_folder):
    print("📥 جاري تحميل الموقع...")
    subprocess.run([
        "httrack",
        url,
        "-O", output_folder,
        "--quiet"
    ])
    print("✅ تم النسخ!")
else:
    print("⚡ تم العثور على نسخة سابقة، استخدام المجلد مباشرة.")

# ---------- 3) تشغيل سيرفر محلي ----------
PORT = 8000

def start_server():
    os.chdir(output_folder)  # ادخل المجلد اللي فيه الموقع
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"🌍 الموقع شغال على http://localhost:{PORT}")
        httpd.serve_forever()

# تشغيل السيرفر في Thread منفصل
thread = threading.Thread(target=start_server)
thread.start()