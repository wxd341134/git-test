import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.search_annotations_page import SearchAnnotationsPage
from utils.logger import Logger

logger = Logger().get_logger()


class SearchAnnotationsUtils:
    """检索批注工具类"""

    def __init__(self, driver):
        """
        初始化
        Args:
            driver: WebDriver实例
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    @allure.step("选中文本: {text}")
    def select_text(self, text):
        """
        选中指定文本
        Args:
            text: 要选中的文本
        """
        try:
            logger.info(f"尝试选中文本: {text}")
            # 使用新的查找元素方法
            elements = self.driver.find_elements(
                By.XPATH,
                f"//*[contains(text(), '{text}')]"
            )

            if elements:
                element = elements[0]
                # 确保元素可见
                self.wait.until(
                    EC.visibility_of(element)
                )

                # 滚动到元素位置
                self.driver.execute_script(
                    "arguments[0].scrollIntoView(true);",
                    element
                )
                time.sleep(0.5)  # 等待滚动完成

                # 移动到元素并双击选中文本
                self.actions.move_to_element(element).double_click().perform()
                time.sleep(1)  # 等待选中效果

                logger.info(f"成功选中文本: {text}")
            else:
                error_msg = f"未找到包含文本 '{text}' 的元素"
                logger.error(error_msg)
                raise Exception(error_msg)

        except Exception as e:
            logger.error(f"选中文本失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "选中文本失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("点击元素: {element_name}")
    def click_element(self, locator, element_name):
        """点击元素的通用方法"""
        try:
            logger.info(f"尝试点击元素: {element_name}")
            element = self.wait.until(EC.element_to_be_clickable(locator))

            # 滚动到元素位置
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);",
                element
            )
            time.sleep(0.5)  # 等待滚动完成

            # 确保元素可点击
            element.click()
            logger.info(f"成功点击元素: {element_name}")

        except Exception as e:
            logger.error(f"点击元素失败 {element_name}: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                f"点击{element_name}失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("输入文本: {text}")
    def input_text(self, locator, text, element_name):
        """输入文本的通用方法"""
        try:
            logger.info(f"尝试在{element_name}中输入文本: {text}")
            element = self.wait.until(EC.presence_of_element_located(locator))

            # 确保元素可见和可交互
            self.wait.until(EC.visibility_of(element))
            element.clear()
            time.sleep(0.5)  # 等待清除完成

            element.send_keys(text)
            logger.info(f"成功输入文本: {text}")

        except Exception as e:
            logger.error(f"输入文本失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "输入文本失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("执行检索批注")
    def add_annotation(self, text_to_select="如下文档", annotation_text="123456"):
        """
        执行完整的检索批注流程
        Args:
            text_to_select: 要选中的文本
            annotation_text: 批注内容
        """
        try:
            # 1. 点击辅助阅卷
            with allure.step("点击辅助阅卷"):
                self.click_element(
                    SearchAnnotationsPage.ASSIST_READ_BUTTON,
                    "辅助阅卷按钮"
                )
                time.sleep(1)  # 等待页面响应

            # 2. 点击AI助手安装文档
            with allure.step("点击AI助手安装文档"):
                self.click_element(
                    SearchAnnotationsPage.AI_ASSISTANT_DOC,
                    "AI助手安装文档"
                )
                time.sleep(2)  # 等待文档加载

            # 3. 选中文本
            with allure.step(f"选中文本: {text_to_select}"):
                self.select_text(text_to_select)
                time.sleep(1)  # 等待选中效果

            # 4. 点击批注按钮
            with allure.step("点击批注按钮"):
                self.click_element(
                    SearchAnnotationsPage.ANNOTATION_BUTTON,
                    "批注按钮"
                )

            # 5. 输入批注内容
            with allure.step("输入批注内容"):
                self.input_text(
                    SearchAnnotationsPage.ANNOTATION_INPUT,
                    annotation_text,
                    "批注输入框"
                )

            # 6. 点击标签下拉框
            with allure.step("点击标签下拉框"):
                self.click_element(
                    SearchAnnotationsPage.LABEL_DROPDOWN,
                    "标签下拉框"
                )
                time.sleep(0.5)  # 等待下拉框展开

            # 7. 选择证据标签
            with allure.step("选择证据标签"):
                self.click_element(
                    SearchAnnotationsPage.EVIDENCE_LABEL,
                    "证据标签"
                )

            # 8. 保存批注
            with allure.step("保存批注"):
                self.click_element(
                    SearchAnnotationsPage.SAVE_BUTTON,
                    "保存按钮"
                )
                time.sleep(1)  # 等待保存完成

            logger.info("检索批注流程执行完成")

        except Exception as e:
            logger.error(f"检索批注流程失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "检索批注失败截图",
                allure.attachment_type.PNG
            )
            raise
