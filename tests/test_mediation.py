import time

import pytest
import allure
from common.Mediation_utils import MediationUtils
from tests.base_test import BaseTest
from utils.logger import logger


@allure.feature("调节模块")
class TestMediation(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_class(self, driver):
        """
        测试类级别的设置，在所有测试方法之前执行
        """
        logger.info("开始测试前置操作...")
        self.mediation_utils = MediationUtils(driver)
        yield
        # 测试结束后的清理操作

    @allure.story("调节功能")
    @allure.title("测试调节基本功能")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_mediation_basic(self, driver):
        """
        测试调节基本功能，包括：
        1. 打开调节界面
        2. 卷宗预览
        3. 保存和导出
        4. 查找替换功能
        """
        try:
            # 记录测试元数据
            current_time = "2025-06-27 03:30:34"
            current_user = "wxd341134"

            with allure.step(f"测试开始 - 时间: {current_time}, 用户: {current_user}"):
                logger.info(f"开始调节测试 - 执行时间: {current_time}")
                logger.info(f"执行用户: {current_user}")

            # 执行调节操作
            # with allure.step("1. 点击进入判决书"):
            #     logger.info("点击进入判决书")
            #     self.judgment_utils.enter_judgment()
            #     time.sleep(2)

            with allure.step("执行调节操作"):
                result = self.mediation_utils.perform_mediation_operations()
                assert result, "调节操作失败"

        except Exception as e:
            logger.error(f"调节测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "测试失败截图",
                allure.attachment_type.PNG
            )
            raise