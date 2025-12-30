import undetected_chromedriver as uc
import pytest
from selenium import webdriver
from utilities.customLogger import CustomLogger

logger = CustomLogger.setup_logger()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "edge"],
        help="Browser option: chrome, firefox, edge"
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser_name")

@pytest.fixture()
def setup(browser):
    driver = None

    if browser == "chrome":
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        # options.add_argument("--disable-extensions")
        # options.add_argument("--headless=new")  # Optional: run in headless mode
        logger.info("Launching Chrome browser with UC")
        driver = uc.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        # options.add_argument("--headless")  # Optional: run in headless mode
        logger.info("Launching Firefox browser")
        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        # options.add_argument("--headless=new")  # Optional: run in headless mode
        logger.info("Launching Edge browser")
        driver = webdriver.Edge(options=options)

    else:
        logger.warning(f"Unknown browser '{browser}', defaulting to Chrome")
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        # options.add_argument("--disable-extensions")
        # options.add_argument("--headless=new")  # Optional: run in headless mode
        driver = uc.Chrome(options=options)

    return driver

### Pytest HTML Report Configuration ###

# ADD environment info to the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    # ADD custom metadata
    metadata["Project Name"] = "Web Automation Testing"
    metadata["Module Name"] = "Customer"
    metadata["Tester"] = "Mrunal"

    # REMOVE unwanted metadata
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)

    logger.info("Updated pytest HTML report metadata")