import time
import pytest
import os
from pages.reading_notes_page import ReadingNotesPage
from pages.login_page import LoginPage
from utils.logger2 import Logger
from common.driver_manager import DriverManager

logger = Logger().get_logger()

class TestDocumentNotes:
    """阅卷笔记测试类"""

    @classmethod
    def setup_class(cls):
        """测试类初始化"""
        logger.info("========== 开始执行阅卷笔记测试 ==========")
        
        # 创建必要的目录结构
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # 创建下载目录
        cls.download_dir = os.path.join(base_dir, "downloads")
        if not os.path.exists(cls.download_dir):
            os.makedirs(cls.download_dir)
            logger.info(f"创建下载目录: {cls.download_dir}")

    @classmethod
    def teardown_class(cls):
        """测试类清理"""
        logger.info("========== 阅卷笔记测试执行完成 ==========")
        
        # 尝试关闭由驱动管理器创建的所有浏览器实例
        try:
            driver_manager = DriverManager()
            driver_manager.quit_all_drivers()
            logger.info("已关闭所有浏览器实例")
        except Exception as e:
            logger.warning(f"关闭浏览器实例时出错: {str(e)}")

    def setup_method(self, method):
        """每个测试方法的初始化"""
        logger.info(f"开始执行测试方法: {method.__name__}")

        # 获取driver实例
        driver_manager = DriverManager()
        self.driver = driver_manager.get_driver()
        self.driver.maximize_window()

        # 创建页面对象
        self.reading_notes_page = ReadingNotesPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def teardown_method(self, method):
        """每个测试方法结束后的清理"""
        logger.info(f"测试方法执行完成: {method.__name__}")

    def test_document_notes(self):
        """测试阅卷笔记功能"""
        try:
            logger.info("开始阅卷笔记测试")

            # 1. 登录系统
            try:
                logger.info("开始登录系统")
                self.login_page.login()
                logger.info("登录系统完成")
            except Exception as e:
                logger.error(f"登录失败: {str(e)}")
                self.reading_notes_page.take_screenshot("login_failed")
                pytest.fail("登录系统失败")

            # 2. 执行阅卷笔记工作流程
            if not self.reading_notes_page.execute_reading_notes_workflow(self.download_dir):
                pytest.fail("阅卷笔记工作流程执行失败")

            # 3. 测试成功完成时保存截图
            self.reading_notes_page.take_screenshot("test_complete")
            logger.info("阅卷笔记功能测试完成")

        except Exception as e:
            logger.error(f"阅卷笔记测试过程中出现错误: {str(e)}")
            self.reading_notes_page.take_screenshot("test_error")
            raise

        finally:
            logger.info("阅卷笔记测试结束")

            # 在测试方法结束时关闭浏览器
            try:
                logger.info("正在关闭浏览器...")
                self.driver.quit()
                logger.info("浏览器已关闭")
            except Exception as e:
                logger.warning(f"关闭浏览器时出错: {str(e)}")


if __name__ == "__main__":
    # 单独运行此测试时使用
    pytest.main(["-v", __file__])
