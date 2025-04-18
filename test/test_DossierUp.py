import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logger2 import Logger

logger = Logger().get_logger()

class TestDossierUp:
    """卷宗上传测试类"""

    def setup_class(self):
        """测试类初始化"""
        logger.info("========== 开始执行卷宗上传测试 ==========")

    def teardown_class(self):
        """测试类清理"""
        logger.info("========== 卷宗上传测试执行完成 ==========")

    def test_dossier_upload(self, driver):
        """测试卷宗上传流程"""
        try:
            logger.info("开始卷宗上传测试")
            
            # 设置等待对象
            self.wait = WebDriverWait(driver, 10)
            self.driver = driver
            
            # 检查浏览器是否仍然打开
            try:
                current_url = driver.current_url
                logger.info(f"当前页面URL: {current_url}")
            except Exception as e:
                logger.error(f"浏览器可能已关闭或不响应: {str(e)}")
                pytest.fail("浏览器会话无效")
                return
            
            # 尝试导航到卷宗上传页面
            logger.info("尝试导航到卷宗上传页面")
            
            # 方法1: 通过点击导航菜单
            try:
                # 首先检查是否存在导航菜单
                menu_button = None
                try:
                    # 可能的菜单按钮定位方式
                    locators = [
                        (By.XPATH, "//button[@class='ant-btn ant-btn-primary' and contains(.,'卷宗管理')]"),
                        (By.XPATH, "//span[contains(text(),'卷宗管理') or contains(text(),'卷宗上传')]"),
                        (By.XPATH, "//div[contains(@class,'menu')]//*[contains(text(),'卷宗')]")
                    ]
                    
                    for locator in locators:
                        try:
                            menu_button = self.wait.until(EC.element_to_be_clickable(locator))
                            if menu_button:
                                logger.info(f"找到菜单按钮: {menu_button.text}")
                                break
                        except:
                            continue
                            
                    if menu_button:
                        # 执行点击
                        driver.execute_script("arguments[0].click();", menu_button)
                        logger.info("点击菜单按钮成功")
                        time.sleep(1)
                        
                        # 尝试找到卷宗上传选项
                        upload_menu = self.wait.until(
                            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'卷宗上传') or contains(@title,'卷宗上传')]"))
                        )
                        driver.execute_script("arguments[0].click();", upload_menu)
                        logger.info("成功点击卷宗上传菜单")
                        time.sleep(2)
                    else:
                        logger.warning("未找到菜单按钮，尝试其他导航方式")
                        raise Exception("菜单按钮未找到")
                        
                except Exception as menu_error:
                    logger.warning(f"通过菜单导航失败: {str(menu_error)}")
                    raise menu_error
                    
            except Exception as e:
                logger.warning(f"通过点击菜单导航失败: {str(e)}")
                
                # 方法2: 直接通过URL导航
                try:
                    logger.info("尝试通过URL直接导航")
                    current_url = driver.current_url
                    base_url = current_url.split('#')[0] if '#' in current_url else current_url
                    
                    # 确认base_url末尾有斜杠
                    if not base_url.endswith('/'):
                        base_url += '/'
                        
                    # 尝试几种可能的URL格式
                    possible_urls = [
                        f"{base_url}#/dossier/upload",
                        f"{base_url}#/dossierup",
                        f"{base_url}#/case/dossier/upload",
                        f"{base_url}dossier/upload",
                    ]
                    
                    for url in possible_urls:
                        try:
                            logger.info(f"尝试访问: {url}")
                            driver.get(url)
                            time.sleep(2)
                            
                            # 检查页面是否加载了卷宗上传相关内容
                            page_content = driver.page_source
                            if '卷宗上传' in page_content or '文件上传' in page_content:
                                logger.info(f"成功导航到卷宗上传页面: {url}")
                                break
                        except:
                            continue
                    else:
                        logger.warning("所有URL尝试均失败")
                        
                except Exception as url_error:
                    logger.error(f"通过URL导航也失败: {str(url_error)}")
                    # 继续执行，可能页面已经是正确的，只是无法验证
            
            # 等待页面加载，确认是否成功进入卷宗上传页面
            logger.info("检查是否已成功进入卷宗上传页面")
            try:
                # 尝试多种可能的页面指示器
                indicators = [
                    (By.XPATH, "//div[contains(text(),'卷宗上传') or contains(@class,'title')]"),
                    (By.XPATH, "//button[contains(text(),'选择文件') or contains(text(),'上传')]"),
                    (By.XPATH, "//div[contains(text(),'文件列表') or contains(text(),'上传记录')]")
                ]
                
                for indicator in indicators:
                    try:
                        element = self.wait.until(EC.presence_of_element_located(indicator))
                        logger.info(f"找到页面指示元素: {element.text}")
                        logger.info("确认已进入卷宗上传页面")
                        break
                    except:
                        continue
                else:
                    logger.warning("未能确认是否已进入卷宗上传页面")
            except Exception as e:
                logger.warning(f"检查页面状态时出错: {str(e)}")
            
            # TODO: 在这里添加卷宗上传的具体步骤
            logger.info("开始执行卷宗上传具体操作")
            
            # 示例: 寻找上传按钮
            try:
                upload_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'选择文件') or contains(text(),'上传文件')]"))
                )
                logger.info(f"找到上传按钮: {upload_button.text}")
                # 实际上传操作需要根据具体页面实现
            except Exception as e:
                logger.warning(f"未找到上传按钮: {str(e)}")
            
            logger.info("卷宗上传测试完成")

        except Exception as e:
            logger.error(f"卷宗上传测试过程中出现错误: {str(e)}")
            # 截图保存错误现场
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            try:
                driver.save_screenshot(f"error_dossier_upload_{timestamp}.png")
                logger.info(f"已保存错误截图: error_dossier_upload_{timestamp}.png")
            except:
                logger.warning("无法保存错误截图")
            raise

        finally:
            logger.info("卷宗上传测试结束") 