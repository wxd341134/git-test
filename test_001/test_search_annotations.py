import allure
import pytest
from common.search_annotations_utils import SearchAnnotationsUtils
from test_001.base_test import BaseTest
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("案件管理系统")
@allure.feature("检索批注功能")
class TestSearchAnnotations(BaseTest):
    """检索批注测试类"""

    def setup_method(self):
        """方法级别的初始化"""
        self.annotations = SearchAnnotationsUtils(self.driver)

    @allure.story("基础批注功能")
    @allure.title("测试添加批注")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_annotation(self):
        """测试添加批注的基本功能"""
        try:
            with allure.step("执行基本批注流程"):
                self.annotations.add_annotation()

                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "批注添加完成",
                    allure.attachment_type.PNG
                )

        except Exception as e:
            logger.error(f"添加批注测试失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise


if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./allure-results"])