import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ")


@pytest.fixture(scope="function")
def browser(request):
    user_lang = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield browser
    print("\nquit browser..")
    time.sleep(2)
    browser.quit()
