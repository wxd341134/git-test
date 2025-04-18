import allure
import pytest
from common.archives_search_utils import ArchivesSearchUtils
from test_001.base_test import BaseTest
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("案件管理系统")
@allure.feature("卷宗检索模块")
class TestArchivesSearch(BaseTest):
    """卷宗检索测试类"""

    @pytest.fixture(autouse=True)
    def setup_teardown(self, driver):
        """
        测试用例级别的设置和清理
        使用基类的driver fixture
        """
        logger.info("开始测试前置操作...")
        try:
            # 初始化卷宗检索工具类
            self.archives_search = ArchivesSearchUtils(driver)
            logger.info("卷宗检索工具类初始化完成")

            # 执行测试
            yield

            logger.info("测试后置操作完成")

        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "设置/清理失败截图",
                allure.attachment_type.PNG
            )
            raise

    def take_screenshot(self, name):
        """截图方法"""
        try:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name,
                allure.attachment_type.PNG
            )
        except Exception as e:
            logger.error(f"截图失败: {str(e)}")

    @allure.story("卷宗检索功能")
    @allure.title("测试卷宗检索基本流程")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_basic_archives_search(self, driver):
        """
        测试卷宗检索基本流程：
        1. 点击卷宗检索
        2. 输入搜索内容
        3. 点击搜索
        4. 预览卷宗
        5. 关闭预览
        6. 勾选仅显示文件名
        7. 关闭搜索
        """
        try:
            with allure.step("执行卷宗检索基本流程"):
                self.archives_search.perform_archives_search("判决")
                self.take_screenshot("基本流程完成")

        except Exception as e:
            logger.error(f"卷宗检索测试失败: {str(e)}")
            self.take_screenshot("基本流程失败")
            raise