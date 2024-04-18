import random

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from library.locators import *
from library.PO.Common import Common


class Products(Common):

    @keyword("user add ${number} product/s to cart")
    def add_product_to_cart(self, number: int):
        self.wait_for_text_element(CommonLocators.title, 'Products')
        if self.are_elements_overlapping(ProductsPage.go_to_cart, ProductsPage.header_container):
            BuiltIn().fail('Visual bug, items in the header of the page are overlapping!')
        # Make number a global variable to be used also in other modules
        self.make_number_common(number)
        # Click add to cart for a number of random items
        items = self.get_webelements(CommonLocators.items)
        for i in range(self.number):
            item = random.choice(items)
            items = self.remove_element_from_list(items, item)
            self.click_on_child_element(item, ProductsPage.add_to_cart_button)
        self.proceed_to_cart()

    def proceed_to_cart(self):
        self.click_element(ProductsPage.go_to_cart)






