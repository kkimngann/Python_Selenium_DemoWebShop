from selenium.webdriver.common.by import By


class LoginForm:
    email_selector = '#Email'
    password_selector = '#Password'
    button_login_selector = 'input[class$="login-button"]'
    error_selector = '.message-error'

    def __init__(self, driver):
        self.driver = driver.driver

    def input_mail(self,email):
        email_element = self.driver.find_element(By.CSS_SELECTOR, self.email_selector)
        email_element.send_keys(email)

    def input_password(self,password):
        password_element = self.driver.find_element(By.CSS_SELECTOR, self.password_selector)
        password_element.send_keys(password)

    def select_login(self):
        button_login_element = self.driver.find_element(By.CSS_SELECTOR, self.button_login_selector)
        button_login_element.click()

    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.error_selector).text



