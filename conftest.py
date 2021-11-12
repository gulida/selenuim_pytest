import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language_name', action='store', default=None,
                     help='Choose language: es or en or fr')

@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language_name")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_name })
    print("\nStart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser..")
    browser.quit()