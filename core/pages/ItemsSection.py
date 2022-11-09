import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.global_variables import EXPLICIT_WAIT
from core.pages.BasePage import BasePage


class ItemSection(BasePage):
    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "cartBtn": ('ID', 'add-to-cart-button'),
        "dontAddProtectionBtn": ('XPATH', '//span[@id="attachSiNoCoverage-announce"]//preceding-sibling::input'),
        **BasePage.locators
    }

    def click_first_item_by_name(self, item_name):
        element_xpath = f'//div[contains(@class,"s-card-container")]//child::span[contains(text(), "{item_name}")][1]'
        element = self.driver.find_element(By.XPATH, element_xpath)
        WebDriverWait(self.driver, EXPLICIT_WAIT).until(
            EC.element_to_be_clickable(element))
        element.click()

    def add_to_car(self):
        self.cartBtn.click_button()
        self.dontAddProtectionBtn.click_button()
        time.sleep(2)
