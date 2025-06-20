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



WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.header svg.svg-icon use"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='旧版本：']/following-sibling::div[1]/div[@role='combobox']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[local-name()='use' and @*='#icon-reverse-left']"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "div.header svg.svg-icon use"))).click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'layer-header')))

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[local-name()='use' and @*='#icon-reverse-left']"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.header svg.svg-icon use"))).click()