from ai_parser.prompt_parser import parse_prompt
from ai_parser.executor import execute_instruction

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 1. Ambil prompt dari AI
prompt = "Try entering an integer in the 'Full Name' field"
instruction = parse_prompt(prompt)

# 2. Setup browser
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# 3. Arahkan ke halaman (kita gunakan halaman dummy sementara)
driver.get("https://the-internet.herokuapp.com/login")

# 4. Eksekusi instruksi AI
try:
    execute_instruction(driver, instruction)
    print("✅ Prompt berhasil dieksekusi di browser")
except Exception as e:
    print("❌ Gagal menjalankan instruksi:", e)

# Tunggu biar kelihatan
input("Tekan ENTER untuk tutup browser...")
driver.quit()
