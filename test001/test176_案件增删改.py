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
driver.get("http://192.168.2.176:86/#/case/index")

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

    # 上传卷宗
    # 上传卷宗
    time.sleep(1)
    current_time = "2025-03-18 11:09:31"
    user_login = "wxd341134"
    #
    # 1. 点击上传卷宗按钮
    upload_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//td[@title='(2025)苏0105民初0001号'][1]/ancestor::div[contains(@class, 'ant-table-content')]/div[3]/div[2]/div/table/tbody/tr[2]/td[3]/div/div[1]")))
    upload_button.click()
    time.sleep(2)  # 等待新页面加载
    #
    # 2. 点击上传zip按钮
    upload_zip_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='tree-button-group ant-btn-group']//button[2]")))
    upload_zip_button.click()
    time.sleep(1)

    # 3. 点击选择文件按钮并上传文件
    # file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//form/div/div[2]//span/div[1]/span[@role='button']//button[@type='button']")))
    # file_input.send_keys(r"E:\项目\法院项目\法官AI助手\材料\卷宗\(2024)鲁0502民初374号.zip")
    # 方法1：使用input标签直接上传
    file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
    file_input.send_keys(r"E:\项目\法院项目\法官AI助手\材料\卷宗\(2024)鲁0502民初374号.zip")
    print('zip文件上传成功')
    # 等待文件上传完成（这里可能需要更长的等待时间，取决于文件大小和网络速度）
    time.sleep(2)  # 调整等待时间

    # 4. 点击确定按钮
    confirm_button2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-modal-root']//button[2]")))
    confirm_button2.click()
    time.sleep(5)

    # 点击上传单个按钮
    upload_zip_button2 = wait.until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='custom-modal ant-modal-root custom-modal j-modal-box fullscreen custom-modal j-modal-box fullscreen']//button[3]")))
    upload_zip_button2.click()
    time.sleep(1)
    # 方法1：使用input标签直接上传
    file_input2 = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file' and contains(@accept, '.docx')]")))
    file_input2.send_keys(r"E:\项目\法院项目\法官AI助手\安装手册\法官AI助手安装文档.docx")
    print('单个文件上传成功')
    # 等待文件上传完成（这里可能需要更长的等待时间，取决于文件大小和网络速度）
    time.sleep(2)  # 调整等待时间

    # 4. 点击确定按钮
    confirm_button3 = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             "//div[.//div[@class='ant-modal-title' and text()='上传单个文件']]//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']")))
    confirm_button3.click()
    time.sleep(2)

    # 5. 点击刷新按钮
    # 等待并点击刷新按钮
    refresh_button_xpath = "//div[@class='tree-button-group ant-btn-group']//button[1]"
    refresh_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, refresh_button_xpath)))
    refresh_button.click()
    print('刷新按钮点击成功')
    time.sleep(1)

    # 等待并点击展开按钮
    expand_button_xpath = "//button[@ant-click-animating-without-extra-node='true']"
    expand_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, expand_button_xpath)))
    expand_button.click()
    time.sleep(1)
    print('展开点击成功')

    # 等待并点击关闭按钮
    close_button_xpath = "//div[@class='ant-modal-footer']//button[2]"
    close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, close_button_xpath)))
    close_button.click()
    time.sleep(2)
    print('关闭按钮点击成功')

    print(f"文件上传成功！上传时间：{current_time}, 上传用户：{user_login}")

    # 1. 点击右上角用户菜单
    user_menu = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']"
    )))
    user_menu.click()
    time.sleep(1)  # 等待下拉菜单显示
    # 报表统计
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
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-modal-footer']//button[2]")))
    confirm_button.click()

    print("密码修改成功！")

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
    # case_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'vue-treeselect__placeholder') and text()='请选择案件类型']")))
    # case_type_dropdown.click()
    # 直接定位input元素
    dropdown_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.vue-treeselect__input")))
    dropdown_input.click()

    # 选择民事诉讼
    civil_case_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'民事')]")))
    # 点击“民事”选项
    civil_case_option.click()
    print("民事已成功选中")
    civil_case_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'民事一审')]")))
    civil_case_option2.click()
    print("民事一审已成功选中")
    time.sleep(2)  # 暂停几秒以便观察结果

    # 选择案由类型
    reason_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'vue-treeselect__placeholder') and text()='请选择案由类型']/following-sibling::div//input[@class='vue-treeselect__input']")))
    reason_select.click()
    admin_case_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"行政案由")]')))
    admin_case_option.click()
    # pension_category_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"抚恤金类")]')))
    # pension_category_option.click()
    # demand_pension_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"要求发给抚恤金")]')))
    # demand_pension_option.click()
    print('案由已成功选中')
    time.sleep(2)  # 暂停几秒以便观察结果

    # # 输入原审案号
    print('开始输入原审案号')
    # 1. 定位到原审案号的输入框（通过placeholder文本定位）
    case_number_input = wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'ant-select-selection__placeholder') and text()='请输入原审案号']/ancestor::div[contains(@class, 'ant-select-selection')]")))

    # 2. 点击输入框
    case_number_input.click()
    time.sleep(1)

    # 3. 定位到真实的输入框并输入内容
    input_field = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "div[class='ant-select ant-select-open ant-select-focused ant-select-enabled ant-select-allow-clear ant-select-no-arrow'] input[class='ant-select-search__field']"
    )))
    input_field.send_keys("(2025)苏0105民初0001号")
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
    edit_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@title='(2025)苏0105民初0001号'][1]/ancestor::div[contains(@class, 'ant-table-content')]/div[3]/div[2]/div/table/tbody/tr/td[3]/div/div[3]")))
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
    delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@title='(2025)苏0105民初0001号'][1]/ancestor::div[contains(@class, 'ant-table-content')]/div[3]/div[2]/div/table/tbody/tr/td[3]/div/div[4]")))
    delete_button.click()

    # 等待删除确认弹窗并点击确认
    time.sleep(1)
    confirm_delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-modal-body']//button[2]")))
    confirm_delete_button.click()
    print('案件删除成功')
    time.sleep(2)




except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 关闭浏览器
    driver.quit()