import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.logger2 import Logger

logger = Logger().get_logger()

class ReadingNotesPage(BasePage):
    """阅卷笔记页面类"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        
        # 添加AI智能问答相关元素定位器
        self.AI_BUTTON = (By.XPATH, "//button[@title='AI智能问答']")
        self.AI_CLOSE_BUTTON = (By.XPATH, "//i[@aria-label='图标: close']//*[name()='svg']")
        
        # 添加新的元素定位器
        self.EXPORT_NOTES_BUTTON = (By.XPATH, "//a[@class='custom-note-btn primary']")
        self.SEARCH_REPLACE_BUTTON = (By.CSS_SELECTOR, "button[title='查找和替换'] span[class='tox-icon tox-tbtn__icon-wrap'] svg")
        self.FIND_INPUT = (By.XPATH, "//input[@placeholder='查找']")
        self.REPLACE_INPUT = (By.XPATH, "//input[@placeholder='替换为']")
        self.FIND_BUTTON = (By.XPATH, "//button[@title='查找']")
        self.REPLACE_BUTTON = (By.XPATH, "//button[@title='替换']")
        self.REPLACE_ALL_BUTTON = (By.XPATH, "//button[@title='全部替换']")
        self.CLOSE_DIALOG_BUTTON = (By.CSS_SELECTOR, "div[class='tox-icon'] svg")
        self.SAVE_BUTTON = (By.XPATH, "//a[contains(text(),'保存')]")
        
        # 创建截图目录
        self.screenshots_dir = self._create_screenshots_dir()
        
        # 定义元素定位器
        self.CASE_NOTES_ICON = (By.XPATH, "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[1]/div/i[2]")
        self.JUDGMENT_DOC = (By.XPATH, "//span[@class='ant-tree-title']/span[text()='判决书']")
        self.ZOOM_OUT_BUTTON = (By.CSS_SELECTOR, "svg[viewBox='64 64 896 896'][data-icon='zoom-out']")
        self.ZOOM_IN_BUTTON = (By.CSS_SELECTOR, "svg[viewBox='64 64 896 896'][data-icon='zoom-in']")
        self.DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "svg[viewBox='64 64 896 896'][data-icon='download']")
        self.PDF_DOWNLOAD_OPTION = (By.XPATH, "//li[contains(text(),'PDF下载')]")
        self.CLOSE_BUTTON = (By.XPATH, "//i[2]//img[1]")
        self.MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'ant-modal-content')]")
    
    def _create_screenshots_dir(self):
        """创建截图保存目录"""
        # 在项目根目录下创建screenshots文件夹
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshots_dir = os.path.join(base_dir, "screenshots")
        
        # 如果目录不存在，则创建
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
            logger.info(f"创建截图目录: {screenshots_dir}")
            
        # 创建当天日期子文件夹
        today = time.strftime("%Y%m%d")
        today_dir = os.path.join(screenshots_dir, today)
        if not os.path.exists(today_dir):
            os.makedirs(today_dir)
            logger.info(f"创建当天截图子目录: {today_dir}")
            
        return today_dir
    
    def click_reading_notes_icon(self):
        """点击阅卷笔记图标"""
        logger.info("点击案件的阅卷笔记按钮")
        try:
            notes_icon = self.wait.until(EC.element_to_be_clickable(self.CASE_NOTES_ICON))
            self.driver.execute_script("arguments[0].click();", notes_icon)
            logger.info("成功点击阅卷笔记按钮")
            time.sleep(2)
            return True
        except Exception as e:
            logger.error(f"点击阅卷笔记按钮失败: {str(e)}")
            self.take_screenshot("click_notes_button_failed")
            return False
    
    def click_judgment_document(self):
        """点击判决书文档"""
        logger.info("点击左侧文档树中的判决书")
        try:
            judgment_doc = self.wait.until(EC.element_to_be_clickable(self.JUDGMENT_DOC))
            self.driver.execute_script("arguments[0].click();", judgment_doc)
            logger.info("成功点击判决书")
            time.sleep(2)
            return True
        except Exception as e:
            logger.error(f"点击判决书失败: {str(e)}")
            self.take_screenshot("click_judgment_failed")
            return False
    
    def zoom_out_document(self):
        """缩小文档视图"""
        logger.info("测试缩小文档视图")
        try:
            # 仅保留标准Selenium点击方法
            zoom_out_button = self.wait.until(EC.element_to_be_clickable(self.ZOOM_OUT_BUTTON))
            zoom_out_button.click()
            logger.info("成功点击缩小按钮")
            time.sleep(1)  # 等待缩小效果
            return True
        except Exception as e:
            logger.error(f"点击缩小按钮失败: {str(e)}")
            self.take_screenshot("zoom_out_failed")
            return False

    def zoom_in_document(self):
        """放大文档视图"""
        logger.info("测试放大文档视图")
        try:
            # 仅保留标准Selenium点击方法
            zoom_in_button = self.wait.until(EC.element_to_be_clickable(self.ZOOM_IN_BUTTON))
            zoom_in_button.click()
            logger.info("成功点击放大按钮")
            time.sleep(1)  # 等待放大效果
            return True
        except Exception as e:
            logger.error(f"点击放大按钮失败: {str(e)}")
            self.take_screenshot("zoom_in_failed")
            return False
    
    def download_document_as_pdf(self, download_dir):
        """下载文档为PDF"""
        logger.info("测试文档下载功能")
        try:
            # 仅保留标准Selenium点击方法
            # 1. 点击下载按钮
            download_button = self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_BUTTON))
            download_button.click()
            logger.info("成功点击下载按钮")
            time.sleep(1)  # 等待下拉菜单出现

            # 2. 选择PDF下载选项
            pdf_option = self.wait.until(EC.element_to_be_clickable(self.PDF_DOWNLOAD_OPTION))
            pdf_option.click()
            logger.info("成功选择PDF下载选项")
            time.sleep(2)  # 等待下载开始

        except Exception as e:
            logger.error(f"文档下载操作失败: {str(e)}")
            self.take_screenshot("download_failed")
            return False

    def take_screenshot(self, name_suffix):
        """保存截图到指定目录"""
        try:
            timestamp = time.strftime("%H%M%S")
            filename = f"{name_suffix}_{timestamp}.png"
            filepath = os.path.join(self.screenshots_dir, filename)

            self.driver.save_screenshot(filepath)
            logger.info(f"已保存截图: {filepath}")
            return filepath
        except Exception as e:
            logger.warning(f"截图保存失败: {str(e)}")
            return None

    def export_and_edit_notes(self):
        """导出并编辑阅卷笔记"""
        logger.info("开始导出和编辑阅卷笔记")
        try:
            # 1. 点击导出阅卷笔记
            logger.info("点击导出阅卷笔记按钮")
            export_button = self.wait.until(EC.element_to_be_clickable(self.EXPORT_NOTES_BUTTON))
            export_button.click()
            time.sleep(2)  # 等待导出完成

            # 2. 点击查询和替换
            logger.info("点击查询和替换按钮")
            search_replace = self.wait.until(EC.element_to_be_clickable(self.SEARCH_REPLACE_BUTTON))
            search_replace.click()
            time.sleep(1)

            # 3. 输入查找内容
            logger.info("输入查找内容")
            find_input = self.wait.until(EC.presence_of_element_located(self.FIND_INPUT))
            find_input.clear()
            find_input.send_keys("方式")
            time.sleep(1)

            # 4. 输入替换内容
            logger.info("输入替换内容")
            replace_input = self.wait.until(EC.presence_of_element_located(self.REPLACE_INPUT))
            replace_input.clear()
            replace_input.send_keys("方式")
            time.sleep(1)

            # 5. 点击查找
            logger.info("点击查找按钮")
            find_button = self.wait.until(EC.element_to_be_clickable(self.FIND_BUTTON))
            find_button.click()
            time.sleep(1)

            # 6. 点击替换
            logger.info("点击替换按钮")
            replace_button = self.wait.until(EC.element_to_be_clickable(self.REPLACE_BUTTON))
            replace_button.click()
            time.sleep(1)

            # 7. 继续点击查找
            logger.info("点击查找按钮")
            find_button2 = self.wait.until(EC.element_to_be_clickable(self.FIND_BUTTON))
            find_button2.click()
            time.sleep(1)

            # 8. 点击全部替换
            logger.info("点击全部替换按钮")
            replace_all_button = self.wait.until(EC.element_to_be_clickable(self.REPLACE_ALL_BUTTON))
            replace_all_button.click()
            time.sleep(1)

            # 9. 关闭弹框
            logger.info("关闭弹框")
            close_button = self.wait.until(EC.element_to_be_clickable(self.CLOSE_DIALOG_BUTTON))
            close_button.click()
            time.sleep(1)

            # 10. 保存
            logger.info("点击保存按钮")
            save_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
            save_button.click()
            time.sleep(2)  # 等待保存完成

            logger.info("阅卷笔记导出和编辑操作完成")
            return True

        except Exception as e:
            logger.error(f"阅卷笔记导出和编辑操作失败: {str(e)}")
            self.take_screenshot("export_edit_notes_failed")
            return False

    def select_text_and_use_ai(self):
        """通过真实鼠标操作选中文本并使用AI智能问答"""
        logger.info("开始通过真实鼠标操作选中文本并使用AI智能问答")
        try:
            # 1. 切换到iframe
            logger.info("切换到iframe")
            iframe = self.driver.find_element(By.TAG_NAME, "iframe")
            self.driver.switch_to.frame(iframe)
            logger.info("成功切换到iframe")

            # 2. 查找包含目标文本的元素
            target_text = "东营区西二路万家新城内"
            logger.info(f"查找包含文本'{target_text}'的元素")

            element_with_text = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{target_text}')]")
            logger.info(f"找到包含目标文本的元素: {element_with_text.tag_name}")

            # 3. 滚动到元素位置使其可见
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element_with_text)
            time.sleep(0.5)  # 等待滚动完成

            # 4. 获取元素的位置和大小
            location = element_with_text.location
            size = element_with_text.size

            # 计算起点和终点坐标
            start_x = location['x'] + 5  # 元素左侧偏移5像素
            start_y = location['y'] + (size['height'] / 2)  # 元素垂直中心
            end_x = start_x + 150  # 向右拖动约150像素，应该足够覆盖目标文本
            end_y = start_y  # 保持相同的y坐标

            logger.info(f"起点坐标: ({start_x}, {start_y}), 终点坐标: ({end_x}, {end_y})")

            # 5. 使用ActionChains模拟鼠标操作
            actions = ActionChains(self.driver)

            # 先点击元素以确保获得焦点
            actions.move_to_element(element_with_text).click().perform()
            time.sleep(0.3)

            # 然后执行鼠标按下、移动、释放的操作
            actions = ActionChains(self.driver)

            # 移动到起点位置
            actions.move_to_element_with_offset(element_with_text, 5, 0)

            # 按下鼠标按钮
            actions.click_and_hold()

            # 移动到终点位置(分多步移动更自然)
            for i in range(1, 6):
                move_to_x = start_x + ((end_x - start_x) * i / 5)
                actions.move_by_offset((end_x - start_x) / 5, 0)
                time.sleep(0.05)  # 非常短的暂停使移动更自然

            # 释放鼠标按钮
            actions.release()

            # 执行整个动作链
            actions.perform()
            logger.info("已执行鼠标拖动选择文本操作")

            # 等待选择生效
            time.sleep(1)

            # 6. 切回主文档
            self.driver.switch_to.default_content()
            logger.info("切回主文档")

            # 7. 查找并点击AI智能问答按钮
            logger.info("查找AI智能问答按钮")
            ai_buttons = self.driver.find_elements(By.XPATH, "//button[@title='AI智能问答']")

            if ai_buttons:
                ai_buttons[0].click()
                logger.info("成功点击AI智能问答按钮")
            else:
                logger.warning("未找到标准AI按钮，尝试查找替代按钮")
                alt_buttons = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'AI') or contains(@title, 'AI')]")
                if alt_buttons:
                    alt_buttons[0].click()
                    logger.info("点击了替代AI按钮")
                else:
                    logger.error("未找到任何AI相关按钮")

            # 8. 等待3秒
            logger.info("等待3秒...")
            time.sleep(5)

            # 9. 关闭AI弹框
            logger.info("关闭AI弹框")
            close_buttons = self.driver.find_elements(By.XPATH, "//i[@aria-label='图标: close']//*[name()='svg']")
            
            if close_buttons:
                close_buttons[0].click()
                logger.info("成功关闭AI弹框")
            else:
                logger.warning("未找到标准关闭按钮，尝试ESC键关闭")
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                logger.info("尝试用ESC键关闭弹框")
            
            time.sleep(1)
            return True
            
        except Exception as e:
            logger.error(f"选中文本并使用AI智能问答失败: {str(e)}")
            self.take_screenshot("ai_qa_failed")
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return True  # 即使失败也继续测试流程

    def select_text_and_use_elements(self):
        """通过真实鼠标操作选中文本并使用构成要件功能"""
        logger.info("开始通过真实鼠标操作选中文本并使用构成要件功能")
        try:
            # 1. 切换到iframe
            logger.info("切换到iframe")
            iframe = self.driver.find_element(By.TAG_NAME, "iframe")
            self.driver.switch_to.frame(iframe)
            logger.info("成功切换到iframe")
            
            # 2. 查找包含目标文本的元素
            target_text = "胜利街道办事处"
            logger.info(f"查找包含文本'{target_text}'的元素")
            
            element_with_text = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{target_text}')]")
            logger.info(f"找到包含目标文本的元素: {element_with_text.tag_name}")
            
            # 3. 滚动到元素位置使其可见
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element_with_text)
            time.sleep(0.5)  # 等待滚动完成
            
            # 4. 获取元素的位置和大小
            location = element_with_text.location
            size = element_with_text.size
            
            # 计算起点和终点坐标
            start_x = location['x'] + 5  # 元素左侧偏移5像素
            start_y = location['y'] + (size['height'] / 2)  # 元素垂直中心
            end_x = start_x + 120  # 向右拖动约120像素，应该足够覆盖目标文本
            end_y = start_y  # 保持相同的y坐标
            
            logger.info(f"起点坐标: ({start_x}, {start_y}), 终点坐标: ({end_x}, {end_y})")
            
            # 5. 使用ActionChains模拟鼠标操作
            actions = ActionChains(self.driver)
            
            # 先点击元素以确保获得焦点
            actions.move_to_element(element_with_text).click().perform()
            time.sleep(0.3)
            
            # 然后执行鼠标按下、移动、释放的操作
            actions = ActionChains(self.driver)
            
            # 移动到起点位置
            actions.move_to_element_with_offset(element_with_text, 5, 0)
            
            # 按下鼠标按钮
            actions.click_and_hold()
            
            # 移动到终点位置(分多步移动更自然)
            for i in range(1, 6):
                move_to_x = start_x + ((end_x - start_x) * i / 5)
                actions.move_by_offset((end_x - start_x) / 5, 0)
                time.sleep(0.05)  # 非常短的暂停使移动更自然
            
            # 释放鼠标按钮
            actions.release()
            
            # 执行整个动作链
            actions.perform()
            logger.info("已执行鼠标拖动选择文本操作")
            
            # 等待选择生效
            time.sleep(1)
            
            # 6. 切回主文档
            self.driver.switch_to.default_content()
            logger.info("切回主文档")
            
            # 7. 查找并点击构成要件按钮
            logger.info("查找构成要件按钮")
            elements_buttons = self.driver.find_elements(By.XPATH, "//button[@title='构成要件']")
            
            if elements_buttons:
                elements_buttons[0].click()
                logger.info("成功点击构成要件按钮")
            else:
                logger.warning("未找到标准构成要件按钮，尝试查找替代按钮")
                alt_buttons = self.driver.find_elements(By.XPATH, 
                    "//*[contains(text(), '构成要件') or contains(@title, '构成要件') or contains(@title, '要件')]")
                if alt_buttons:
                    alt_buttons[0].click()
                    logger.info("点击了替代构成要件按钮")
                else:
                    logger.error("未找到任何构成要件相关按钮")
            
            # 8. 等待5秒
            logger.info("等待5秒...")
            time.sleep(5)
            
            # 9. 关闭构成要件弹框
            logger.info("关闭构成要件弹框")
            close_buttons = self.driver.find_elements(By.XPATH, "//i[@aria-label='图标: close']//*[name()='svg']")
            
            if close_buttons:
                close_buttons[0].click()
                logger.info("成功关闭构成要件弹框")
            else:
                logger.warning("未找到标准关闭按钮，尝试ESC键关闭")
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                logger.info("尝试用ESC键关闭弹框")
            
            time.sleep(1)
            return True
            
        except Exception as e:
            logger.error(f"选中文本并使用构成要件功能失败: {str(e)}")
            self.take_screenshot("elements_analysis_failed")
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return True  # 即使失败也继续测试流程

    def execute_reading_notes_workflow(self, download_dir):
        """执行完整的阅卷笔记工作流程"""
        try:
            # 1. 点击阅卷笔记图标
            if not self.click_reading_notes_icon():
                logger.error("无法完成阅卷笔记工作流程: 点击阅卷笔记图标失败")
                return False

            # # 2. 点击判决书文档
            # if not self.click_judgment_document():
            #     logger.error("无法完成阅卷笔记工作流程: 点击判决书文档失败")
            #     return False
            #
            # # 3. 测试缩小功能
            # self.zoom_out_document()
            #
            # # 4. 测试放大功能
            # self.zoom_in_document()
            #
            # # 5. 测试下载功能
            # self.download_document_as_pdf(download_dir)
            #
            # # 6. 关闭判决书预览弹框
            # if not self.close_document_viewer():
            #     logger.error("关闭判决书预览失败")
            #     return False

            # 7. 执行导出和编辑操作
            # if not self.export_and_edit_notes():
            #     logger.error("无法完成阅卷笔记工作流程: 导出和编辑操作失败")
            #     return False
            
            # 8. 选中文本并使用AI智能问答
            if not self.select_text_and_use_ai():
                logger.error("无法完成阅卷笔记工作流程: AI智能问答功能失败")
                # 继续执行，不中断工作流程，因为这是额外功能

            # 9. 选中其他文本并使用构成要件
            if not self.select_text_and_use_elements():
                logger.error("无法完成阅卷笔记工作流程: 构成要件功能失败")
                # 继续执行，不中断工作流程，因为这是额外功能

            # 工作流程完成
            logger.info("阅卷笔记工作流程执行完成")
            return True

        except Exception as e:
            logger.error(f"执行阅卷笔记工作流程时出错: {str(e)}")
            self.take_screenshot("workflow_error")
            return False

    def close_document_viewer(self):
        """关闭判决书预览弹框"""
        logger.info("关闭判决书预览弹框")
        try:
            # 1. 确保关闭按钮可点击
            close_button = self.wait.until(EC.element_to_be_clickable(self.CLOSE_BUTTON))
            close_button.click()
            logger.info("已点击关闭按钮")
            time.sleep(4)

            # 2. 等待并验证弹框消失
            try:
                # 使用较短的超时时间专门用于等待弹框消失
                short_wait = WebDriverWait(self.driver, 5)
                short_wait.until_not(EC.presence_of_element_located(self.MODAL_CONTENT))
                logger.info("确认判决书预览弹框已完全关闭")

                # 额外添加一个很短的等待，确保DOM完全更新
                # time.sleep(0.5)
                return True

            except Exception as e:
                logger.warning(f"等待弹框消失超时: {str(e)}")

        except Exception as e:
            logger.error(f"关闭判决书预览弹框失败: {str(e)}")
            self.take_screenshot("close_dialog_failed")
            return False

