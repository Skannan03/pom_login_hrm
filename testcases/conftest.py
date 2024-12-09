import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Specify the browser to run tests: chrome, firefox, or edge"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser").lower()

    if browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser: choose from 'chrome', 'firefox', or 'edge'")

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Wait until the page loads (use WebDriverWait for a better approach)
    request.cls.driver = driver
    yield driver
    driver.quit()
