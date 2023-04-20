from component.login_form_component import LoginForm


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.login_form = LoginForm(self.driver)

    def login_flow(self, email, password):
        self.login_form.input_mail(email)
        self.login_form.input_password(password)
        self.login_form.select_login()

