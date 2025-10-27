import selenium.webdriver as webdriver
from pages.base_page import BasePage, By

class ImdbResultPage(BasePage):
    MOVIE_INFO = (By.CLASS_NAME, "ipc-metadata-list-summary-item__t")
    def press_link(self):
        self.click(self.MOVIE_INFO)
