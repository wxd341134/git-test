import configparser
import os


class ConfigReader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigReader, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        self.config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        self.config.read(config_path, encoding='utf-8')

    def get_url(self):
        return self.config.get('URL', 'base_url')

    def get_login_info(self):
        return {
            'username': self.config.get('LOGIN', 'username'),
            'password': self.config.get('LOGIN', 'password')
        }

    def get_browser_config(self):
        return {
            'browser_type': self.config.get('BROWSER', 'browser_type'),
            'headless': self.config.getboolean('BROWSER', 'headless'),
            'implicit_wait': self.config.getint('BROWSER', 'implicit_wait')
        }

    def get_default_case_info(self):
        return {
            'case_name': self.config.get('CASE', 'default_case_name'),
            'case_number': self.config.get('CASE', 'default_case_number')
        }