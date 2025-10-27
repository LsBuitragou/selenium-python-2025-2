Feature: Buscar un artista en last.fm y validar la fecha de su ultimo release
    Scenario: Validar la fecha de ultimo release de Michael Jackson
        Given el usuario está en el home page de last.fm
        When el usuario busca al artista "Michael Jackson"
        And presiona el link del primer resultado
        Then la fecha del ultimo release debe ser "30 September 2025"