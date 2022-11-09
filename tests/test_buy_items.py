import pytest

from core.drivers.DriverManager import DriverManager
from core.global_variables import BASE_URI
from core.pages.HeaderSection import HeaderSection
from core.pages.ItemsSection import ItemSection
from core.pages.cartSection import CartSection


@pytest.fixture(autouse=True, scope='class')
def initialize_driver():
    """
    This fixture initialize the driver before to execute class test and after quit from driver when all test of
    class was executed
    """
    DriverManager()
    yield
    DriverManager().driver.quit()


class TestUIDestinations:

    @pytest.fixture(autouse=True, scope='function')
    def go_to_home_page(self):
        DriverManager().driver.get(BASE_URI)

    def test_validate_total_amount_is_less_than_10000(self):
        """
        This test add 2 refrigerator to cart and validate total amount is less than 10000
        """
        header = HeaderSection()
        header.search_item("refrigerador")
        items = ItemSection()
        items.click_first_item_by_name('Samsung')
        items.add_to_car()
        header.go_to_dashboard()
        header.search_item("refrigerador")
        items.click_first_item_by_name('mabe')
        items.add_to_car()
        header.got_to_cart()
        cart = CartSection()
        total_mount = cart.get_total_amount().replace('$', '')
        pesos = int(total_mount.split('.')[0].replace(',', ''))
        cents = float(f".{total_mount.split('.')[1]}")
        total = pesos + cents
        expected_value = 10000
        assert total < expected_value, f"Expected total mount less than {expected_value} but actual is {total}"

    def test_validate_total_amount_is_grater_than_10000(self):
        """
        This test add 2 refrigerator to cart and validate total amount is grater than 10000
        """
        header = HeaderSection()
        header.search_item("refrigerador")
        items = ItemSection()
        items.click_first_item_by_name('Samsung')
        items.add_to_car()
        header.go_to_dashboard()
        header.search_item("refrigerador")
        items.click_first_item_by_name('mabe')
        items.add_to_car()
        header.got_to_cart()
        cart = CartSection()
        total_mount = cart.get_total_amount().replace('$', '')
        pesos = int(total_mount.split('.')[0].replace(',', ''))
        cents = float(f".{total_mount.split('.')[1]}")
        total = pesos + cents
        expected_value = 10000
        assert total > expected_value, f"expected total mount grater than {expected_value} but actual is {total}"
