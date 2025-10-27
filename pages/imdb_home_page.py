import selenium.webdriver as webdriver
from pages.base_page import BasePage, By

class ImdbHomePage(BasePage):
    
    SEARCH_BAR = (By.ID, "suggestion-search")
    SEARCH_INPUT = (By.CLASS_NAME, "react-autosuggest__input--focused")
    SEARCH_BTN = (By.CLASS_NAME, "ipc-icon--magnify")

    def search_movie(self, artist_name):
        self.click(self.SEARCH_BAR)
        self.enter_text(self.SEARCH_INPUT, artist_name)
        self.click(self.SEARCH_BTN)