from datetime import datetime
from ai_parser.prompt_parser import parse_prompt
from ai_parser.prompt_parser_smart import smart_parse_prompt
from ai_parser.executor import execute_instruction
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import os

# Daftar prompt AI yang ingin dieksekusi
# prompts = [
#     "Try entering an integer in the 'Full Name' field",
#     "Try entering an integer in the 'Password' field",
#     "Click the Login button"
# ]

# prompts = [
#     "Enter username tomsmith into the username field",
#     "Enter password SuperSecretPassword! into the password field",
#     "Click the Login button"
# ]

# daftar prompt smart
prompts = [
    "Type tomsmith into the username field",
    "Enter SuperSecretPassword! into the password field",
    "Click the login button"
]


# Inisialisasi driver Selenium
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Buka halaman login
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

log_results = []

def save_screenshot(driver, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{step_name}_{timestamp}.png"
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(filename)
    return filename


for i, prompt in enumerate(prompts, start=1):
    try:
        instruksi = parse_prompt(prompt)
        execute_instruction(driver, instruksi)
        
        # ✅ Tambahkan validasi login di sini
        if "login" in prompt.lower():
            time.sleep(2)
            if "You logged into a secure area!" in driver.page_source:
                log_results.append([f"Step {i}", prompt, "Passed", "Login successful"])
            else:
                # log_results.append([f"Step {i}", prompt, "Failed", "Login failed or message not found"])
                
                screenshot_path = save_screenshot(driver, f"step{i}_login_failed")
                log_results.append([f"Step {i}", prompt, "Failed", f"Login failed (screenshot: {screenshot_path})"])

            continue  # ⛔ Hindari log ganda (jangan lanjut ke append default)

        # 📝 Jika bukan step login, lanjut append biasa
        log_results.append([f"Step {i}", prompt, "Passed", "Executed successfully"])

    # except Exception as e:
    #     log_results.append([f"Step {i}", prompt, "Failed", str(e)])


    except Exception as e:
        screenshot_path = save_screenshot(driver, f"step{i}")
        log_results.append([f"Step {i}", prompt, "Failed", f"{str(e)} (screenshot: {screenshot_path})"])


# Buat folder logs/ jika belum ada
os.makedirs("logs", exist_ok=True)

# Simpan ke CSV
with open("logs/result.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Step", "Prompt", "Status", "Message"])
    writer.writerows(log_results)

print("✅ Hasil log disimpan di logs/result.csv")

# Tunggu supaya bisa dilihat
input("🧪 Semua prompt dijalankan. Tekan ENTER untuk menutup browser...")
driver.quit()