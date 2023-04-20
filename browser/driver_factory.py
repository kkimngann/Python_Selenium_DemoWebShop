from selenium import webdriver


class Driver:
    def __init__(self, browser_name):
        self.driver = None
        self.browser_name = browser_name
        if self.driver is None:
            self.driver = self.new_driver()

    def new_driver(self):
        global driver

        GRID_HUB = 'http://10.182.100.48:4444/wd/hub'
        if self.browser_name == 'chrome':
            driver = webdriver.Remote(
                command_executor=GRID_HUB,
                options=webdriver.ChromeOptions()
            )

        if self.browser_name == 'firefox':
            driver = webdriver.Remote(
                command_executor=GRID_HUB,
                options=webdriver.FirefoxOptions()
            )

        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver

