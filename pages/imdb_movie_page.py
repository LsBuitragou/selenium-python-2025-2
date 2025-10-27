import selenium.webdriver as webdriver
from pages.base_page import BasePage, By

class ImdbMoviePage(BasePage):
    MOVIE_NAME = (By.CLASS_NAME, "hero__primary-text")
    MOVIE_RATING = (By.CLASS_NAME, "lbQcRY")

    def get_movie_name(self):
        return self.find_element(self.MOVIE_NAME).text
    def get_movie_rating(self):
        return self.find_element(self.MOVIE_RATING).text