import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru, en',  # или default=None,
                     help='Language')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption('language')
    print(f'\nStart browser {browser_name} for test..')
    if browser_name == "firefox":
        options = Options()
        options.set_preference("intl.accept_languages", language)
        browser = Firefox(options=options)
    else:
        if browser_name != 'Chrome':
            print(f'\nDriver {browser_name} not found!')
            print('\nStart default browser Chrome for test..')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()