from seleniumpagefactory.Pagefactory import PageFactory

from core.drivers.DriverManager import DriverManager
from core.global_variables import EXPLICIT_WAIT


class BasePage(PageFactory):

    def __init__(self, driverManager=DriverManager(), timeout=EXPLICIT_WAIT):
        super().__init__()
        self.driver = driverManager.driver
        self.timeout = timeout

    locators = {
    }
