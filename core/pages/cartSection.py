from core.pages.BasePage import BasePage


class CartSection(BasePage):
    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "subTotalLbl": ('ID', 'sc-subtotal-amount-buybox'),
        **BasePage.locators
    }

    def get_total_amount(self):
        return self.subTotalLbl.get_text()
