from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

from test001.login import initialize_driver, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    old_username = "wxdfg"
    old_password = "wxd341134@"
    driver = initialize_driver()
    driver, wait = login(driver, old_username, old_password,)
    current_time = "2025-03-21 05:52:58"
    user_login = "wxd341134"
    print(f"开始执行辅助阅卷自动化测试 - 时间: {current_time}, 用户: {user_login}")

    # 1. 点击辅助阅卷
    try:
        auxiliary_reading = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//td[@title='(2025)苏0105民初0001号'][1]/ancestor::div[contains(@class, 'ant-table-content')]/div[3]/div[2]/div/table/tbody/tr/td[1]"
        )))
        auxiliary_reading.click()
        print("步骤1执行成功：点击辅助阅卷")
        time.sleep(2)
    except Exception as e:
        print(f"步骤1执行失败：点击辅助阅卷时出错 - {str(e)}")
        raise

    # 2. 点击庭审笔录1
    try:
        court_record = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//span[@class='ant-tree-title']/span[text()='庭审笔录1']"
        )))
        court_record.click()
        print("步骤2执行成功：点击庭审笔录1")
        time.sleep(1)
    except Exception as e:
        print(f"步骤2执行失败：点击庭审笔录1时出错 - {str(e)}")
        raise

    # 3. 点击设为庭审笔录
    try:
        set_record = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[@class='title' and contains(text(),'庭审笔录1')]/../following-sibling::i[@aria-label='图标: copy']"
        )))
        set_record.click()
        print("步骤3执行成功：点击设为庭审笔录")
        time.sleep(1)
    except Exception as e:
        print(f"步骤3执行失败：点击设为庭审笔录时出错 - {str(e)}")
        raise

    # 4. 输入原告处理意见1
    try:
        opinion1 = wait.until(EC.presence_of_element_located((
            By.XPATH, "//form/div[6]/div/div[1]/div[3]/div[2]/div/span/textarea[@placeholder='请输入处理意见']"
        )))
        opinion1.clear()
        opinion1.send_keys("无意见1")
        print("步骤4执行成功：输入原告处理意见1")
        time.sleep(1)
    except Exception as e:
        print(f"步骤4执行失败：输入原告处理意见1时出错 - {str(e)}")
        raise

    # 5. 输入原告处理意见2
    try:
        opinion2 = wait.until(EC.presence_of_element_located((
            By.XPATH, "//form/div[6]/div/div[2]/div[3]/div[2]/div/span/textarea[@placeholder='请输入处理意见']"
        )))
        opinion2.clear()
        opinion2.send_keys("无意见2")
        print("步骤5执行成功：输入原告处理意见2")
        time.sleep(1)
    except Exception as e:
        print(f"步骤5执行失败：输入原告处理意见2时出错 - {str(e)}")
        raise

    # 6. 点击确定按钮
    try:
        confirm_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='ant-btn ant-btn-primary']"
        )))
        confirm_button.click()
        print("步骤6执行成功：点击确定按钮")
        time.sleep(2)
    except Exception as e:
        print(f"步骤6执行失败：点击确定按钮时出错 - {str(e)}")
        raise

    print("\n测试执行完成!")
    print("执行信息汇总:")
    print(f"执行时间: {current_time}")
    print(f"执行用户: {user_login}")
    print("执行步骤:")
    print("1. 点击辅助阅卷")
    print("2. 点击庭审笔录1")
    print("3. 点击设为庭审笔录")
    print("4. 输入原告处理意见1: 无意见1")
    print("5. 输入原告处理意见2: 无意见2")
    print("6. 点击确定按钮")

except Exception as e:
    print(f"\n测试执行失败!")
    print(f"失败时间: {current_time}")
    print(f"执行用户: {user_login}")
    print(f"错误信息: {str(e)}")

finally:
    print("\n测试执行结束")
    # 关闭浏览器
    driver.quit()








