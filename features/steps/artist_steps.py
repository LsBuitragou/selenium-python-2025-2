from behave import given, when, then
from selenium import webdriver
from pages.lastfm_home_page import LastfmHomePage
from pages.lastfm_result_page import LastFmResultPage
from pages.lastfm_artist_page import ArtistPage


@given('el usuario está en el home page de last.fm')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.last.fm/")
    context.lastfm_home = LastfmHomePage(context.driver)
    

@when('el usuario busca al artista "{artist_name}"')
def step_search_page(context, artist_name):
    context.lastfm_home.search_artist(artist_name)
    context.lastfm_result = LastFmResultPage(context.driver)

@when('presiona el link del primer resultado')
def step_press_link(context):
    
    context.lastfm_result.press_link()
    context.lastfm_artist = ArtistPage(context.driver)

@then('la fecha del ultimo release debe ser "{expected_date}"')
def step_compare_dates(context, expected_date):
    actual_date = context.lastfm_artist.get_latest_release_date()
    assert actual_date == expected_date, f"Expected {expected_date}, but got {actual_date}"
    context.driver.quit()
