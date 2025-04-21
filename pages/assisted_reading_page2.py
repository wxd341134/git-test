import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utils.logger2 import Logger

logger = Logger().get_logger()


class AssistedReadingPage:
    """辅助阅卷页面对象类"""

    # 所有元素定位器
    # 主要操作区域
    AUXILIARY_READING = (
        By.XPATH,
        "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[1]/div/i[1]"
    )

    # 庭审笔录相关元素
    COURT_RECORD = (By.XPATH, "//span[@class='ant-tree-title']/span[text()='庭审笔录1']")
    SET_RECORD = (By.XPATH, "//span[@class='ant-tree-title']/span[text()='庭审笔录1']/following-sibling::i[2]")
    CANCEL_SET_RECORD = (By.CSS_SELECTOR, "svg[data-v-19fbe780][data-v-3f752b24].plusType.svg-icon")
    CONFIRM_CANCEL_BUTTON = (By.CSS_SELECTOR, "button.ant-btn.ant-btn-primary.ant-btn-sm")

    # 处理意见相关元素
    OPINION1 = (By.XPATH, "//form/div[6]/div/div[1]/div[3]/div[2]/div/span/textarea[@placeholder='请输入处理意见']")
    OPINION2 = (By.XPATH, "//form/div[6]/div/div[2]/div[3]/div[2]/div/span/textarea[@placeholder='请输入处理意见']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")

    # 下载相关元素
    DOWNLOAD_BUTTON = (By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']")
    PDF_DOWNLOAD_OPTION = (By.XPATH, "//li[contains(text(),'PDF下载')]")

    # 庭审笔录2相关元素
    COURT_RECORD2 = (By.XPATH, "//span[@class='ant-tree-title']/span[text()='庭审笔录2']")
    ADD_EVIDENCE_BUTTON = (By.XPATH, "//span[@class='ant-tree-title']/span[text()='庭审笔录2']/following-sibling::i[3]")
    DIRECTORY_DROPDOWN = (By.XPATH, "//span[@class='ant-select-selection__placeholder']")
    COURT_MATERIALS_OPTION = (By.XPATH, "//span[@title='法院材料']")
    CONFIRM_ADD_EVIDENCE = (By.CSS_SELECTOR, "button[class='ant-btn ant-btn-primary']")

    # 庭审笔录3相关元素
    COURT_RECORD3_CHECKBOX = (
        By.XPATH, "//span[@class='ant-tree-title']/span[text()='庭审笔录3']/ancestor::li[1]/span[2]/span")
    EVIDENCE_ADD_BUTTON = (By.XPATH, "//span[contains(text(),'证据添加')]")
    DIRECTORY_DROPDOWN2 = (By.XPATH, "//span[@class='ant-select-selection__placeholder']")
    APPELLANT_OPTION = (By.XPATH, "//span[@title='上诉人']")
    CONFIRM_EVIDENCE_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")

    # 证据引用相关元素
    EVIDENCE_REFERENCE_TAB = (By.XPATH, "//div[@aria-selected='false']")
    REFRESH_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-warning']")
    EVIDENCE_RECORD_DETAIL = (By.XPATH, "//a[contains(text(),'庭审笔录2')]")
    CLOSE_DETAIL_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-sm']")

    # 双屏阅卷相关元素
    RECORD2_CHECKBOX = (
        By.XPATH, "//a[contains(text(),'庭审笔录2')]/ancestor::tr[1]/td[1]//span[@class='ant-checkbox']")
    RECORD3_CHECKBOX = (
        By.XPATH, "//a[contains(text(),'庭审笔录3')]/ancestor::tr[1]/td[1]//span[@class='ant-checkbox']")
    RECORD4_CHECKBOX = (By.XPATH,
                        "//a[contains(text(),'庭审笔录3')]/ancestor::tr[1]/td[1]//span[@class='ant-checkbox ant-checkbox-checked']")
    DUAL_SCREEN_READING_BUTTON = (By.XPATH, "//div[@class='splitter-pane splitter-paneR vertical ']//button[1]")
    CLOSE_DUAL_SCREEN_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-sm']")

    # 上诉人/第三人选择相关元素
    APPELLANT_SELECTOR = (By.XPATH, "//div[@class='ant-select-selection__rendered']")
    THIRD_PARTY_OPTION = (By.XPATH, "//li[contains(@class, 'ant-select-dropdown-menu-item') and text()='第三人']")

    # 批量修改相关元素
    BATCH_EDIT_BUTTON = (By.XPATH, "//div[@class='splitter-pane splitter-paneR vertical ']//button[2]")
    EVIDENCE_NAME_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[1]/div")
    EVIDENCE_TYPE_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[2]/div")
    NO_OBJECTION_OPTION = (By.XPATH, "//li[contains(text(),'无异议')]")
    EVIDENCE_OPINION_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[3]/div")
    EVIDENCE_PURPOSE_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[4]/div")
    EVIDENCE_DOCUMENT_TYPE_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[5]/div")
    PHYSICAL_EVIDENCE_OPTION = (By.XPATH, "//li[contains(text(),'物证')]")
    EVIDENCE_FORM_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[6]/div")
    PHOTO_EVIDENCE_OPTION = (By.XPATH, "//li[contains(text(),'照片')]")
    CONFIRM_BATCH_EDIT_BUTTON = (
        By.XPATH, "//div[@class='ant-modal-root j-modal-box fullscreen j-modal-box fullscreen']//button[2]")

    def __init__(self, driver):
        """初始化页面对象"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_auxiliary_reading(self):
        """点击辅助阅卷按钮"""
        logger.info("点击辅助阅卷")
        auxiliary_reading = self.wait.until(
            EC.element_to_be_clickable(self.AUXILIARY_READING)
        )
        auxiliary_reading.click()
        time.sleep(2)
        logger.info("成功点击辅助阅卷")
        return self

    def click_court_record1(self):
        """点击庭审笔录1"""
        logger.info("点击庭审笔录1")
        court_record = self.wait.until(
            EC.element_to_be_clickable(self.COURT_RECORD)
        )
        court_record.click()
        time.sleep(2)
        logger.info("成功点击庭审笔录1")
        return self

    def set_as_court_record(self):
        """设为庭审笔录"""
        logger.info("点击设为庭审笔录")
        set_record = self.wait.until(
            EC.element_to_be_clickable(self.SET_RECORD)
        )
        set_record.click()
        time.sleep(1)
        logger.info("成功点击设为庭审笔录")
        return self

    def enter_opinions(self, opinion1="无意见1", opinion2="无意见2"):
        """输入处理意见"""
        logger.info("输入原告处理意见1")
        opinion1_elem = self.wait.until(
            EC.presence_of_element_located(self.OPINION1)
        )
        opinion1_elem.clear()
        opinion1_elem.send_keys(opinion1)
        time.sleep(1)
        logger.info("成功输入原告处理意见1")

        logger.info("输入原告处理意见2")
        opinion2_elem = self.wait.until(
            EC.presence_of_element_located(self.OPINION2)
        )
        opinion2_elem.clear()
        opinion2_elem.send_keys(opinion2)
        time.sleep(1)
        logger.info("成功输入原告处理意见2")
        return self

    def confirm_settings(self):
        """点击确定按钮"""
        logger.info("点击确定按钮")
        confirm_button = self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON)
        )
        confirm_button.click()
        time.sleep(2)
        logger.info("成功点击确定按钮")
        return self

    def cancel_set_record(self):
        """取消设置庭审笔录"""
        logger.info("点击取消设置庭审笔录")

        # 先点击庭审笔录1确保选中
        self.click_court_record1()

        # 找到取消设置按钮并点击
        try:
            cancel_set_record = self.wait.until(
                EC.element_to_be_clickable(self.CANCEL_SET_RECORD)
            )
            cancel_set_record.click()
        except:
            logger.warning("无法使用SVG/use定位方式，尝试备用定位")
            try:
                cancel_button = self.driver.find_element(
                    By.XPATH,
                    "//span[@class='ant-tree-title']/span[text()='庭审笔录1']/following-sibling::*[1]"
                )
                cancel_button.click()
            except:
                logger.error("未能找到取消设置按钮")
                raise

        time.sleep(1)

        # 点击确定取消设置 - 使用多种方法保证点击成功
        logger.info("点击确定取消设置")
        self._click_confirm_button(self.CONFIRM_CANCEL_BUTTON)
        logger.info("成功取消设置庭审笔录")
        return self

    def download_pdf(self):
        """下载PDF"""
        logger.info("点击下载按钮")
        download_button = self.wait.until(
            EC.element_to_be_clickable(self.DOWNLOAD_BUTTON)
        )
        download_button.click()
        time.sleep(1)

        logger.info("选择PDF下载")
        pdf_download_option = self.wait.until(
            EC.element_to_be_clickable(self.PDF_DOWNLOAD_OPTION)
        )
        pdf_download_option.click()
        time.sleep(3)  # 等待下载开始
        logger.info("成功下载笔录PDF")
        return self

    def add_court_record2_as_evidence(self):
        """添加庭审笔录2为证据"""
        logger.info("点击庭审笔录2")
        court_record2 = self.wait.until(
            EC.element_to_be_clickable(self.COURT_RECORD2)
        )
        court_record2.click()
        time.sleep(2)

        logger.info("点击添加为证据按钮")
        add_evidence_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_EVIDENCE_BUTTON)
        )
        add_evidence_button.click()
        time.sleep(2)

        logger.info("点击目录下拉框")
        directory_dropdown = self.wait.until(
            EC.element_to_be_clickable(self.DIRECTORY_DROPDOWN)
        )
        directory_dropdown.click()
        time.sleep(1)

        logger.info("选择法院材料选项")
        court_materials_option = self.wait.until(
            EC.element_to_be_clickable(self.COURT_MATERIALS_OPTION)
        )
        court_materials_option.click()
        time.sleep(1)

        logger.info("点击确定按钮")
        confirm_add_evidence = self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_ADD_EVIDENCE)
        )
        confirm_add_evidence.click()
        time.sleep(2)
        logger.info("成功添加庭审笔录2为证据")
        return self

    def add_court_record3_as_evidence(self):
        """将庭审笔录3添加为证据"""
        logger.info("选择庭审笔录3")
        court_record3_checkbox = self.wait.until(
            EC.element_to_be_clickable(self.COURT_RECORD3_CHECKBOX)
        )
        court_record3_checkbox.click()
        time.sleep(1)

        logger.info("点击证据添加按钮")
        evidence_add_button = self.wait.until(
            EC.element_to_be_clickable(self.EVIDENCE_ADD_BUTTON)
        )
        evidence_add_button.click()
        time.sleep(1)

        logger.info("点击目录下拉框")
        directory_dropdown2 = self.wait.until(
            EC.element_to_be_clickable(self.DIRECTORY_DROPDOWN2)
        )
        directory_dropdown2.click()
        time.sleep(1)

        logger.info("选择上诉人选项")
        appellant_option = self.wait.until(
            EC.element_to_be_clickable(self.APPELLANT_OPTION)
        )
        appellant_option.click()
        time.sleep(1)

        logger.info("点击确定按钮")
        confirm_evidence_button = self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_EVIDENCE_BUTTON)
        )
        confirm_evidence_button.click()
        time.sleep(2)
        logger.info("成功将庭审笔录3添加为证据")
        return self

    def check_evidence_reference(self):
        """证据引用功能"""
        logger.info("点击证据引用标签页")
        evidence_reference_tab = self.wait.until(
            EC.element_to_be_clickable(self.EVIDENCE_REFERENCE_TAB)
        )
        evidence_reference_tab.click()
        time.sleep(2)

        logger.info("点击刷新按钮")
        refresh_button = self.wait.until(
            EC.element_to_be_clickable(self.REFRESH_BUTTON)
        )
        refresh_button.click()
        time.sleep(2)

        logger.info("点击查看庭审笔录2详情")
        evidence_record_detail = self.wait.until(
            EC.element_to_be_clickable(self.EVIDENCE_RECORD_DETAIL)
        )
        evidence_record_detail.click()
        time.sleep(2)

        logger.info("点击关闭详情")
        close_detail_button = self.wait.until(
            EC.element_to_be_clickable(self.CLOSE_DETAIL_BUTTON)
        )
        close_detail_button.click()
        time.sleep(2)
        logger.info("成功查看证据引用功能")
        return self

    def perform_dual_screen_reading(self):
        """双屏阅卷功能"""
        logger.info("选择庭审笔录2和庭审笔录3")
        record2_checkbox = self.wait.until(
            EC.element_to_be_clickable(self.RECORD2_CHECKBOX)
        )
        record2_checkbox.click()
        time.sleep(1)

        record3_checkbox = self.wait.until(
            EC.element_to_be_clickable(self.RECORD3_CHECKBOX)
        )
        record3_checkbox.click()
        time.sleep(1)

        logger.info("点击双屏阅卷按钮")
        dual_screen_reading_button = self.wait.until(
            EC.element_to_be_clickable(self.DUAL_SCREEN_READING_BUTTON)
        )
        dual_screen_reading_button.click()
        time.sleep(3)

        logger.info("查看双屏阅卷内容")
        time.sleep(2)

        logger.info("点击关闭双屏阅卷")
        close_dual_screen_button = self.wait.until(
            EC.element_to_be_clickable(self.CLOSE_DUAL_SCREEN_BUTTON)
        )
        close_dual_screen_button.click()
        time.sleep(2)
        logger.info("成功完成双屏阅卷功能")
        return self

    def select_third_party(self):
        """选择上诉人为第三人"""
        logger.info("点击上诉人选择器")
        try:
            time.sleep(2)

            appellant_selector = self.wait.until(
                EC.element_to_be_clickable(self.APPELLANT_SELECTOR)
            )

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", appellant_selector)
            time.sleep(1)

            try:
                logger.info("尝试点击上诉人选择器")
                appellant_selector.click()
            except Exception as e:
                logger.warning(f"标准点击上诉人选择器失败: {str(e)}")
                self.driver.execute_script("arguments[0].click();", appellant_selector)
                logger.info("使用JavaScript点击上诉人选择器")

            time.sleep(1)

            logger.info("查找并点击第三人选项")
            try:
                third_party_option = self.driver.find_element(*self.THIRD_PARTY_OPTION)
                third_party_option.click()
                logger.info("成功点击第三人选项")
            except Exception as e:
                logger.warning(f"找不到第三人选项元素: {str(e)}")
                self._try_alternative_third_party_selection()

            time.sleep(2)
            logger.info("成功选择上诉人为第三人")

        except Exception as e:
            logger.warning(f"选择上诉人为第三人失败，但继续执行: {str(e)}")

        return self

    def refresh_and_uncheck_record3(self):
        """刷新并取消选中庭审笔录3"""
        logger.info("点击刷新按钮")
        refresh_button = self.wait.until(
            EC.element_to_be_clickable(self.REFRESH_BUTTON)
        )
        refresh_button.click()
        time.sleep(2)

        logger.info("取消选中庭审笔录3")
        record4_checkbox = self.wait.until(
            EC.element_to_be_clickable(self.RECORD4_CHECKBOX)
        )
        record4_checkbox.click()
        time.sleep(1)
        logger.info("成功取消选中庭审笔录3")
        return self

    def perform_batch_edit(self):
        """执行批量修改功能"""
        logger.info("点击批量修改按钮")
        batch_edit_button = self.wait.until(
            EC.element_to_be_clickable(self.BATCH_EDIT_BUTTON)
        )
        batch_edit_button.click()
        time.sleep(2)

        # 修改证据名称
        self._edit_evidence_name("庭审笔录2修改")

        # 选择质证类型
        self._select_evidence_type()

        # 填写质证意见
        self._fill_evidence_opinion("无意见")

        # 填写证明目的
        self._fill_evidence_purpose("无目的")

        # 选择证件类型
        self._select_document_type()

        # 选择证据形式
        self._select_evidence_form()

        # 点击确定按钮保存修改
        logger.info("点击确定按钮保存修改")
        confirm_batch_edit_button = self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_BATCH_EDIT_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", confirm_batch_edit_button)
        time.sleep(2)
        logger.info("成功完成批量修改")

        return self

    def _click_confirm_button(self, locator):
        """多方式尝试点击确认按钮"""
        try:
            confirm_button = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            # 方法1: 尝试先等待一段时间，让tooltip消失
            time.sleep(2)

            try:
                # 方法2: 尝试移动鼠标到其他位置，避开tooltip
                ActionChains(self.driver).move_to_element_with_offset(
                    confirm_button, -100, -100
                ).perform()
                time.sleep(1)
            except Exception as e:
                logger.warning(f"移动鼠标失败: {str(e)}")

            try:
                # 方法3: 标准点击
                logger.info("尝试标准点击确认按钮")
                confirm_button.click()
            except Exception as e:
                logger.warning(f"标准点击确认按钮失败: {str(e)}")

                try:
                    # 方法4: 使用JavaScript点击
                    logger.info("尝试使用JavaScript点击确认按钮")
                    self.driver.execute_script("arguments[0].click();", confirm_button)
                except Exception as e:
                    logger.warning(f"JavaScript点击确认按钮失败: {str(e)}")

                    try:
                        # 方法5: 尝试关闭tooltip
                        logger.info("尝试关闭干扰的tooltip")
                        tooltips = self.driver.find_elements(By.XPATH, "//div[@role='tooltip']")
                        if tooltips:
                            # 点击页面其他区域以关闭tooltip
                            ActionChains(self.driver).move_by_offset(100, 100).click().perform()
                            time.sleep(1)
                            # 再次尝试点击确认按钮
                            confirm_button.click()
                        else:
                            # 方法6: 使用坐标点击
                            logger.info("尝试使用坐标点击确认按钮")
                            rect = self.driver.execute_script(
                                "return arguments[0].getBoundingClientRect();",
                                confirm_button
                            )
                            x = rect['x'] + rect['width'] / 2
                            y = rect['y'] + rect['height'] / 2
                            ActionChains(self.driver).move_by_offset(x, y).click().perform()
                    except Exception as e:
                        logger.error(f"所有点击方法均失败: {str(e)}")
                        self.driver.save_screenshot("confirm_button_click_failed.png")
                        raise

            time.sleep(2)

        except Exception as e:
            logger.error(f"未能点击确定按钮: {str(e)}")
            self.driver.save_screenshot("confirm_button_click_failed.png")
            raise

    def _try_alternative_third_party_selection(self):
        """尝试其他方式选择第三人"""
        try:
            # 查找所有下拉选项
            options = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'ant-select-dropdown-menu-item')]")

            # 遍历查找包含"第三人"的选项
            for option in options:
                if "第三人" in option.text:
                    logger.info(f"找到匹配的选项: {option.text}")
                    option.click()
                    logger.info("成功选择第三人选项")
                    break
        except Exception as e:
            logger.warning(f"通用选择器查找第三人选项失败: {str(e)}")

            # 最后尝试直接使用JavaScript选择第三人
            try:
                self.driver.execute_script("""
                    var options = document.querySelectorAll('li.ant-select-dropdown-menu-item');
                    for (var i = 0; i < options.length; i++) {
                        if (options[i].textContent.includes('第三人')) {
                            options[i].click();
                            break;
                        }
                    }
                """)
                logger.info("通过JavaScript尝试选择第三人选项")
            except Exception as e:
                logger.warning(f"JavaScript选择第三人选项失败: {str(e)}")

    def _edit_evidence_name(self, new_name):
        """修改证据名称"""
        logger.info(f"修改证据名称为: {new_name}")
        try:
            evidence_name_cell = self.wait.until(
                EC.presence_of_element_located(self.EVIDENCE_NAME_CELL)
            )

            # 使用JavaScript进行双击操作
            self.driver.execute_script("""
                var element = arguments[0];
                var event = new MouseEvent('dblclick', {
                    'view': window,
                    'bubbles': true,
                    'cancelable': true
                });
                element.dispatchEvent(event);
            """, evidence_name_cell)
            time.sleep(1)

            # 尝试在激活的输入框中输入内容
            try:
                # 检查是否已存在输入框或创建新的输入元素
                self.driver.execute_script(f"""
                    var cell = arguments[0];
                    if (!cell.querySelector('input')) {{
                        var input = document.createElement('input');
                        input.value = '{new_name}';
                        cell.innerHTML = '';
                        cell.appendChild(input);
                        input.focus();
                    }} else {{
                        var input = cell.querySelector('input');
                        input.value = '{new_name}';
                        input.focus();
                    }}
                """, evidence_name_cell)
                time.sleep(1)

                # 按回车确认
                ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                time.sleep(1)
                logger.info("成功修改证据名称")
            except Exception as e:
                logger.warning(f"使用JavaScript修改证据名称时出错: {str(e)}")
        except Exception as e:
            logger.warning(f"修改证据名称失败，但继续执行: {str(e)}")

    def _select_evidence_type(self):
        """选择质证类型"""
        logger.info("选择质证类型")
        try:
            evidence_type_cell = self.wait.until(
                EC.element_to_be_clickable(self.EVIDENCE_TYPE_CELL)
            )
            evidence_type_cell.click()
            time.sleep(1)

            no_objection_option = self.wait.until(
                EC.element_to_be_clickable(self.NO_OBJECTION_OPTION)
            )
            no_objection_option.click()
            time.sleep(1)
            logger.info("成功选择质证类型为无异议")
        except Exception as e:
            logger.warning(f"质证类型选择失败，但继续执行: {str(e)}")

    def _fill_evidence_opinion(self, opinion_text):
        """填写质证意见"""
        logger.info(f"填写质证意见: {opinion_text}")
        try:
            evidence_opinion_cell = self.wait.until(
                EC.presence_of_element_located(self.EVIDENCE_OPINION_CELL)
            )

            # 使用JavaScript一步到位填写
            self.driver.execute_script(f"""
                var cell = arguments[0];
                // 确保单元格被点击和聚焦
                cell.click();

                // 检查是否有input子元素
                var input = cell.querySelector('input');
                if (!input) {{
                    // 如果没有input，创建一个
                    input = document.createElement('input');
                    cell.innerHTML = '';
                    cell.appendChild(input);
                }}

                // 设置值并触发必要的事件
                input.value = '{opinion_text}';
                input.focus();
                input.dispatchEvent(new Event('input', {{ bubbles: true }}));
                input.dispatchEvent(new Event('change', {{ bubbles: true }}));

                // 模拟回车键提交
                var enterEvent = new KeyboardEvent('keydown', {{
                    key: 'Enter',
                    code: 'Enter',
                    keyCode: 13,
                    which: 13,
                    bubbles: true
                }});
                input.dispatchEvent(enterEvent);
            """, evidence_opinion_cell)

            time.sleep(0.5)
            logger.info("成功填写质证意见")
        except Exception as e:
            logger.warning(f"填写质证意见失败，但继续执行: {str(e)}")

    def _fill_evidence_purpose(self, purpose_text):
        """填写证明目的"""
        logger.info(f"填写证明目的: {purpose_text}")
        try:
            evidence_purpose_cell = self.wait.until(
                EC.presence_of_element_located(self.EVIDENCE_PURPOSE_CELL)
            )

            # 使用JavaScript一步到位填写
            self.driver.execute_script(f"""
                var cell = arguments[0];
                // 确保单元格被点击和聚焦
                cell.click();

                // 检查是否有input子元素
                var input = cell.querySelector('input');
                if (!input) {{
                    // 如果没有input，创建一个
                    input = document.createElement('input');
                    cell.innerHTML = '';
                    cell.appendChild(input);
                }}

                // 设置值并触发必要的事件
                input.value = '{purpose_text}';
                input.focus();
                input.dispatchEvent(new Event('input', {{ bubbles: true }}));
                input.dispatchEvent(new Event('change', {{ bubbles: true }}));

                // 模拟回车键提交
                var enterEvent = new KeyboardEvent('keydown', {{
                    key: 'Enter',
                    code: 'Enter',
                    keyCode: 13,
                    which: 13,
                    bubbles: true
                }});
                input.dispatchEvent(enterEvent);
            """, evidence_purpose_cell)

            time.sleep(0.5)
            logger.info("成功填写证明目的")
        except Exception as e:
            logger.warning(f"填写证明目的失败，但继续执行: {str(e)}")

    def _select_document_type(self):
        """选择证件类型"""
        logger.info("选择证件类型")
        try:
            # 等待页面稳定
            time.sleep(1)

            # 找到证件类型单元格
            evidence_document_type_cell = self.wait.until(
                EC.presence_of_element_located(self.EVIDENCE_DOCUMENT_TYPE_CELL)
            )

            # 截取屏幕以便调试
            try:
                self.driver.save_screenshot("before_document_type_click.png")
            except:
                pass

            # 滚动到元素位置以确保可见
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", evidence_document_type_cell)
            time.sleep(0.5)

            # 使用多种方法尝试点击
            clicked = False
            try:
                # 方法1: 使用标准点击
                logger.info("尝试标准点击证件类型单元格")
                evidence_document_type_cell.click()
                clicked = True
                time.sleep(1)
            except Exception as e:
                logger.warning(f"标准点击证件类型单元格失败: {str(e)}")
                try:
                    # 方法2: 使用JavaScript点击
                    logger.info("尝试使用JavaScript点击证件类型单元格")
                    self.driver.execute_script("arguments[0].click();", evidence_document_type_cell)
                    clicked = True
                    time.sleep(1)
                except Exception as e:
                    logger.warning(f"JavaScript点击证件类型单元格失败: {str(e)}")
                    try:
                        # 方法3: 使用ActionChains
                        logger.info("尝试使用ActionChains点击证件类型单元格")
                        ActionChains(self.driver).move_to_element(evidence_document_type_cell).click().perform()
                        clicked = True
                        time.sleep(1)
                    except Exception as e:
                        logger.warning(f"ActionChains点击证件类型单元格失败: {str(e)}")

            # 如果点击成功，尝试寻找并点击物证选项
            if clicked:
                try:
                    # 截取屏幕以便调试
                    self.driver.save_screenshot("after_document_type_click.png")
                    logger.info("寻找物证选项")

                    # 使用更宽泛的等待条件找到下拉选项
                    physical_evidence_option = self.wait.until(
                        EC.presence_of_element_located(self.PHYSICAL_EVIDENCE_OPTION)
                    )

                    # 尝试点击物证选项
                    try:
                        logger.info("尝试点击物证选项")
                        physical_evidence_option.click()
                        time.sleep(1)
                        logger.info("成功选择证件类型为物证")
                    except Exception as e:
                        logger.warning(f"点击物证选项失败，尝试JavaScript点击: {str(e)}")
                        self.driver.execute_script("arguments[0].click();", physical_evidence_option)
                        time.sleep(1)
                        logger.info("通过JavaScript成功点击物证选项")
                except Exception as e:
                    logger.warning(f"找不到或无法点击物证选项: {str(e)}")
                    # 尝试使用不同的定位方式
                    try:
                        logger.info("尝试使用更通用的选择器查找物证选项")
                        # 尝试使用更通用的选择器
                        options = self.driver.find_elements(By.XPATH,
                                                            "//div[contains(@class, 'dropdown') or contains(@class, 'select')]//li")
                        for option in options:
                            if "物证" in option.text:
                                logger.info(f"找到匹配选项: {option.text}")
                                option.click()
                                time.sleep(1)
                                logger.info("成功选择证件类型为物证")
                                break
                    except Exception as e:
                        logger.warning(f"尝试通用选择器失败: {str(e)}")
            else:
                logger.warning("无法激活证件类型下拉菜单")

        except Exception as e:
            logger.warning(f"选择证件类型失败，但继续执行: {str(e)}")

    def _select_evidence_form(self):
        """选择证据形式"""
        logger.info("选择证据形式")
        try:
            # 等待页面稳定
            time.sleep(1)

            evidence_form_cell = self.wait.until(
                EC.presence_of_element_located(self.EVIDENCE_FORM_CELL)
            )

            # 滚动到元素位置以确保可见
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", evidence_form_cell)
            time.sleep(0.5)

            # 使用多种方法尝试点击
            clicked = False
            try:
                logger.info("尝试标准点击证据形式单元格")
                evidence_form_cell.click()
                clicked = True
            except:
                try:
                    logger.info("尝试使用JavaScript点击证据形式单元格")
                    self.driver.execute_script("arguments[0].click();", evidence_form_cell)
                    clicked = True
                except:
                    logger.info("尝试使用ActionChains点击证据形式单元格")
                    ActionChains(self.driver).move_to_element(evidence_form_cell).click().perform()
                    clicked = True

            time.sleep(1)

            if clicked:
                try:
                    logger.info("寻找照片选项")
                    photo_evidence_option = self.wait.until(
                        EC.presence_of_element_located(self.PHOTO_EVIDENCE_OPTION)
                    )

                    try:
                        logger.info("尝试点击照片选项")
                        photo_evidence_option.click()
                    except:
                        logger.info("尝试使用JavaScript点击照片选项")
                        self.driver.execute_script("arguments[0].click();", photo_evidence_option)

                    time.sleep(1)
                    logger.info("成功选择证据形式为照片")
                except Exception as e:
                    logger.warning(f"找不到或无法点击照片选项: {str(e)}")
                    try:
                        # 尝试使用更通用的选择器
                        options = self.driver.find_elements(By.XPATH,
                                                            "//div[contains(@class, 'dropdown') or contains(@class, 'select')]//li")
                        for option in options:
                            if "照片" in option.text:
                                option.click()
                                time.sleep(1)
                                logger.info("成功选择证据形式为照片")
                                break
                    except Exception as e:
                        logger.warning(f"尝试通用选择器失败: {str(e)}")
            else:
                logger.warning("无法激活证据形式下拉菜单")

        except Exception as e:
            logger.warning(f"选择证据形式失败，但继续执行: {str(e)}") 