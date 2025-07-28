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



WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "td[title='(2025)苏0105民初0001号'] ~ td:last-child .custom-svg-icon:nth-of-type(3) svg"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//td[@title='(2024)鲁0502民初374号']/ancestor::tr/td[11]/div/div[3]//*[name()='svg']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[local-name()='use' and @*='#icon-reverse-left']"))).click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'layer-header')))

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[3]/div/div[3]"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td[title='(2025)苏0105民初0001号'] ~ td:last-child .custom-svg-icon:nth-of-type(3) svg"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//td[@title='(2025)苏0105民初0001号']/ancestor::tr/td[11]/div/div[3]//*[name()='use']"))).click()