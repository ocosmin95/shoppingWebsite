from library.PO.LogIn import LogIn
from library.PO.Common import Common
from library.PO.Products import Products
from library.PO.Cart import Cart
from library.PO.CheckoutOverview import CheckoutOverview
from library.PO.CheckoutInformation import CheckoutInformation
from library.PO.CheckoutComplete import CheckoutComplete


class AppLibrary(LogIn, Products, Cart, CheckoutInformation, CheckoutOverview, CheckoutComplete):
    pass
