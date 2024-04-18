from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

from library.locators import *
from library.PO.Common import Common


class CheckoutOverview(Common):

    @keyword("verify checkout overview page")
    def verify_checkout_information(self, negative: bool = False):
        self.wait_for_text_element(CommonLocators.title, 'Checkout: Overview')
        # Verify how many products are present in overview page
        items = self.get_webelements(CommonLocators.items)
        if len(items) == self.number:
            BuiltIn().log('All products are present in checkout page!', console=True)
        else:
            BuiltIn().fail("Not all products are present in checkout page!")
        # Verify billing information
        self.wait_for_text_element(CheckoutOverviewPage.payment_information, 'Payment Information:')
        self.wait_for_text_element(CheckoutOverviewPage.shipping_information, 'Shipping Information:')
        self.wait_for_text_element(CheckoutOverviewPage.price_total, 'Price Total')

    @keyword('finish checkout')
    def finish_checkout(self):
        self.click_element(CheckoutOverviewPage.overview_finish)

