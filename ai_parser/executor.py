from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def execute_instruction(driver, instruction):
    action = instruction.get("action")

    if action == "type":
        selector = instruction.get("selector")
        value = instruction.get("value")

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        element.clear()
        element.send_keys(value)

    elif action == "click":
        selector = instruction.get("selector")
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        element.click()

    else:
        raise ValueError(f"Action '{action}' not supported yet.")
