from core.pages.BasePage import BasePage


class HeaderSection(BasePage):
    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "searchInput": ('ID', 'twotabsearchtextbox'),
        "searchBtn": ('ID', 'nav-search-submit-button'),
        "logoBtn": ('XPATH', '//a[@href="/ref=nav_logo"]'),
        "cartBtn": ('ID', 'nav-cart'),
        **BasePage.locators
    }

    def search_item(self, item_name):
        """
        This method logout when a user is logout in page
        """
        self.searchInput.set_text(item_name)
        self.searchBtn.click_button()

    def go_to_dashboard(self):
        self.logoBtn.click_button()

    def got_to_cart(self):
        self.cartBtn.click_button()
