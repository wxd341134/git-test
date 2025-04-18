from selenium.webdriver.chrome.service import Service  # 导入 Service 类
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from urllib3.util import wait

# 指定 ChromeDriver 的路径
chrome_driver_path = '/chromedriver-win64/chromedriver.exe'  # 替换为你的 chromedriver 路径

# 创建 Service 对象
service = Service(chrome_driver_path)

# 使用 Service 对象启动 ChromeDriver
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get("http://192.168.2.76:86/#/case/index")

# 将浏览器窗口最大化
driver.maximize_window()

# 打印网页标题
print(driver.title)

# 等待页面加载完成
wait = WebDriverWait(driver, 10)  # 设置最长等待时间为10秒

# 定位用户名输入框并输入用户名
username_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入账号']")
username_field.send_keys("wxdfg")  # 替换为实际的用户名
time.sleep(1)

# 定位密码输入框并输入密码
password_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']")
password_field.send_keys("wxd341134@")  # 替换为实际的密码
time.sleep(5)

#    # 定位验证码图片元素，并打印提示信息让用户查看验证码
# captcha_element = driver.find_element(By.XPATH, '//img[contains(@src, "/judge-ai/captcha")]')
# print("请查看页面上的验证码，并在接下来的输入框中输入验证码：")
#
#     # 等待用户手动输入验证码
# captcha_text = input("请输入验证码: ")
#
# # 填写验证码到输入框（使用提供的XPath表达式）
# input_element = driver.find_element(By.XPATH, "//input[@placeholder='请输入验证码']")
# input_element.clear()
# input_element.send_keys(captcha_text)


    # 定位登录按钮并点击
login_button = driver.find_element(By.XPATH,"//button[@type='button']")
login_button.click()

    # 可以添加更多的逻辑来验证是否登录成功
time.sleep(3)  # 暂停几秒以便观察结果

    # 点击添加按钮
print('点击添加按钮')
add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ant-form-item-children']/button[./span[text()='添加']]")))
add_button.click()

    # 输入案件名称
print('输入案件名称')

# case_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[.//div[text()='新增案件']]/../following-sibling::div[1]//input[@placeholder='请输入案件名称']")))
# case_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[1]/div/div[2]/div/span/input")))
# case_name_input.send_keys("(2025)苏0105民初0001号")


# 输入案件编号
case_number_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[3]/div/div[2]/div/span/input")))
case_number_input.send_keys("(2025)苏0105民初0001号")

# 选择案件类型
case_type_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[4]/div/div[2]/div/span/div/div/div/div")))
case_type_dropdown.click()

# 选择民事诉讼
civil_litigation_option = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[4]/div/div[2]/div/span/div/div/div/div[2]')))
civil_litigation_option.click()

# 选择民事诉讼
# 获取下拉框的所有选项
options = case_type_dropdown.find_elements(By.XPATH, ".//div[@class='ant-select-selection-selected-value'][text()='民事诉讼']")
print(options)
# try:
#     # 等待页面加载完成
#     wait = WebDriverWait(driver, 10)  # 设置最长等待时间为10秒
#
#     # 定位用户名输入框并输入用户名
#     username_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入账号']")
#     username_field.send_keys("wxdfg")  # 替换为实际的用户名
#     time.sleep(1)
#
#     # 定位密码输入框并输入密码
#     password_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']")
#     password_field.send_keys("wxd341134@")  # 替换为实际的密码
#     time.sleep(1)
#
#     # 定位验证码图片元素，并打印提示信息让用户查看验证码
#     captcha_element = driver.find_element(By.XPATH, '//img[contains(@src, "/judge-ai/captcha")]')
#     print("请查看页面上的验证码，并在接下来的输入框中输入验证码：")
#
#     # 等待用户手动输入验证码
#     captcha_text = input("请输入验证码: ")
#
#     # 填写验证码到输入框（使用提供的XPath表达式）
#     input_element = driver.find_element(By.XPATH, "//input[@placeholder='请输入验证码']")
#     input_element.clear()
#     input_element.send_keys(captcha_text)
#
#
#     # 定位登录按钮并点击
#     login_button = driver.find_element(By.XPATH,"//button[@type='button']")
#     login_button.click()
#
#     # 可以添加更多的逻辑来验证是否登录成功
#     time.sleep(3)  # 暂停几秒以便观察结果
#
#     # 点击添加按钮
#     print('点击添加按钮')
#     add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ant-form-item-children']/button[./span[text()='添加']]")))
#     add_button.click()
#
#     # 输入案件名称
#     print('输入案件名称')
#
#     #case_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[.//div[text()='新增案件']]/../following-sibling::div[1]//input[@placeholder='请输入案件名称']")))
#     # case_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[1]/div/div[2]/div/span/input")))
#     # case_name_input.send_keys("(2025)苏0105民初0001号")
#
#     # 定位并填写案件编号
#     # case_number_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="请输入案件编号"]')))
#     # case_number_input.send_keys('(2025)苏0105民初0001号')
#
#     time.sleep(2)  # 暂停几秒以便观察结果
#
#
# except Exception as e:
#     print(f"An error occurred: {e}")
#
# finally:
#     # 关闭浏览器
#     driver.quit()