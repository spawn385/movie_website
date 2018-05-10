import fresh_tomatoes
from media import Movie


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

    movie_list = [terminator2, desperate_measures, the_other_guys]
    fresh_tomatoes.open_movies_page(movie_list)


if __name__ == "__main__":
    main()
