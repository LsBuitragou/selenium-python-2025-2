from behave import given, when, then
from selenium import webdriver
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_result_page import ImdbResultPage
from pages.imdb_movie_page import ImdbMoviePage

@given('el usuario está en el home page de imdb.com')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")
    context.imdb_home = ImdbHomePage(context.driver)

@when('el usuario busca la pelicula "{movie_name}"')
def step_search_page(context, movie_name):
    context.imdb_home.search_movie(movie_name)
    context.imdb_result = ImdbResultPage(context.driver)

@when('presiona el link de la primera pelicula')
def step_press_link(context):
    context.imdb_result.press_link()
    context.imdb_movie = ImdbMoviePage(context.driver)

@then('el titulo del resultado debe ser "{expected_title}"')
def step_compare_title(context, expected_title):
    actual_title = context.imdb_movie.get_movie_name()
    assert actual_title == expected_title, f"Expected {expected_title}, but got {actual_title}"

@then('la calificación debe ser "{expected_rating}"')
def step_compare_rating(context, expected_rating):
    actual_rating = context.imdb_movie.get_movie_rating()
    assert actual_rating == expected_rating, f"Expected {expected_rating}, but got {actual_rating}"
    context.driver.quit()
