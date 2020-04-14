import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru", help="Choose language: es")
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    user_language = request.config.getoption("--language")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()   
    
