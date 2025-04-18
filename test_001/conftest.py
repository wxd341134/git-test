import pytest

@pytest.fixture(scope="session")
def browser_type():
    """在conftest.py中覆盖浏览器类型设置"""
    return "chrome"  # 可以根据需要修改为其他浏览器