import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.caseMg_page import CasePage
from utils.logger import Logger

logger = Logger().get_logger()


class CaseUtils:
    """案件管理工具类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.current_time = "2025-07-18 07:11:55"
        self.current_user = "wxd341134"

    def _click_element(self, locator, element_name):
        """通用点击元素方法"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"{self.current_time} - {self.current_user} - 点击 {element_name} 成功")
            time.sleep(1)
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 点击 {element_name} 失败: {str(e)}")
            self._take_screenshot(f"{element_name}点击失败")
            return False

    def _input_text(self, locator, text, element_name):
        """通用文本输入方法"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            logger.info(f"{self.current_time} - {self.current_user} - 在 {element_name} 中输入文本 '{text}' 成功")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 文本输入失败: {str(e)}")
            self._take_screenshot(f"{element_name}输入失败")
            return False

    def _take_screenshot(self, name):
        """统一的截图方法"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("添加案件: {case_name}")
    def add_case(self, case_name, case_number):
        """添加案件流程"""
        try:
            # 点击添加按钮
            with allure.step("点击添加按钮"):
                if not self._click_element(CasePage.add_button, "添加按钮"):
                    return False

            # 填写基本信息
            with allure.step("填写案件信息"):
                if not self._input_text(CasePage.case_name_input, case_name, "案件名称"):
                    return False
                if not self._input_text(CasePage.case_number_input, case_number, "案件编号"):
                    return False

            # 选择案件类型
            with allure.step("选择案件类型"):
                if not self._select_case_type():
                    return False

            # 选择案由
            with allure.step("选择案由类型"):
                if not self._select_case_reason():
                    return False

            # 填写原审案号
            with allure.step("填写原审案号"):
                if not self._input_original_case_number(case_number):
                    return False

            # 选择日期
            with allure.step("选择立案日期"):
                if not self._select_filing_date():
                    return False

            # 提交表单
            with allure.step("提交案件信息"):
                if not self._click_element(CasePage.confirm_button, "确认按钮"):
                    return False

            logger.info(f"{self.current_time} - {self.current_user} - 案件添加成功: {case_name}")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 案件添加失败: {str(e)}")
            self._take_screenshot("add_case_failed")
            return False

    def _select_case_type(self):
        """选择案件类型"""
        try:
            # 点击案件类型下拉框
            if not self._click_element(CasePage.case_type_dropdown, "案件类型下拉框"):
                return False

            # 选择民事案件
            if not self._click_element(CasePage.civil_case_option, "民事案件选项"):
                return False

            # 选择民事一审
            if not self._click_element(CasePage.civil_case_option2, "民事一审选项"):
                return False

            logger.info(f"{self.current_time} - {self.current_user} - 选择案件类型成功")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 选择案件类型失败: {str(e)}")
            self._take_screenshot("select_case_type_failed")
            return False

    def _select_case_reason(self):
        """选择案由类型"""
        try:
            # 点击案由选择框
            if not self._click_element(CasePage.reason_select, "案由选择框"):
                return False

            # 选择行政案由
            if not self._click_element(CasePage.admin_case_option, "行政案由选项"):
                return False

            logger.info(f"{self.current_time} - {self.current_user} - 选择案由类型成功")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 选择案由类型失败: {str(e)}")
            self._take_screenshot("select_case_reason_failed")
            return False

    def _input_original_case_number(self, case_number):
        """输入原审案号"""
        try:
            # 点击原审案号输入框
            if not self._click_element(CasePage.original_case_input, "原审案号输入框"):
                return False

            # 输入原审案号
            if not self._input_text(CasePage.original_case_field, case_number, "原审案号"):
                return False

            logger.info(f"{self.current_time} - {self.current_user} - 输入原审案号成功")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 输入原审案号失败: {str(e)}")
            self._take_screenshot("input_original_case_number_failed")
            return False

    def _select_filing_date(self):
        """选择立案日期"""
        try:
            # 点击日期输入框
            if not self._click_element(CasePage.date_input, "日期输入框"):
                return False

            # 选择今天
            if not self._click_element(CasePage.today_option, "今天选项"):
                return False

            logger.info(f"{self.current_time} - {self.current_user} - 选择立案日期成功")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 选择立案日期失败: {str(e)}")
            self._take_screenshot("select_filing_date_failed")
            return False

    @allure.step("编辑案件: {case_name}")
    def edit_case(self, case_name):
        """编辑案件流程"""
        try:
            # 定位编辑按钮
            edit_locator = (By.XPATH, f"//td[@title='{case_name}']/ancestor::tr/td[11]/div/div[3]//*[name()='svg']")

            # 点击编辑按钮
            with allure.step("点击编辑按钮"):
                if not self._click_element(edit_locator, "编辑按钮"):
                    return False

            # 修改案件名称
            with allure.step("修改案件名称"):
                new_name = f"{case_name}修改"
                if not self._input_text(CasePage.case_name_input, new_name, "案件名称"):
                    return False

            # 提交修改
            with allure.step("提交修改"):
                if not self._click_element(CasePage.confirm_button, "确认按钮"):
                    return False

            logger.info(f"{self.current_time} - {self.current_user} - 案件编辑成功: {new_name}")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 案件编辑失败: {str(e)}")
            self._take_screenshot("edit_case_failed")
            return False

    @allure.step("删除案件: {case_number}")
    def delete_case(self, case_number):
        """删除案件流程"""
        try:
            # 定位删除按钮
            delete_locator = (By.XPATH, f"//td[@title='{case_number}']/ancestor::tr/td[11]/div/div[4]//*[name()='svg']")

            # 点击删除按钮
            with allure.step("点击删除按钮"):
                if not self._click_element(delete_locator, "删除按钮"):
                    return False

            # 确认删除
            with allure.step("确认删除"):
                if not self._click_element(CasePage.confirm_button, "确认删除"):
                    return False

            logger.info(f"{self.current_time} - {self.current_user} - 案件删除成功: {case_number}")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 案件删除失败: {str(e)}")
            self._take_screenshot("delete_case_failed")
            return False