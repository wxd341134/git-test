from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 导入 Service 类

# 指定 ChromeDriver 的路径
chrome_driver_path = '/chromedriver-win64/chromedriver.exe'  # 替换为你的 chromedriver 路径

# 创建 Service 对象
service = Service(chrome_driver_path)

# 使用 Service 对象启动 ChromeDriver
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get("http://192.168.2.76:86/#/case/index")

# 打印网页标题
print(driver.title)



try:
    # 等待页面加载
    time.sleep(2)  # 根据需要调整等待时间或使用显式等待

    # 定位用户名输入框并输入用户名
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入账号']")
    username_field.send_keys("wxdfg")  # 替换为实际的用户名
    time.sleep(1)

    # 定位密码输入框并输入密码
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']")
    password_field.send_keys("wxd341134@")  # 替换为实际的密码
    time.sleep(1)

    # 定位验证码输入框并输入验证码
    captcha_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入验证码']")
    captcha_field.send_keys("captcha_code")  # 替换为你识别到的验证码


    # 定位登录按钮并点击
    login_button = driver.find_element(By.XPATH,"//button[@type='button']")
    login_button.click()

    # 可以添加更多的逻辑来验证是否登录成功
    time.sleep(5)  # 暂停几秒以便观察结果

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 关闭浏览器
    driver.quit()