import pytest
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from pages.base_page import BasePage
from pages.login_page import LoginPage
from test001.login import initialize_driver, login
from utils.logger2 import Logger


logger = Logger().get_logger()

class TestPersonalCenter:
    """个人中心功能测试类"""

    @pytest.fixture(scope="class", autouse=True)
    def setup_driver(self, driver):
        """
        设置 driver 实例
        """
        TestPersonalCenter.driver = driver
        logger.info("开始执行个人中心测试")
        yield
        logger.info("个人中心测试执行完成")

    @allure.feature("个人中心")
    @allure.story("完整测试流程")
    def test_personal_center_workflow(self):
        """测试个人中心完整流程"""
        try:
            # 登录
            self.base_page = BasePage(self.driver)
            self.login_page = LoginPage(self.driver)
            # 执行登录
            self.login_page.login("wxdfg", "wxd341134@")
            logger.info("完成登录")
            time.sleep(2)  # 等待页面加载完成

            # 1. 报表统计
            self.do_report_statistics()

            # 2. 字体下载
            self.do_font_download()

            # 3. 修改密码 (修改密码后系统会自动退出)
            self.do_change_password()

            # 4. 直接使用新密码登录
            self.do_verify_new_password()

        except Exception as e:
            logger.error(f"个人中心测试流程失败: {str(e)}")
            allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            raise

    def click_user_menu(self):
        """点击右上角用户菜单"""
        try:
            with allure.step("点击右上角用户菜单"):
                # 等待并点击右上角用户菜单
                user_menu = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']"))
                )
                user_menu.click()
                logger.info("成功点击右上角用户菜单")
                time.sleep(1)  # 等待菜单展开
        except Exception as e:
            logger.error(f"点击用户菜单失败: {str(e)}")
            allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            raise

    def do_report_statistics(self):
        """执行报表统计功能"""
        with allure.step("测试报表统计功能"):
            try:
                # 点击右上角菜单
                self.click_user_menu()

                with allure.step("点击报表统计选项"):
                    report_option = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'报表统计')]"))
                    )
                    report_option.click()
                    logger.info("点击报表统计选项")
                    time.sleep(1)

                with allure.step("点击承办部门"):
                    department = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[@title='按承办部门']"))
                    )
                    department.click()
                    logger.info("点击承办部门")
                    time.sleep(1)

                with allure.step("选择承办人"):
                    handler = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'按承办人')]"))
                    )
                    handler.click()
                    logger.info("选择承办人")
                    time.sleep(1)

                with allure.step("点击查询按钮"):
                    query_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//body//div//button[1]"))
                    )
                    query_button.click()
                    logger.info("点击查询按钮")
                    time.sleep(2)  # 等待查询结果

                with allure.step("点击导出按钮"):
                    export_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//body//div//button[3]"))
                    )
                    export_button.click()
                    logger.info("点击导出按钮")
                    time.sleep(3)  # 等待导出完成

            except Exception as e:
                logger.error(f"报表统计测试失败: {str(e)}")
                allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
                raise

    def do_font_download(self):
        """执行字体下载功能"""
        with allure.step("测试字体下载功能"):
            try:
                # 点击右上角菜单
                self.click_user_menu()

                with allure.step("点击字体下载选项"):
                    font_option = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'字体下载')]"))
                    )
                    font_option.click()
                    logger.info("点击字体下载选项")
                    time.sleep(1)

                with allure.step("点击方正小标简体按钮"):
                    fangzheng_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-modal-body']//button[2]"))
                    )
                    fangzheng_button.click()
                    logger.info("点击方正小标简体按钮")
                    time.sleep(2)  # 等待下载开始

                with allure.step("点击关闭弹框"):
                    close_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[@class='ant-modal-close-x']"))
                    )
                    close_button.click()
                    logger.info("点击关闭弹框")
                    time.sleep(1)

            except Exception as e:
                logger.error(f"字体下载测试失败: {str(e)}")
                allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
                raise

    def do_change_password(self):
        """执行修改密码功能"""
        with allure.step("测试修改密码功能"):
            try:
                # 点击右上角菜单
                self.click_user_menu()

                with allure.step("点击修改密码选项"):
                    password_option = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'修改密码')]"))
                    )
                    password_option.click()
                    logger.info("点击修改密码选项")
                    time.sleep(1)

                with allure.step("输入原密码"):
                    old_password_input = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='请输入原密码']"))
                    )
                    old_password_input.send_keys("wxd341134@")
                    logger.info("输入原密码")

                with allure.step("输入新密码"):
                    new_password_input = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='请输入新密码']"))
                    )
                    new_password_input.send_keys("wxd341134@")
                    logger.info("输入新密码")

                with allure.step("确认新密码"):
                    confirm_new_password_input = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='请再次输入新密码']"))
                    )
                    confirm_new_password_input.send_keys("wxd341134@")
                    logger.info("确认新密码")

                with allure.step("点击确定按钮"):
                    confirm_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-modal-footer']//button[2]"))
                    )
                    confirm_button.click()
                    logger.info("点击确定按钮")
                    time.sleep(2)  # 等待系统处理

            except Exception as e:
                logger.error(f"修改密码测试失败: {str(e)}")
                allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
                raise

    def do_verify_new_password(self):
        """执行验证新密码登录功能"""
        with allure.step("验证新密码登录功能"):
            try:
                time.sleep(1)  # 等待1秒，确保登录页面出现

                with allure.step("使用新密码登录"):
                    # 使用LoginPage类的方法进行登录
                    self.login_page = LoginPage(self.driver)
                    self.login_page.login("wxdfg", "wxd341134@")
                    logger.info("完成新密码登录")
                    time.sleep(2)  # 等待登录完成

                with allure.step("验证登录成功"):
                    # 验证是否登录成功
                    user_menu = WebDriverWait(self.driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']"))
                    )
                    assert user_menu.is_displayed(), "使用新密码登录失败"
                    logger.info("使用新密码登录成功")

                    # 添加截图作为证据
                    allure.attach(self.driver.get_screenshot_as_png(), "登录成功截图", allure.attachment_type.PNG)

            except Exception as e:
                logger.error(f"验证新密码登录失败: {str(e)}")
                allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
                raise


if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./allure-results", "test_UserCenter.py"])