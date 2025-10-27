Feature: Buscar una pelicula en imdb y validar su titulo y calificación
    Scenario: Validar el titulo y calificación de la pelicula "Barbie"
        Given el usuario está en el home page de imdb.com
        When el usuario busca la pelicula "Barbie"
        And presiona el link de la primera pelicula
        Then el titulo del resultado debe ser "Barbie"
        And la calificación debe ser "6,8"