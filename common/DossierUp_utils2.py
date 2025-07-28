import os
import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.common import get_project_root
from utils.logger import Logger
from pages.DossierUp_page2 import DossierUpPage

logger = Logger().get_logger()


class DossierUpUtils:
    """卷宗上传工具类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator, element_name):
        """点击元素的通用方法"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"点击 {element_name} 成功")
            time.sleep(1)
            return True
        except Exception as e:
            logger.error(f"点击 {element_name} 失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                f"{element_name}点击失败截图",
                allure.attachment_type.PNG
            )
            return False

    def click_upload_button(self):
        """点击上传卷宗按钮"""
        return self.click_element(DossierUpPage.UPLOAD_BUTTON, "上传卷宗按钮")

    def upload_zip_file(self, file_path):
        """上传ZIP文件"""
        try:
            # 点击上传zip按钮
            if not self.click_element(DossierUpPage.UPLOAD_ZIP_BUTTON, "上传ZIP按钮"):
                return False

            # 上传文件
            file_input = self.wait.until(EC.presence_of_element_located(DossierUpPage.FILE_INPUT))
            file_input.send_keys(file_path)
            logger.info(f"选择ZIP文件: {file_path}")
            time.sleep(2)

            # 确认上传
            if not self.click_element(DossierUpPage.ZIP_CONFIRM_BUTTON, "确认上传按钮"):
                return False

            time.sleep(5)
            return True
        except Exception as e:
            logger.error(f"上传ZIP文件失败: {str(e)}")
            return False

    def upload_single_file(self, file_path):
        """上传单个文件"""
        try:
            # 点击上传单个文件按钮
            if not self.click_element(DossierUpPage.UPLOAD_SINGLE_BUTTON, "上传单个文件按钮"):
                return False

            # 上传文件
            file_input = self.wait.until(EC.presence_of_element_located(DossierUpPage.DOCX_FILE_INPUT))
            file_input.send_keys(file_path)
            logger.info(f"选择单个文件: {file_path}")
            time.sleep(2)

            # 确认上传
            if not self.click_element(DossierUpPage.SINGLE_FILE_CONFIRM_BUTTON, "确认上传按钮"):
                return False

            time.sleep(2)
            return True
        except Exception as e:
            logger.error(f"上传单个文件失败: {str(e)}")
            return False

    def refresh_and_expand_file_list(self):
        """刷新并展开文件列表"""
        try:
            # 点击刷新按钮
            if not self.click_element(DossierUpPage.REFRESH_BUTTON, "刷新按钮"):
                return False

            # 尝试点击展开按钮
            try:
                self.click_element(DossierUpPage.EXPAND_BUTTON, "展开按钮")
            except:
                logger.warning("未找到展开按钮或按钮点击失败")

            return True
        except Exception as e:
            logger.error(f"刷新并展开文件列表失败: {str(e)}")
            return False

    def close_upload_window(self):
        """关闭上传窗口"""
        return self.click_element(DossierUpPage.CLOSE_BUTTON, "关闭按钮")

    @staticmethod
    def check_test_files(test_data_dir):
        """检查测试文件"""
        try:
            # 确保test_data目录存在
            if not os.path.exists(test_data_dir):
                logger.warning(f"test_data目录不存在，创建目录: {test_data_dir}")
                os.makedirs(test_data_dir)

            # 查找ZIP文件和DOCX文件
            zip_file_path = next(
                (os.path.join(test_data_dir, f) for f in os.listdir(test_data_dir) if f.endswith('.zip')), None)
            docx_file_path = next(
                (os.path.join(test_data_dir, f) for f in os.listdir(test_data_dir) if f.endswith('.docx')), None)

            if zip_file_path:
                logger.info(f"找到ZIP文件: {os.path.basename(zip_file_path)}")
            if docx_file_path:
                logger.info(f"找到DOCX文件: {os.path.basename(docx_file_path)}")

            return zip_file_path, docx_file_path
        except Exception as e:
            logger.error(f"检查测试文件失败: {str(e)}")
            return None, None

    @allure.step("执行完整的卷宗上传流程")
    def execute_upload_workflow(self, test_data_dir):
        """执行完整的卷宗上传流程"""
        try:
            # 检查测试文件
            zip_file_path, docx_file_path = self.check_test_files(test_data_dir)

            # 执行上传流程
            with allure.step("点击上传卷宗按钮"):
                if not self.click_upload_button():
                    raise Exception("点击上传卷宗按钮失败")

            with allure.step("上传ZIP文件"):
                if zip_file_path:
                    if not self.upload_zip_file(zip_file_path):
                        raise Exception("ZIP文件上传失败")

            with allure.step("上传单个文件"):
                if docx_file_path:
                    if not self.upload_single_file(docx_file_path):
                        raise Exception("单个文件上传失败")

            with allure.step("刷新并展开文件列表"):
                if not self.refresh_and_expand_file_list():
                    raise Exception("刷新并展开文件列表失败")

            with allure.step("关闭上传窗口"):
                if not self.close_upload_window():
                    raise Exception("关闭上传窗口失败")

            logger.info("卷宗上传流程执行完成")
            return True

        except Exception as e:
            logger.error(f"卷宗上传流程执行失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "上传流程失败截图",
                allure.attachment_type.PNG
            )
            return False