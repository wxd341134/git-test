import pytest
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger2 import Logger
from common.driver_manager import DriverManager

# 确保当前目录在 Python 路径中
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

logger = Logger().get_logger()

# 保存WebDriver实例
_driver = None


# 检查是否通过命令行直接提供了参数，仅在直接调用pytest时注册这些选项
def pytest_addoption(parser):
    # 检查这些选项是否已经被添加，避免重复添加
    if not any(opt.startswith('--browser') for opt in sys.argv):
        parser.addoption("--browser", action="store", default="chrome", help="指定浏览器")

    if not any(opt.startswith('--headless') for opt in sys.argv):
        parser.addoption("--headless", action="store", default="false", help="是否使用无头模式")

    # 这个选项 run_tests.py 中没有定义，应该是安全的
    parser.addoption("--no-login-for-casemg", action="store_true", default=False,
                     help="执行CaseMg测试时不重新登录")

    # 添加URL选项
    if not any(opt.startswith('--url') for opt in sys.argv):
        parser.addoption("--url", action="store", default="http://localhost", help="测试URL")


# 增加超时设置
def pytest_configure(config):
    config.option.timeout = 300  # 设置超时时间为300秒


@pytest.fixture(scope="session")
def base_url(request):
    try:
        return request.config.getoption("--url")
    except:
        return "http://localhost"  # 默认URL


@pytest.fixture(scope="session")
def driver():
    """提供WebDriver实例"""
    try:
        # 不再强制关闭已有的Chrome进程
        logger.info("开始初始化WebDriver...")
        driver = DriverManager.get_driver()

        # 验证driver是否正常工作
        try:
            driver.current_url
            logger.info("WebDriver实例验证成功")
        except Exception as e:
            logger.error(f"WebDriver实例验证失败: {str(e)}")
            raise

        yield driver

    except Exception as e:
        logger.error(f"Driver fixture 失败: {str(e)}")
        raise


@pytest.fixture
def need_login(request):
    """确定测试是否需要登录"""
    # 获取当前测试类名
    test_class = request.cls.__name__ if request.cls else ""

    # 如果先执行了用户中心测试，案件管理测试不需要重新登录
    if test_class == "TestCaseManagement" and hasattr(request.session, "logged_in"):
        return False

    # 记录已登录状态
    if test_class == "TestPersonalCenter":
        request.session.logged_in = True

    return True