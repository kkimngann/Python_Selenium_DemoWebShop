from selenium.webdriver.common.by import By


class TopMenu:
    login_link_selector = '.ico-login'
    current_user_selector = '[href="/customer/info"]'
    logout_link_selector = '.ico-logout'

    def __init__(self, driver):
        self.driver = driver.driver

    def select_login_link(self):
        element = self.driver.find_element(By.CSS_SELECTOR,self.login_link_selector)
        element.click()

    def get_current_login_user_email(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.current_user_selector).text

    def check_button_logout_exist(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, self.logout_link_selector)) > 0
