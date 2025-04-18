from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test001.login import initialize_driver, login

old_username = "wxdfg"
old_password = "wxd341134@"
driver = initialize_driver()
driver, wait = login(driver, old_username, old_password, )
current_time = "2025-03-21 05:52:58"
user_login = "wxd341134"




WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='05cbfc42-613d-405c-8065-cedf7c7b9b39'] li:nth-child(2)"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select ant-select-enabled ant-select-allow-clear']//div[@class='ant-select-selection__rendered']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'全部')]"))).click()