from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

from test001.login import initialize_driver, login

try:
    old_username = "wxdfg"
    old_password = "wxd341134@"
    driver = initialize_driver()
    driver, wait = login(driver, old_username, old_password,)
    time.sleep(2)


    # 1. 点击案件编号输入框并输入内容
    case_number_input = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[@class='ant-input-affix-wrapper']//input[@placeholder='请输入案件编号']"
    )))
    case_number_input.click()
    case_number_input.clear()  # 清除可能存在的内容
    case_number_input.send_keys("2025")
    time.sleep(1)

    # 2. 点击案件名称输入框并输入内容
    case_name_input = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[@class='ant-input-affix-wrapper']//input[@placeholder='请输入案件名称']"
    )))
    case_name_input.click()
    case_name_input.clear()  # 清除可能存在的内容
    case_name_input.send_keys("(2025)苏0105民初0001号")
    time.sleep(1)

    # 3. 点击下拉图标
    dropdown_icon = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//label[@title='判决书状态']/ancestor::div[@class='form-item ant-row ant-form-item']/div[2]/div/span"
    )))
    dropdown_icon.click()
    time.sleep(1)  # 等待下拉菜单显示

    # 4. 选择"未生成"选项
    ungenerated_option = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//li[contains(text(),'未生成')]"
    )))
    ungenerated_option.click()
    time.sleep(1)

    # 5. 点击查询按钮
    query_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//body//div//button[1]"
    )))
    query_button.click()
    print('查询成功')
    time.sleep(2)  # 等待查询结果加载

    #6.点击重置按钮
    reset_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//body//div//button[3]"
    )))
    reset_button.click()
    print('重置查询成功')
    time.sleep(1)




except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 关闭浏览器
    driver.quit()