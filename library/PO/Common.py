import yaml

from robot.api.deco import keyword

from library.WebLibrary import WebLibrary


class Common(WebLibrary):
    def __init__(self):
        self.website_link = yaml.load(open("resources/webpages.yaml"), Loader=yaml.FullLoader)
        self.users = yaml.load(open("resources/users.yaml"), Loader=yaml.FullLoader)
        self.user_information = yaml.load(open("resources/users_information.yaml"), Loader=yaml.FullLoader)
        self.number = 0

    @keyword("user navigate to webpage in ${browser}")
    def test(self, browser: str):
        self.open_browser(browser)
        self.website_link = yaml.load(open("resources/webpages.yaml"), Loader=yaml.FullLoader)
        self.navigate_to_page(self.website_link['test_env']['Saucedemo']['url'])

    @keyword('Close browser')
    def close_browser(self):
        self.close_browser_action()

    def remove_element_from_list(self, elements_list, element_to_remove):
        return [element for element in elements_list if element != element_to_remove]

    def make_number_common(self, number):
        self.number = number





