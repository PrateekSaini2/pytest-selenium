import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture(params=['Chrome', 'Firefox'], scope='function')
def setup_driver(request):
    # if request.param == 'Chrome':
    #     driver = webdriver.Chrome(
    #         service=ChromeService(
    #         ChromeDriverManager().install()
    #         ))
    #     print('Setting up Chrome')
    # if request.param == 'Firefox':
    #     driver = webdriver.Firefox(
    #         service=FirefoxService(
    #         GeckoDriverManager().install()
    #         ))
    #     print('Setting up Firefox')

    driver = webdriver.Remote(
           command_executor='http://127.0.0.1:4444/wd/hub',
           desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})

    driver.get('https://www.saucedemo.com/')
    request.cls.driver = driver
    assert 'Swag Labs' in driver.title
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield
    print('Closing driver')
    driver.close()
    print('Quitting driver')
    driver.quit()