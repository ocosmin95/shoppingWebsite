from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

from library.locators import *
from library.PO.Common import Common


class LogIn(Common):

    @keyword("user logs in with credentials ${user}")
    def user_log_in(self, user: str):
        self.wait_for_presence_of_element(LogInPage.logIn_button)
        self.input_text(LogInPage.username_field, self.users[user]['username'])
        self.input_text(LogInPage.password_field, self.users[user]['password'])
        try:
            self.click_element_with_timeout_method(LogInPage.logIn_button, timeout=2)
        except:
            BuiltIn().fail('Takes to much time for user to be logged in! Perfomance issue!')
        try:
            self.wait_for_invisibility_of_element(CommonLocators.error_message)
        except:
            BuiltIn().fail('User cannot login!')






