from concurrent.futures import ThreadPoolExecutor, TimeoutError
from selenium import webdriver
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        NoSuchElementException,
                                        StaleElementReferenceException,
                                        WebDriverException, TimeoutException)
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from robot.libraries.BuiltIn import BuiltIn


class WebLibrary:

    def open_browser(self, browser):
        self.create_driver(browser)
        self.driver.maximize_window()

    def close_browser_action(self):
        self.driver.quit()

    def create_driver(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        self.driver.find_elements()

    def navigate_to_page(self, page_url: str):
        self.driver.get(page_url)

    def element_is_visible(self, locator: tuple) -> bool:
        try:
            element = self.driver.find_element(*locator)
            if element.is_displayed():
                return True
        except:
            return False

    def get_text(self, locator: tuple):
        element = self.driver.find_element(locator)
        return element.text

    def click_element_with_timeout(self, driver, element, timeout):
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(element.click)
            try:
                # Wait for the click operation to complete within the timeout
                future.result(timeout=timeout)
            except TimeoutError:
                future.cancel()
                raise TimeoutError(f"Click operation timed out after {timeout} seconds.")

    def click_element_with_timeout_method(self, locator: tuple, timeout: int = 5):
        element = self.wait_for_presence_of_element(locator)
        self.click_element_with_timeout(self.driver, element, timeout)

    def click_element(self, locator: tuple):
        element = self.wait_for_presence_of_element(locator)
        element.click()

    def wait_for_element_to_be_clickable(self, locator: tuple, timeout: int = 3):
        try:
            # Wait for the presence of the element
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator))
            element.click()
        except:
            raise TimeoutException

    def wait_for_presence_of_element(self, locator: tuple):
        timeout = 3
        try:
            # Wait for the presence of the element
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator))
            print("Element is present on the page")
            # Return found element
            return element
        except TimeoutException:
            BuiltIn().fail("Timed out waiting for element to be present")

    def wait_for_visibility_of_element(self, locator: tuple, timeout: int = 3):
        try:
            # Wait for the visibility of the element
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            print("Element is visible on the page")
            # Return found element
            return element
        except TimeoutException:
            raise TimeoutException

    def wait_for_invisibility_of_element(self, locator: tuple, timeout: int = 3):
        try:
            # Wait for the invisibility of the element
            element = WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator))
            print("Element is invisible on the page")
            # Return found element
            return element
        except TimeoutException:
            raise TimeoutException

    def input_text(self, locator: tuple, text: str):
        input_field = self.wait_for_presence_of_element(locator)
        input_field.clear()
        input_field.send_keys(text)

    def get_webelements(self, locator: tuple) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def wait_for_text_element(self, locator: tuple, check_text: str):
        element = self.wait_for_presence_of_element(locator)
        if element.text == check_text:
            BuiltIn().log("Element with text // " + check_text + " // present in page")
        else:
            BuiltIn().fail("Element with text //  " + check_text + " // NOT present in page")

    def click_on_child_element(self, parent_element: WebElement, child_locator: tuple):
        child_element = parent_element.find_element(*child_locator)
        child_element.click()

    def are_elements_overlapping(self, locator1, locator2):
        element1 = self.driver.find_element(*locator1)
        element2 = self.driver.find_element(*locator2)
        element1_rect = element1.rect
        element2_rect = element2.rect

        if (
                (element1_rect["x"] < element2_rect["x"] + element2_rect["width"]) and
                (element1_rect["x"] + element1_rect["width"] > element2_rect["x"]) and
                (element1_rect["y"] < element2_rect["y"] + element2_rect["height"]) and
                (element1_rect["y"] + element1_rect["height"] > element2_rect["y"])
        ):
            return True
        else:
            return False


