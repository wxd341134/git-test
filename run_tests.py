import os
import sys  # 添加sys模块导入
import subprocess
import argparse
import time
from utils.logger2 import Logger
import pytest

logger = Logger().get_logger()

import pytest
import os
import shutil

def run_tests():
    try:
        # 清理并创建结果目录
        results_dir = os.path.join(os.path.dirname(__file__), 'allure-results')
        if os.path.exists(results_dir):
            shutil.rmtree(results_dir)
        os.makedirs(results_dir)

        # 运行测试
        pytest.main([
            f'test_001/test_UserCenter.py',
            f'test_001/test_DossierUp.py',
            # f'tests/test_CaseMg.py',
            f'test_001/test_AssistedG.py',
            '-v',
            '--alluredir', results_dir
        ])

        # 生成报告
        report_dir = os.path.join(os.path.dirname(__file__), 'allure-report')
        os.system(f'allure generate {results_dir} -o {report_dir} --clean')
        #os.system(f'allure open {report_dir}')  #自动打开报告

    except Exception as e:
        logger.error(f"测试执行失败: {e}")
        raise

if __name__ == '__main__':
    # 选择要运行的测试文件
    run_tests()