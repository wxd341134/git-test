import time
import pytest
import allure
from datetime import datetime
from tests.base_test import BaseTest
from pages.assisted_read_page import AssistedReadPage
from common.assisted_read_utils import AssistedReadUtils
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("辅助阅卷")
@allure.feature("辅助阅卷")
class TestAssistedReading(BaseTest):
    """辅助阅卷测试类"""

    @pytest.fixture(autouse=True)
    def setup_TestAssistedRead(self, driver):
        """
        测试前后处理
        前置：初始化TestAssistedRead对象
        后置：记录日志
        """
        logger.info("开始测试前置操作...")
        try:
            # 初始化工具类
            self.TestAssistedRead_utils = AssistedReadUtils(driver)
            yield
            logger.info("测试后置操作完成")
        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "设置或清理失败截图",
                allure.attachment_type.PNG
            )
            raise


    @allure.story("辅助阅卷流程")
    @allure.title("辅助阅卷完整流程测试")
    @allure.description("""
    测试步骤：
    1. 点击辅助阅卷
    2. 点击并处理庭审笔录2
    3. 设置和取消设置庭审笔录
    4. 下载PDF文件
    5. 添加庭审笔录2和3为证据
    6. 测试证据引用功能
    7. 测试双屏阅卷功能
    8. 选择上诉人为第三人
    9. 执行批量修改功能
    """)
    def test_assisted_reading(self):
        """测试辅助阅卷流程"""
        try:
            # 1. 点击辅助阅卷
            with allure.step("点击辅助阅卷"):
                logger.info("步骤1: 点击辅助阅卷按钮")
                assert AssistedReadUtils.click_auxiliary_reading(self.TestAssistedRead_utils)


            # 2. 点击庭审笔录1
            with allure.step("点击并处理庭审笔录2"):
                logger.info("步骤2: 点击庭审笔录2")
                assert AssistedReadUtils.click_court_record1(self.TestAssistedRead_utils)


            # 3. 设为庭审笔录和输入处理意见
            with allure.step("设置庭审笔录并输入处理意见"):
                logger.info("步骤3: 设置庭审笔录并输入处理意见")
                assert AssistedReadUtils.set_as_court_record(self.TestAssistedRead_utils)
                assert AssistedReadUtils.enter_opinions(self.TestAssistedRead_utils, "无意见1", "无意见2")
                assert AssistedReadUtils.confirm_settings(self.TestAssistedRead_utils)


            # 4. 取消设置庭审笔录
            with allure.step("取消设置庭审笔录"):
                logger.info("步骤4: 取消设置庭审笔录")
                assert AssistedReadUtils.cancel_set_record(self.TestAssistedRead_utils)


            # 5. 下载PDF
            with allure.step("下载笔录PDF"):
                logger.info("步骤5: 下载笔录PDF")
                assert AssistedReadUtils.download_pdf(self.TestAssistedRead_utils)


            # 6. 添加庭审笔录2为证据
            with allure.step("添加庭审笔录2为证据"):
                logger.info("步骤6: 添加庭审笔录2为证据")
                assert AssistedReadUtils.add_court_record2_as_evidence(self.TestAssistedRead_utils)


            # 7. 将庭审笔录3添加为证据
            with allure.step("将庭审笔录3添加为证据"):
                logger.info("步骤7: 添加庭审笔录3为证据")
                assert AssistedReadUtils.add_court_record3_as_evidence(self.TestAssistedRead_utils)


            # 8. 证据引用功能
            with allure.step("测试证据引用功能"):
                logger.info("步骤8: 测试证据引用功能")
                assert AssistedReadUtils.check_evidence_reference(self.TestAssistedRead_utils)


            # 9. 双屏阅卷功能
            with allure.step("测试双屏阅卷功能"):
                logger.info("步骤9: 测试双屏阅卷功能")
                assert AssistedReadUtils.perform_dual_screen_reading(self.TestAssistedRead_utils)


            # 10. 选择上诉人为第三人
            with allure.step("选择上诉人为第三人"):
                logger.info("步骤10: 选择上诉人为第三人")
                assert AssistedReadUtils.select_third_party(self.TestAssistedRead_utils)


            # 11. 刷新并取消选中庭审笔录3
            with allure.step("刷新并取消选中庭审笔录3"):
                logger.info("步骤11: 刷新并取消选中庭审笔录3")
                assert AssistedReadUtils.refresh_and_uncheck_record3(self.TestAssistedRead_utils)


            # 12. 批量修改功能
            with allure.step("执行批量修改功能"):
                logger.info("步骤12: 执行批量修改功能")
                assert AssistedReadUtils.perform_batch_edit(self.TestAssistedRead_utils)


            logger.info("辅助阅卷测试用例执行完成")

        except Exception as e:
            logger.error(f"辅助阅卷测试失败: {str(e)}")
            allure.attach(
                str(e),
                name="error_message",
                attachment_type=allure.attachment_type.TEXT
            )
            raise




if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./reports/allure-results", __file__])