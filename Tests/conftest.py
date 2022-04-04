import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        s = Service(TestData.CHROME_EXECUTABLE_PATH)
        web_driver = webdriver.Chrome(service=s)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()
