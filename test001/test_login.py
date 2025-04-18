import pytest
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test001.login import initialize_driver, login
from utils.logger import Logger

logger = Logger().get_logger()


@allure.feature("登录功能")
class TestLogin:
    """登录功能测试类"""

    def setup_class(self):
        """测试类级别初始化"""
        logger.info("开始登录功能测试...")
        self.driver = None
        self.wait = None

    def teardown_class(self):
        """测试类级别清理"""
        logger.info("登录功能测试完成")
        if self.driver:
            self.driver.quit()

    @allure.story("登录测试")
    @pytest.mark.parametrize("username,password,expected_result", [
        ("wxdfg", "wxd341134@", True),  # 有效账号密码
        ("invalid", "invalid123", False),  # 无效账号密码
        ("", "", False),  # 空账号密码
    ])
    def test_login(self, username, password, expected_result):
        """测试不同的登录场景"""
        try:
            with allure.step("初始化浏览器"):
                self.driver = initialize_driver()
                assert self.driver is not None, "浏览器初始化失败"

            with allure.step(f"测试登录场景 - 用户名: {username}"):
                self.driver, self.wait = login(self.driver, username, password)

                if expected_result:
                    # 验证登录成功
                    with allure.step("验证登录成功"):
                        user_menu = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.XPATH,
                                                            "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']"))
                        )
                        assert user_menu.is_displayed(), "登录后未找到用户菜单"

                        # 获取并验证当前登录用户信息
                        current_user = user_menu.text
                        assert username in current_user, f"当前登录用户 {current_user} 与期望用户 {username} 不匹配"

                        # 记录登录成功的时间
                        login_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
                        allure.attach(
                            f"Login Time (UTC): {login_time}\nUsername: {username}",
                            "Login Information",
                            allure.attachment_type.TEXT
                        )
                else:
                    # 验证登录失败
                    with allure.step("验证登录失败"):
                        error_message = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-message-error')]"))
                        )
                        assert error_message.is_displayed(), "未显示错误消息"

        except Exception as e:
            logger.error(f"登录测试失败: {str(e)}")
            if self.driver:
                # 截图并附加到报告
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "登录失败截图",
                    allure.attachment_type.PNG
                )
            raise
        finally:
            if self.driver:
                self.driver.quit()
                self.driver = None

    @allure.story("验证码功能")
    def test_captcha_visibility(self):
        """测试验证码是否正确显示"""
        try:
            with allure.step("初始化浏览器并访问登录页面"):
                self.driver = initialize_driver()
                self.driver.get("http://192.168.2.176:86/#/case/index")

            with allure.step("验证验证码图片是否显示"):
                captcha_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//img[contains(@src, "/judge-ai/captcha")]'))
                )
                assert captcha_element.is_displayed(), "验证码图片未显示"

                # 截取验证码图片
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "验证码显示截图",
                    allure.attachment_type.PNG
                )

        except Exception as e:
            logger.error(f"验证码测试失败: {str(e)}")
            if self.driver:
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "测试失败截图",
                    allure.attachment_type.PNG
                )
            raise
        finally:
            if self.driver:
                self.driver.quit()
                self.driver = None

    @allure.story("登录界面元素")
    def test_login_page_elements(self):
        """测试登录页面基本元素"""
        try:
            with allure.step("初始化浏览器并访问登录页面"):
                self.driver = initialize_driver()
                self.driver.get("http://192.168.2.176:86/#/case/index")

            elements_to_check = {
                "用户名输入框": "//input[@placeholder='请输入账号']",
                "密码输入框": "//input[@placeholder='请输入密码']",
                "验证码输入框": "//input[@placeholder='请输入验证码']",
                "登录按钮": "//button[@type='button']"
            }

            for element_name, xpath in elements_to_check.items():
                with allure.step(f"检查{element_name}是否存在"):
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    assert element.is_displayed(), f"{element_name}未正确显示"

            # 截图记录页面状态
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "登录页面元素验证截图",
                allure.attachment_type.PNG
            )

        except Exception as e:
            logger.error(f"登录页面元素测试失败: {str(e)}")
            if self.driver:
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "测试失败截图",
                    allure.attachment_type.PNG
                )
            raise
        finally:
            if self.driver:
                self.driver.quit()
                self.driver = None


if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./allure-results", "test_login.py"])