import os
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
import allure
from utils.logger2 import Logger
from common.driver_manager import DriverManager

logger = Logger().get_logger()


@allure.epic("FGAI自动化测试")
@allure.feature("卷宗管理")
class TestDossierUpload:
    """卷宗上传测试类"""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.login_page = LoginPage(driver)

        # 测试文件路径
        self.test_data_dir = os.path.join(os.getcwd(), "test_data")

        # 确保test_data目录存在
        if not os.path.exists(self.test_data_dir):
            logger.warning(f"test_data目录不存在，创建目录: {self.test_data_dir}")
            os.makedirs(self.test_data_dir)

        # 查找ZIP文件
        self.zip_file_path = None
        for file in os.listdir(self.test_data_dir):
            if file.endswith('.zip'):
                self.zip_file_path = os.path.join(self.test_data_dir, file)
                logger.info(f"找到ZIP文件: {file}")
                break

        if not self.zip_file_path:
            logger.warning("未在test_data目录中找到ZIP文件")

        # 查找单个文件(DOCX)
        self.docx_file_path = None
        for file in os.listdir(self.test_data_dir):
            if file.endswith('.docx'):
                self.docx_file_path = os.path.join(self.test_data_dir, file)
                logger.info(f"找到DOCX文件: {file}")
                break

        if not self.docx_file_path:
            logger.warning("未在test_data目录中找到DOCX文件")

        yield  # 添加 yield 使其成为 setup/teardown fixture

        # 确保测试结束后关闭浏览器
        try:
            logger.info("测试结束，关闭浏览器")
            DriverManager.quit_driver()
        except Exception as e:
            logger.error(f"关闭浏览器时出错: {str(e)}")

    @allure.story("卷宗上传")
    @allure.title("卷宗上传流程测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dossier_upload(self):
        """测试卷宗上传流程"""
        try:
            # 1. 登录系统
            with allure.step("登录系统"):
                logger.info("开始登录系统")
                self.login_page.login()
                time.sleep(2)
                logger.info("登录成功")
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name="login_success",
                    attachment_type=allure.attachment_type.PNG
                )

            # 2. 点击上传卷宗按钮
            with allure.step("点击上传卷宗按钮"):
                logger.info("点击上传卷宗按钮")
                upload_button = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH,
                     "//td[@title='(2025)苏0105民初0001号'][1]/ancestor::div[contains(@class, 'ant-table-content')]/div[3]/div[2]/div/table/tbody/tr[2]/td[3]/div/div[1]")
                ))
                upload_button.click()
                time.sleep(2)
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name="upload_button_clicked",
                    attachment_type=allure.attachment_type.PNG
                )

            # 3. 点击上传zip按钮并上传文件
            with allure.step("上传ZIP文件"):
                logger.info("点击上传zip按钮")
                upload_zip_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='tree-button-group ant-btn-group']//button[2]"))
                )
                upload_zip_button.click()
                time.sleep(1)

                if self.zip_file_path and os.path.exists(self.zip_file_path):
                    logger.info(f"上传ZIP文件: {self.zip_file_path}")
                    file_input = self.wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "input[type='file']")
                    ))
                    file_input.send_keys(self.zip_file_path)
                    logger.info("ZIP文件已选择")
                    time.sleep(2)

                    confirm_button = self.wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//div[@class='ant-modal-root']//button[2]")
                    ))
                    confirm_button.click()
                    time.sleep(5)
                    allure.attach(
                        self.driver.get_screenshot_as_png(),
                        name="zip_upload_complete",
                        attachment_type=allure.attachment_type.PNG
                    )
                else:
                    logger.warning("未找到可用的ZIP文件，跳过ZIP上传步骤")
                    allure.attach(
                        "未找到可用的ZIP文件",
                        name="zip_file_missing",
                        attachment_type=allure.attachment_type.TEXT
                    )

            # 4. 点击上传单个文件按钮并上传
            with allure.step("上传单个文件"):
                logger.info("点击上传单个文件按钮")
                upload_single_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH,
                                                "//div[@class='custom-modal ant-modal-root custom-modal j-modal-box fullscreen custom-modal j-modal-box fullscreen']//button[3]"))
                )
                upload_single_button.click()
                time.sleep(1)

                if self.docx_file_path and os.path.exists(self.docx_file_path):
                    logger.info(f"上传单个文件: {self.docx_file_path}")
                    file_input2 = self.wait.until(EC.presence_of_element_located(
                        (By.XPATH, "//input[@type='file' and contains(@accept, '.docx')]")
                    ))
                    file_input2.send_keys(self.docx_file_path)
                    logger.info("单个文件已选择")
                    time.sleep(2)

                    confirm_button2 = self.wait.until(EC.element_to_be_clickable(
                        (By.XPATH,
                         "//div[.//div[@class='ant-modal-title' and text()='上传单个文件']]//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']")
                    ))
                    confirm_button2.click()
                    time.sleep(2)
                    allure.attach(
                        self.driver.get_screenshot_as_png(),
                        name="single_file_upload_complete",
                        attachment_type=allure.attachment_type.PNG
                    )
                else:
                    logger.warning("未找到可用的DOCX文件，跳过单个文件上传步骤")
                    allure.attach(
                        "未找到可用的DOCX文件",
                        name="docx_file_missing",
                        attachment_type=allure.attachment_type.TEXT
                    )

            # 5. 刷新和展开文件列表
            with allure.step("刷新和展开文件列表"):
                logger.info("点击刷新按钮")
                refresh_button = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='tree-button-group ant-btn-group']//button[1]")
                ))
                refresh_button.click()
                time.sleep(1)

                logger.info("点击展开按钮")
                try:
                    expand_button = self.wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//button[@ant-click-animating-without-extra-node='true']")
                    ))
                    expand_button.click()
                    time.sleep(1)
                except:
                    logger.warning("未找到展开按钮或按钮点击失败")

                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name="file_list_expanded",
                    attachment_type=allure.attachment_type.PNG
                )

            # 6. 关闭上传窗口
            with allure.step("关闭上传窗口"):
                logger.info("点击关闭按钮")
                close_button = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='ant-modal-footer']//button[2]")
                ))
                close_button.click()
                time.sleep(2)
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name="upload_window_closed",
                    attachment_type=allure.attachment_type.PNG
                )

            logger.info("卷宗上传测试完成")

        except Exception as e:
            logger.error(f"卷宗上传测试失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="test_failed",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                str(e),
                name="error_message",
                attachment_type=allure.attachment_type.TEXT
            )
            raise

        finally:
            # 确保在测试结束后关闭浏览器
            try:
                logger.info("测试结束，关闭浏览器")
                DriverManager.quit_driver()
            except Exception as e:
                logger.error(f"关闭浏览器时出错: {str(e)}")

    @allure.step("验证元素是否存在")
    def verify_element_exists(self, locator, timeout=10):
        """验证元素是否存在"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False

    @allure.step("验证元素是否可点击")
    def verify_element_clickable(self, locator, timeout=10):
        """验证元素是否可点击"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except:
            return False

    @pytest.fixture(autouse=True)
    def teardown_method(self):
        """每个测试方法结束后的清理工作"""
        yield
        try:
            logger.info("测试方法结束，确保浏览器已关闭")
            DriverManager.quit_driver()
        except Exception as e:
            logger.error(f"清理过程中关闭浏览器出错: {str(e)}")
