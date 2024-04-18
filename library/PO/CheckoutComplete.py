from robot.api.deco import keyword
from library.locators import *
from library.PO.Common import Common
from robot.libraries.BuiltIn import BuiltIn


class CheckoutComplete(Common):

    @keyword('verify checkout was successful')
    def verify_successful_checkout(self):
        self.wait_for_text_element(CommonLocators.title, 'Checkout: Complete!')
        BuiltIn().log('Checkout was completed successfully!', console=True)
