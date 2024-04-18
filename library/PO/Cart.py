from robot.api.deco import keyword
from library.PO.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from library.locators import *


class Cart(Common):

    @keyword("verify product/s are added to cart")
    def check_number_of_products_in_cart(self):
        # Verify how many products we're added to cart
        self.wait_for_text_element(CommonLocators.title, 'Your Cart')
        items = self.get_webelements(CommonLocators.items)
        if len(items) == self.number:
            BuiltIn().log('All products are added to cart!', console=True)
        else:
            BuiltIn().fail("Not all products we're added to cart!")

    @keyword("proceed to Checkout")
    def proceed_to_checkout(self):
        self.click_element(CartPage.checkout_button)