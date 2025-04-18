import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.assisted_reading_page2 import AssistedReadingPage
from pages.login_page import LoginPage
import allure
from utils.logger2 import Logger
from common.driver_manager import DriverManager


logger = Logger().get_logger()


@allure.epic("FGAI自动化测试")
@allure.feature("辅助阅卷")
class TestAssistedReading:
    """辅助阅卷测试类"""

    def setup_class(self):
        """类级别的初始化"""
        logger.info("初始化测试类...")
        self.driver = DriverManager.get_driver()
        self.wait = WebDriverWait(self.driver, 10)
        self.login_page = LoginPage(self.driver)

        # 创建辅助阅卷页面对象
        self.assisted_page = AssistedReadingPage(self.driver)

    def teardown_class(self):
        """类级别的清理"""
        logger.info("测试类执行完成，进行清理...")
        try:
            if hasattr(self, 'driver'):
                DriverManager.quit_driver()
                logger.info("浏览器已关闭")
        except Exception as e:
            logger.error(f"关闭浏览器时出错: {str(e)}")

    @allure.story("辅助阅卷流程")
    @allure.title("辅助阅卷测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_assisted_reading(self):
        """测试辅助阅卷流程"""
        try:
            # 1. 登录系统
            with allure.step("登录系统"):
                logger.info("开始登录系统")
                self.login_page.login()
                time.sleep(3)  # 增加登录后的等待时间
                logger.info("登录成功")
                self.take_screenshot("login_success")

            # 2. 点击辅助阅卷
            with allure.step("点击辅助阅卷"):
                self.assisted_page.click_auxiliary_reading()
                self.take_screenshot("auxiliary_reading_clicked")

            # 3. 点击庭审笔录1
            with allure.step("点击庭审笔录1"):
                self.assisted_page.click_court_record1()
                self.take_screenshot("court_record1_clicked")

            # 4. 设为庭审笔录和输入处理意见
            with allure.step("设为庭审笔录并输入处理意见"):
                (self.assisted_page
                 .set_as_court_record()
                 .enter_opinions("无意见1", "无意见2")
                 .confirm_settings())
                self.take_screenshot("set_court_record_complete")

            # 5. 取消设置庭审笔录
            with allure.step("取消设置庭审笔录"):
                self.assisted_page.cancel_set_record()
                self.take_screenshot("cancel_set_record_complete")

            # 6. 下载PDF
            with allure.step("下载笔录PDF"):
                self.assisted_page.download_pdf()
                self.take_screenshot("pdf_download_complete")

            # 7. 添加庭审笔录2为证据
            with allure.step("添加庭审笔录2为证据"):
                self.assisted_page.add_court_record2_as_evidence()
                self.take_screenshot("add_evidence_complete")

            # 8. 将庭审笔录3添加为证据
            with allure.step("将庭审笔录3添加为证据"):
                self.assisted_page.add_court_record3_as_evidence()
                self.take_screenshot("add_record3_evidence_complete")

            # 9. 证据引用功能
            with allure.step("证据引用功能"):
                self.assisted_page.check_evidence_reference()
                self.take_screenshot("evidence_reference_complete")

            # 10. 双屏阅卷功能
            with allure.step("双屏阅卷功能"):
                self.assisted_page.perform_dual_screen_reading()
                self.take_screenshot("dual_screen_reading_complete")

            # 11. 选择上诉人为第三人
            with allure.step("选择上诉人为第三人"):
                self.assisted_page.select_third_party()
                self.take_screenshot("select_third_party_complete")

            # 12. 刷新并取消选中庭审笔录3
            with allure.step("刷新并取消选中庭审笔录3"):
                self.assisted_page.refresh_and_uncheck_record3()
                self.take_screenshot("refresh_uncheck_record3_complete")

            # 13. 批量修改功能
            with allure.step("批量修改功能"):
                self.assisted_page.perform_batch_edit()
                self.take_screenshot("batch_edit_complete")

            logger.info("辅助阅卷测试完成")

        except Exception as e:
            logger.error(f"辅助阅卷测试失败: {str(e)}")
            self.take_screenshot("test_failed")
            raise

    def take_screenshot(self, name):
        """截图并添加到Allure报告"""
        try:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
        except:
            logger.warning(f"无法获取{name}截图")








