import os

import pytest
import allure
from common.case_utils import CaseUtils
from tests.base_test import BaseTest
from utils.common import get_project_root, load_json_data
from utils.logger import Logger

logger = Logger().get_logger()
class TestDataManager:
    """测试数据管理类"""

    @staticmethod
    def get_test_data():
        """获取测试数据"""
        try:
            data_file = os.path.join(get_project_root(), 'test_data', 'case_data.json')
            logger.info(f"尝试加载测试数据文件: {data_file}")

            if not os.path.exists(data_file):
                TestDataManager._create_default_test_data(data_file)

            test_data = load_json_data(data_file)
            logger.info("测试数据加载成功")
            return test_data

        except Exception as e:
            logger.error(f"加载测试数据失败: {e}")
            return TestDataManager._get_default_data()

@allure.epic("案件管理系统")
@allure.feature("案件管理")
class TestCaseManagement(BaseTest):
    """案件管理测试类"""

    @pytest.fixture(autouse=True)
    def setup_case(self, driver):
        """
        测试前后处理
        前置：初始化CaseUtils对象，加载测试数据
        后置：记录日志
        """
        logger.info("开始测试前置操作...")
        try:
            # 初始化工具类
            self.case_utils = CaseUtils(driver)
            # 加载测试数据
            self.test_data = TestDataManager.get_test_data()
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

    @allure.story("案件基本操作")
    @allure.title("案件增删改功能测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_crud(self, driver):
        """
        测试案件的基本操作
        步骤：
        1. 添加新案件
        2. 编辑案件信息
        3. 删除案件
        """
        try:
            # 获取测试数据
            case_data = self.test_data["test_cases"][0]
            case_name = case_data["case_name"]
            case_number = case_data["case_number"]

            with allure.step(f"测试开始 - 案件名称: {case_name}"):
                logger.info(f"开始案件操作测试 - 案件: {case_name}")

            # 添加案件
            with allure.step(f"添加案件: {case_name}"):
                assert self.case_utils.add_case(case_name, case_number), "添加案件失败"

            # # 编辑案件
            with allure.step(f"编辑案件: {case_name}"):
                assert self.case_utils.edit_case(case_name), "编辑案件失败"

            # 删除案件
            with allure.step(f"删除案件: {case_number}"):
                assert self.case_utils.delete_case(case_number), "删除案件失败"

            logger.info("案件操作测试完成")

        except AssertionError as ae:
            logger.error(f"断言失败: {str(ae)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "断言失败截图",
                allure.attachment_type.PNG
            )
            raise
        except Exception as e:
            logger.error(f"测试执行失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "测试失败截图",
                allure.attachment_type.PNG
            )
            allure.attach(
                str(e),
                "错误信息",
                allure.attachment_type.TEXT
            )
            raise


if __name__ == "__main__":
    pytest.main([
        "-v",
        "--alluredir=./reports/allure-results",
        __file__
    ])