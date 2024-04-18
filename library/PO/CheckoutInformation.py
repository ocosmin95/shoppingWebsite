import random

from robot.api.deco import keyword
from library.locators import *
from library.PO.Common import Common
from robot.libraries.BuiltIn import BuiltIn


class CheckoutInformation(Common):

    @keyword("complete user information")
    def complete_user_information(self, negative: bool = False):
        self.wait_for_text_element(CommonLocators.title, 'Checkout: Your Information')
        if negative:
            # workflow for negative test case
            user = 'negative'
        else:
            # get random user
            user = 'user'+str(random.randint(1, 5))
        # add user info
        self.input_text(CheckoutInformationPage.information_first_name, self.user_information[user]['first_name'])
        self.input_text(CheckoutInformationPage.information_last_name, self.user_information[user]['last_name'])
        self.input_text(CheckoutInformationPage.information_zip_code, self.user_information[user]['zip_code'])

    @keyword("complete user information in negative scenario")
    def complete_user_negative_scenario(self):
        self.complete_user_information(negative=True)

    @keyword("verify user cannot pass checkout information step")
    def verify_error_message_your_information_form(self):
        try:
            self.wait_for_visibility_of_element(CommonLocators.error_message)
        except:
            BuiltIn().fail('Error message present when filling you information form!')

    @keyword('continue to checkout')
    def continue_checkout(self):
        self.click_element(CheckoutInformationPage.information_continue_button)
        if self.element_is_visible(CommonLocators.error_message):
            BuiltIn().fail('Error message displayed after completing Your Information fields!')



