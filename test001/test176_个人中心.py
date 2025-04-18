from test001.login import initialize_driver, login
from selenium.webdriver.chrome.service import Service  # 导入 Service 类
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# # 指定 ChromeDriver 的路径
# chrome_driver_path = 'E:\AutoTest\FgAI\chromedriver-win64\chromedriver.exe'  # 替换为你的 chromedriver 路径
#
# # 创建 Service 对象
# service = Service(chrome_driver_path)
#
# # 使用 Service 对象启动 ChromeDriver
# driver = webdriver.Chrome(service=service)
#
# # 打开网页
# driver.get("http://192.168.2.176:86/#/case/index")
#
# # 打印网页标题
# print(driver.title)
#
#
# # 将浏览器窗口最大化
# driver.maximize_window()


try:
    old_username = "wxdfg"
    old_password = "wxd341134@"
    driver = initialize_driver()
    driver, wait = login(driver, old_username, old_password)
    time.sleep(2)
    # 指定 ChromeDriver 的路径

    # 等待页面加载完成
    wait = WebDriverWait(driver, 10)  # 设置最长等待时间为10秒
    # 1. 点击右上角用户菜单
    user_menu = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']"
    )))
    user_menu.click()
    time.sleep(1)  # 等待下拉菜单显示
#报表统计
    # 2. 点击下拉菜单中的"报表统计"选项
    report_stats = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//li[contains(text(),'报表统计')]"
    )))
    report_stats.click()
    time.sleep(1)

    # 3. 点击承办部门
    department = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//div[@title='按承办部门']"
    )))
    department.click()
    time.sleep(1)

    # 4. 选择承办人
    handler = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//li[contains(text(),'按承办人')]"
    )))
    handler.click()
    time.sleep(1)

    # 5. 点击查询按钮
    query_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//body//div//button[1]"
    )))
    query_button.click()
    time.sleep(2)  # 等待查询结果

    # 6. 点击导出按钮
    export_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//body//div//button[3]"
    )))
    export_button.click()
    time.sleep(3)  # 等待导出完成

    # 7. 再次点击右上角用户菜单
    user_menu2 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']"
    )))
    user_menu2.click()
    time.sleep(1)  # 等待下拉菜单显示
# 字体下载
    # 8. 点击下拉菜单中的"字体下载"选项
    font_download = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//li[contains(text(),'字体下载')]"
    )))
    font_download.click()
    time.sleep(1)

    # 9. 点击方正小标简体按钮
    fangzheng_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//div[@class='ant-modal-body']//button[2]"
    )))
    fangzheng_button.click()
    time.sleep(2)  # 等待下载开始

    # 10. 点击关闭弹框
    close_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[@class='ant-modal-close-x']"
    )))
    close_button.click()
    time.sleep(1)
#修改密码
    # 11. 点击右上角用户菜单
    user_menu3 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']")))
    user_menu3.click()
    time.sleep(1)  # 等待下拉菜单加载

    # 12. 下拉选择修改密码
    change_password_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'修改密码')]")))
    change_password_option.click()
    time.sleep(1)  # 等待对话框加载

    # 13. 输入原密码
    old_password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='请输入原密码']")))
    old_password_input.send_keys("wxd341134@")

    # 14. 输入新密码
    new_password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='请输入新密码']")))
    new_password_input.send_keys("wxd341134@")

    # 15. 确认输入新密码
    confirm_new_password_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='请再次输入新密码']")))
    confirm_new_password_input.send_keys("wxd341134@")

    # 16. 点击确定按钮
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-modal-root']//button[2]")))
    confirm_button.click()

    print("密码修改成功！")
    driver.quit()
    # . 点击返回图标
    # back_icon = wait.until(EC.element_to_be_clickable((
    #     By.XPATH, "//div[@class='fl doubleLogo marginleft_15']//div//img"
    # )))
    # back_icon.click()
    # time.sleep(1)
#验证新密码登录
    time.sleep(2)
    new_username = "wxdfg"
    new_password = "wxd341134@"
    driver = initialize_driver()
    driver, wait = login(driver, new_username, new_password, )
    time.sleep(2)
    print('再次登录成功')

#退出登录
    # 1. 点击右上角用户菜单
    user_menu4 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']")))
    user_menu4.click()
    time.sleep(1)  # 等待下拉菜单加载

    # 2. 下拉退出
    change_password_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'退出')]")))
    change_password_option.click()
    time.sleep(1)  # 等待对话框加载

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 关闭浏览器
    driver.quit()