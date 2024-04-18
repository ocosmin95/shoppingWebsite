from selenium.webdriver.common.by import By


class CommonLocators:
    title = (By.XPATH, '//*[@data-test="title"]')
    items = (By.XPATH, '//*[@data-test="inventory-item"]')
    error_message = (By.XPATH, '//*[@class="error-message-container error"]')


class LogInPage:
    logIn_button = (By.XPATH, '//*[@class="submit-button btn_action"]')
    username_field = (By.XPATH, '//*[@data-test="username"]')
    password_field = (By.XPATH, '//*[@data-test="password"]')


class ProductsPage:
    add_to_cart_button = (By.XPATH, './/*[@class="btn btn_primary btn_small btn_inventory "]')
    go_to_cart = (By.XPATH, '//*[@data-test="shopping-cart-link"]')
    header_container = (By.XPATH, '//*[@data-test="secondary-header"]')


class CartPage:
    checkout_button = (By.XPATH, '//*[@data-test="checkout"]')


class CheckoutInformationPage:
    information_first_name = (By.XPATH,  '//*[@data-test="firstName"]')
    information_last_name = (By.XPATH, '//*[@data-test="lastName"]')
    information_zip_code = (By.XPATH, '//*[@data-test="postalCode"]')
    information_continue_button = (By.XPATH, '//*[@data-test="continue"]')


class CheckoutOverviewPage:
    payment_information = (By.XPATH, '//*[@data-test="payment-info-label"]')
    shipping_information = (By.XPATH, '//*[@data-test="shipping-info-label"]')
    price_total = (By.XPATH, '//*[@data-test="total-info-label"]')
    overview_finish = (By.XPATH, '//*[@data-test="finish"]')

