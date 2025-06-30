import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/login"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_input_integer_in_username(driver):
    driver.get(BASE_URL)

    try:
        # Isi username dengan angka
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("123456")

        # Klik login tanpa password
        driver.find_element(By.CLASS_NAME, "radius").click()

        # Tunggu error muncul
        wait = WebDriverWait(driver, 10)
        error = wait.until(
            EC.presence_of_element_located((By.ID, "flash"))
        ).text

        assert "Your username is invalid!" in error
        print("✅ Test Passed: Integer input ditolak sebagai username")

    except Exception as e:
        pytest.fail(f"❌ Test Failed: {str(e)}")
