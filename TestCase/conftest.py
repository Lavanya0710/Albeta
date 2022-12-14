import chromedriver_autoinstaller
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()))
    return driver

# from webdriver_manager.firefox import GeckoDriverManager
#
#
# @pytest.fixture()
# def setup(browser):
#     if browser=="chrome":
#         driver=webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()))
#     elif browser=="firefox":
#         driver= webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#     return driver
#
# ###give browser name from command line
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# #fetch the browser name and send to setup method
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

# -----------------------------PyTest HTML REPORT-------------------------------------------
def pytest_configure(config):
    config._metadata['Project Name'] = 'Alberta'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Lavanya'

@pytest.mark.optionhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)