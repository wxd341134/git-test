import time
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementNotInteractableException,
    NoSuchElementException
)

logger = logging.getLogger(__name__)


class TextSelection2:
    """文本选择工具类 - 使用ActionChains模拟鼠标操作"""

    def find_text_element(self, text_to_find, container_xpath="//body"):
        """
        查找包含指定文本的元素
        Args:
            text_to_find: 要查找的文本
            container_xpath: 搜索范围的xpath，默认为整个body
        Returns:
            tuple: (元素, 文本起始位置, 文本内容)
        """
        try:
            # 使用XPath查找包含目标文本的元素
            xpath = f"{container_xpath}//*[contains(text(), '{text_to_find}')]"
            elements = self.driver.find_elements(By.XPATH, xpath)

            for element in elements:
                element_text = element.text
                if text_to_find in element_text:
                    text_start_pos = element_text.index(text_to_find)
                    return element, text_start_pos, element_text

            raise NoSuchElementException(f"未找到包含文本 '{text_to_find}' 的元素")

        except Exception as e:
            logger.error(f"查找文本元素失败: {str(e)}")
            raise

    def get_text_coordinates(self, element, text_to_select, start_pos):
        """
        获取文本的坐标信息
        Args:
            element: 包含文本的元素
            text_to_select: 要选择的文本
            start_pos: 文本在元素内容中的起始位置
        Returns:
            tuple: (起始x坐标, 起始y坐标, 结束x坐标, 结束y坐标)
        """
        try:
            # 获取元素的位置和大小
            location = element.location
            size = element.size

            # 计算文本的起始和结束坐标
            # 这里使用简单的线性插值来估算文本位置
            text_width = len(text_to_select) * (size['width'] / len(element.text))

            start_x = location['x'] + (start_pos * size['width'] / len(element.text))
            start_y = location['y'] + (size['height'] / 2)
            end_x = start_x + text_width
            end_y = start_y

            return start_x, start_y, end_x, end_y

        except Exception as e:
            logger.error(f"获取文本坐标失败: {str(e)}")
            raise

    def drag_select_text(self, text_to_select, container_xpath="//body"):
        """
        通过鼠标拖动选择文本
        Args:
            text_to_select: 要选择的文本
            container_xpath: 搜索范围的xpath
        Returns:
            bool: 是否成功选择文本
        """
        try:
            logger.info(f"开始选择文本: {text_to_select}")

            # 查找包含文本的元素
            element, start_pos, element_text = self.find_text_element(
                text_to_select,
                container_xpath
            )

            # 确保元素可见
            self.wait.until(EC.visibility_of(element))
            element.location_once_scrolled_into_view
            time.sleep(0.5)

            # 获取文本坐标
            start_x, start_y, end_x, end_y = self.get_text_coordinates(
                element,
                text_to_select,
                start_pos
            )

            # 执行鼠标操作
            self.actions.move_to_element_with_offset(
                element,
                start_x - element.location['x'],
                start_y - element.location['y']
            )
            self.actions.click_and_hold()

            # 使用relative_by来移动到结束位置
            relative_move = end_x - start_x
            self.actions.move_by_offset(relative_move, 0)

            # 释放鼠标，完成选择
            self.actions.release()
            self.actions.perform()

            # 等待一小段时间确保选择完成
            time.sleep(0.5)

            logger.info("文本选择成功")
            return True

        except Exception as e:
            logger.error(f"文本选择失败: {str(e)}")
            raise

    def get_selected_text(self):
        """
        获取当前选中的文本
        Returns:
            str: 选中的文本内容
        """
        try:
            # 使用JavaScript获取选中的文本
            selected_text = self.driver.execute_script(
                "return window.getSelection().toString();"
            )
            return selected_text
        except Exception as e:
            logger.error(f"获取选中文本失败: {str(e)}")
            return ""

    def verify_selection(self, expected_text):
        """
        验证文本是否正确选中
        Args:
            expected_text: 期望选中的文本
        Returns:
            bool: 是否正确选中
        """
        try:
            selected_text = self.get_selected_text()
            is_correct = selected_text.strip() == expected_text.strip()
            if not is_correct:
                logger.warning(
                    f"文本选择验证失败，期望: {expected_text}, 实际: {selected_text}"
                )
            return is_correct
        except Exception as e:
            logger.error(f"验证文本选择失败: {str(e)}")
            return False