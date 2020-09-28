from behave import fixture, use_fixture
from selenium.webdriver import Chrome, ChromeOptions
from unittest import TestCase
import time

@fixture
def browser_firefox(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    context.driver = Chrome(chrome_options=chrome_options) #Esto lo hace en before
    #Aquí se podría poner el Login, si para todas las pruebas se necesita estar logeado
    context.url = 'http://127.0.0.1:8000/'
    #login(context)
    context.test = TestCase()
    yield context.driver # A partir de aquí, lo hace después de todo
    # -- CLEANUP-FIXTURE PART:
    #context.driver.quit()

def before_all(context):
    use_fixture(browser_firefox, context)
    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook