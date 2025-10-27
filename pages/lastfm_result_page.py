import selenium.webdriver as webdriver
from pages.base_page import BasePage, By

class LastFmResultPage(BasePage):
    ARTIST_LINK = (By.CLASS_NAME, "link-block-target")
    def press_link(self):
        self.click(self.ARTIST_LINK)
