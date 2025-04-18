from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from test001.login import initialize_driver, login

try:
    old_username = "wxdfg"
    old_password = "wxd341134@"
    print("Initializing driver...")  # 打印日志以确认函数调用
    driver = initialize_driver()
    driver, wait = login(driver, old_username, old_password)
    time.sleep(2)

    # print('点击添加按钮')
    # add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//body//div//button[2]")))
    # add_button.click()
    # time.sleep(2)  # 暂停几秒以便观察结果
    #
    # # 添加案件名称
    # print('输入案件名称')
    # case_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-col ant-col-24']//input[@placeholder='请输入案件名称']")))
    # case_name_input.send_keys("(2025)苏0105民初0001号")
    # time.sleep(1)  # 暂停几秒以便观察结果
    #
    # # 输入案件编号
    # case_number_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-col ant-col-12']//input[@placeholder='请输入案件编号']")))
    # case_number_input.send_keys("(2025)苏0105民初0001号")
    #
    # # 定位案件类型
    # # case_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'vue-treeselect__placeholder') and text()='请选择案件类型']")))
    # # case_type_dropdown.click()
    # # 直接定位input元素
    # dropdown_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.vue-treeselect__input")))
    # dropdown_input.click()
    #
    # # 选择民事诉讼
    # civil_case_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'民事')]")))
    # # 点击“民事”选项
    # civil_case_option.click()
    # print("民事已成功选中")
    # civil_case_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'民事一审')]")))
    # civil_case_option2.click()
    # print("民事一审已成功选中")
    # time.sleep(2)  # 暂停几秒以便观察结果
    #
    # # 选择案由类型
    # reason_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'vue-treeselect__placeholder') and text()='请选择案由类型']/following-sibling::div//input[@class='vue-treeselect__input']")))
    # reason_select.click()
    # admin_case_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"行政案由")]')))
    # admin_case_option.click()
    # # pension_category_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"抚恤金类")]')))
    # # pension_category_option.click()
    # # demand_pension_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"要求发给抚恤金")]')))
    # # demand_pension_option.click()
    # print('案由已成功选中')
    # time.sleep(2)  # 暂停几秒以便观察结果
    #
    # # # 输入原审案号
    # print('开始输入原审案号')
    # # 1. 定位到原审案号的输入框（通过placeholder文本定位）
    # case_number_input = wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'ant-select-selection__placeholder') and text()='请输入原审案号']/ancestor::div[contains(@class, 'ant-select-selection')]")))
    #
    # # 2. 点击输入框
    # case_number_input.click()
    # time.sleep(1)
    #
    # # 3. 定位到真实的输入框并输入内容
    # input_field = wait.until(EC.presence_of_element_located((
    #     By.CSS_SELECTOR, "div[class='ant-select ant-select-open ant-select-focused ant-select-enabled ant-select-allow-clear ant-select-no-arrow'] input[class='ant-select-search__field']"
    # )))
    # input_field.send_keys("(2025)苏0105民初0001号")
    # time.sleep(1)
    #
    # # 选择立案日期
    # print('开始选择立案日期')
    # # 等待并点击占位符文本所在的输入框
    # placeholder = wait.until(EC.element_to_be_clickable((By.XPATH, "//form/div/div[7]//input[@placeholder='选择开始日期']")))
    # placeholder.click()
    # # 等待并定位实际的输入框
    # today_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="今天"]')))
    # today_option.click()
    # time.sleep(2)
    #
    # # 点击确定按钮
    # confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="ant-modal-root"]//button[2]')))
    # confirm_button.click()

    #上传卷宗
    # 上传卷宗
    time.sleep(1)
    current_time = "2025-03-18 11:09:31"
    user_login = "wxd341134"
    #
    # 1. 点击上传卷宗按钮
    upload_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//td[@title='(2025)苏0105民初0001号'][1]/ancestor::div[contains(@class, 'ant-table-content')]/div[3]/div[2]/div/table/tbody/tr[2]/td[3]/div/div[1]")))
    upload_button.click()
    time.sleep(2)  # 等待新页面加载
    #
    #2. 点击上传zip按钮
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
        EC.element_to_be_clickable((By.XPATH, "//div[@class='custom-modal ant-modal-root custom-modal j-modal-box fullscreen custom-modal j-modal-box fullscreen']//button[3]")))
    upload_zip_button2.click()
    time.sleep(1)
    # 方法1：使用input标签直接上传
    file_input2 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file' and contains(@accept, '.docx')]")))
    file_input2.send_keys(r"E:\项目\法院项目\法官AI助手\安装手册\法官AI助手安装文档.docx")
    print('单个文件上传成功')
    # 等待文件上传完成（这里可能需要更长的等待时间，取决于文件大小和网络速度）
    time.sleep(2)  # 调整等待时间

    # 4. 点击确定按钮
    confirm_button3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[.//div[@class='ant-modal-title' and text()='上传单个文件']]//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']")))
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



except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 关闭浏览器
    driver.quit()