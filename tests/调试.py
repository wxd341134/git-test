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



WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-radio-input"))).click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ant-radio-wrapper"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "layer-header"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".layer-header"))).click()


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-radio-input"))).click()


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ant-radio-input[value='false']"))).click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//label[.//span[text()='不认同']]"))).click()


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-radio-wrapper > span.ant-radio > input[value='false']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='page-control']//*[name()='svg']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//form[@class='ant-form ant-form-horizontal']//label[span='不认同']/span/input[@type='radio']"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@value='true']//button[1]"))).click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'layer-header')))