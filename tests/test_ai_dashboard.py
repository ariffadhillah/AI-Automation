import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# simpan kedlam excel
# from reports.logger_excel import log_result

# simpan kedalanm csv
from reports.logger_csv import log_result



BASE_URL = "https://the-internet.herokuapp.com/login"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_input_integer_in_username(driver):
    test_name = "Input angka ke username"
    driver.get(BASE_URL)

    try:
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("123456")

        driver.find_element(By.CLASS_NAME, "radius").click()

        wait = WebDriverWait(driver, 10)
        error = wait.until(
            EC.presence_of_element_located((By.ID, "flash"))
        ).text

        assert "Your username is invalid!" in error
        print("✅ Test Passed: Integer input ditolak sebagai username")
        log_result(test_name, "Passed", "Validasi error muncul")

    except Exception as e:
        log_result(test_name, "Failed", str(e))
        pytest.fail(f"❌ Test Failed: {str(e)}")
