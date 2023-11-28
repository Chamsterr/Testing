import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class DriverSingleton:
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls._createInstance()
        return cls._instance

    @classmethod
    def _createInstance(cls):
        project_dir = os.path.dirname(os.getcwd())
        print(project_dir)
        download_dir = os.path.join(project_dir, 'Framework/download')

        options = Options()
        options.add_argument("--user-data-dir=profile")
        options.add_experimental_option("prefs", {"download.default_directory": download_dir})
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        return driver