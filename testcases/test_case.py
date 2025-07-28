import pytest
from pages.login_page import LoginPage
from pages.caseMg_page import CasePage
import yaml
import time

def load_config():
    with open('config/config.ini', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestCaseManagement:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.config = load_config()

    def test_create_and_edit_case(self, driver):
        """测试创建并修改案件"""
        try:
            # 登录
            login_page = LoginPage(driver)
            login_page.login(
                self.config['credentials']['username'],
                self.config['credentials']['password']
            )

            # 创建新案件
            case_page = CasePage(driver)
            case_name = "(2025)苏0105民初0001号"
            case_page.create_new_case(case_name, case_name)

            # 修改刚创建的案件
            new_case_name = f"{case_name}修改"
            case_page.edit_case(new_case_name)

        except Exception as e:
            pytest.fail(f"Test failed: {str(e)}")