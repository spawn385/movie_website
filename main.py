import fresh_tomatoes
from movie import Movie


def main():
    terminator2 = Movie("Terminator 2: Judgment Day",
                        "https://goo.gl/x1z2jh",
                        "https://www.youtube.com/watch?v=-W8CegO_Ixw")

    desperate_measures = Movie("Desperate Measures",
                               "https://goo.gl/TYLtYW",
                               "https://www.youtube.com/watch?v=i63VGK1ElN0")

    the_other_guys = Movie("The Other Guys",
                           "https://goo.gl/52CCzt",
                           "https://www.youtube.com/watch?v=D6WOoUG1eNo")

    the_naked_gun2 = Movie("The Naked Gun 2 1/2: The Smell of Fear",
                           "https://goo.gl/99V6dy",
                           "https://www.youtube.com/watch?v=H4RssRXLWhQ")

    superbad = Movie("Superbad",
                     "https://goo.gl/GBjbVY",
                     "https://www.youtube.com/watch?v=zFjaJbihWwc")

    hot_fuzz = Movie("Hot Fuzz",
                     "https://goo.gl/Mth17E",
                     "https://www.youtube.com/watch?v=ayTnvVpj9t4")

    eraser = Movie("Eraser",
                   "https://goo.gl/etXiRz",
                   "https://www.youtube.com/watch?v=31_OEhX30sY")

    movie_list = [terminator2, desperate_measures, the_other_guys, 
                  the_naked_gun2, superbad, hot_fuzz, eraser]
    fresh_tomatoes.open_movies_page(movie_list)


if __name__ == "__main__":
    main()
