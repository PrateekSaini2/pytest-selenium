import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture(scope='function')
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

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Remote(
           command_executor='http://localhost:4444/wd/hub',
           options=chrome_options)

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