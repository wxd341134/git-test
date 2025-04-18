import logging
import os
from datetime import datetime
import yaml
from appium import webdriver

class Logger:
    def __init__(self):
        # 创建logger
        self.logger = logging.getLogger('MessageTest')
        self.logger.setLevel(logging.INFO)

        # 检查是否已有处理器，避免重复添加
        if not self.logger.hasHandlers():
            # 创建handler
            log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            log_file = os.path.join(log_dir, f'test_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
            fh = logging.FileHandler(log_file, encoding='utf-8')
            ch = logging.StreamHandler()

            # 设置格式
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger


# 创建全局logger实例
logger = Logger().get_logger()