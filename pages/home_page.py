from component.top_menu_component import TopMenu


class HomePage:
    def __init__(self ,driver):
        self.driver = driver
        self.top_menu = TopMenu(self.driver)

    def select_login(self):
        self.top_menu.select_login_link()