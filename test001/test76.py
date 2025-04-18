from selenium.webdriver.chrome.service import Service  # 导入 Service 类
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 指定 ChromeDriver 的路径
chrome_driver_path = 'E:\AutoTest\FgAI\chromedriver-win64\chromedriver.exe'  # 替换为你的 chromedriver 路径

# 创建 Service 对象
service = Service(chrome_driver_path)

# 使用 Service 对象启动 ChromeDriver
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get("http://192.168.2.76:86/#/case/index")

# 打印网页标题
print(driver.title)


# 将浏览器窗口最大化
driver.maximize_window()



try:
    # 等待页面加载完成
    wait = WebDriverWait(driver, 10)  # 设置最长等待时间为10秒

    # 定位用户名输入框并输入用户名
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入账号']")
    username_field.send_keys("wxdfg")  # 替换为实际的用户名
    time.sleep(1)

    # 定位密码输入框并输入密码
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']")
    password_field.send_keys("wxd341134@")  # 替换为实际的密码
    time.sleep(1)

       # 定位验证码图片元素，并打印提示信息让用户查看验证码
    captcha_element = driver.find_element(By.XPATH, '//img[contains(@src, "/judge-ai/captcha")]')
    print("请查看页面上的验证码，并在接下来的输入框中输入验证码：")

        # 等待用户手动输入验证码
    captcha_text = input("请输入验证码: ")

    # 填写验证码到输入框（使用提供的XPath表达式）
    input_element = driver.find_element(By.XPATH, "//input[@placeholder='请输入验证码']")
    input_element.clear()
    input_element.send_keys(captcha_text)

    # 定位登录按钮并点击
    login_button = driver.find_element(By.XPATH, "//button[@type='button']")
    login_button.click()

    # 可以添加更多的逻辑来验证是否登录成功
    time.sleep(2)  # 暂停几秒以便观察结果

    print('点击添加按钮')
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//body//div//button[2]")))
    add_button.click()
    time.sleep(2)  # 暂停几秒以便观察结果

    # 添加案件名称
    print('输入案件名称')
    case_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-col ant-col-24']//input[@placeholder='请输入案件名称']")))
    case_name_input.send_keys("(2025)苏0105民初0001号")
    time.sleep(1)  # 暂停几秒以便观察结果

    # 输入案件编号
    case_number_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-col ant-col-12']//input[@placeholder='请输入案件编号']")))
    case_number_input.send_keys("(2025)苏0105民初0001号")

    # 定位案件类型
    case_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-selection__placeholder' and text()='请选择类型']")))
    case_type_dropdown.click()

    # 选择民事诉讼
    # 定位“民事诉讼”选项
    civil_case_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'民事诉讼')]")))
    # 点击“民事诉讼”选项
    civil_case_option.click()
    print("民事诉讼选项已成功选中")
    time.sleep(2)  # 暂停几秒以便观察结果

    # 选择案由类型
    reason_select = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@class="vue-treeselect__input"]')))
    reason_select.click()
    admin_case_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"行政案由")]')))
    admin_case_option.click()
    pension_category_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"抚恤金类")]')))
    pension_category_option.click()
    demand_pension_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"要求发给抚恤金")]')))
    demand_pension_option.click()
    print('案由已成功选中')
    time.sleep(2)  # 暂停几秒以便观察结果

    # # 输入原审案号
    print('开始输入原审案号')
    original_case_number_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-select-selection__placeholder' and text()='请输入原审案号']")))
    # 由于该元素可能是一个div，我们需要首先点击它以激活输入框
    original_case_number_input.click()
    # 然后定位实际的输入框并输入值
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@ect-enabled ant-select-no-arrow']//input[@class='ant-select-search__field']")))
    input_box.send_keys('(2025)苏0105民初0001号')
    time.sleep(1)

    # 选择立案日期
    print('开始选择立案日期')
    # 等待并点击占位符文本所在的输入框
    placeholder = wait.until(EC.element_to_be_clickable((By.XPATH, "//form/div/div[7]//input[@placeholder='选择开始日期']")))
    placeholder.click()
    # 等待并定位实际的输入框
    today_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="今天"]')))
    today_option.click()
    time.sleep(2)

    # 点击确定按钮
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="ant-modal-root"]//button[2]')))
    confirm_button.click()

    # 定位并点击“修改”按钮
    print('开始编辑案件')
    time.sleep(1)
    # 定位并点击编辑图标
    # 定位包含编辑图标的div元素
    edit_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@title='(2025)苏0105民初0001号'][1]/ancestor::tr//td[9]/div/div[3]")))
    edit_icon.click()

    # 等待案件名称输入框可见并修改其内容
    case_name_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='ant-col ant-col-24']//input[@placeholder='请输入案件名称']")))
    # 先全选输入框中的内容，然后按退格键删除
    case_name_input.send_keys(Keys.CONTROL + "a")  # 全选
    case_name_input.send_keys(Keys.BACKSPACE)  # 删除
    time.sleep(1)  # 等待清空完成
    case_name_input.send_keys('(2025)苏0105民初0001号修改')
    time.sleep(2)  # 观察2秒
    # 点击"确定"按钮
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-modal-root']//button[2]")))
    confirm_button.click()

    # 可以添加一些等待时间以确保操作完成
    time.sleep(3)
    # 2. 删除操作
    # 定位到删除按钮
    delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@title='(2025)苏0105民初0001号'][1]/ancestor::tr//td[9]/div/div[4]")))
    delete_button.click()

    # 等待删除确认弹窗并点击确认
    confirm_delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-modal-body']//button[2]")))
    confirm_delete_button.click()
    time.sleep(2)




except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 关闭浏览器
    driver.quit()