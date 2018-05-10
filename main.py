import fresh_tomatoes 
from movie import Movie

def main():
    terminator2 = Movie("Terminator 2: Judgment Day", 
                       "https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg", 
                       "https://www.youtube.com/watch?v=-W8CegO_Ixw")
    desperate_measures = Movie("Desperate Measures",
                               "https://upload.wikimedia.org/wikipedia/en/a/a1/Desperate_measures.jpg",
                               "https://www.youtube.com/watch?v=i63VGK1ElN0")
                               
    the_other_guys = Movie("The Other Guys",
                           "https://upload.wikimedia.org/wikipedia/en/6/6b/Other_guys_poster.jpg", 
                           "https://www.youtube.com/watch?v=D6WOoUG1eNo")
                           
    the_naked_gun2 = Movie("The Naked Gun 2 1/2: The Smell of Fear",
                           "https://upload.wikimedia.org/wikipedia/en/d/d1/Naked_Gun_2.jpg",
                           "https://www.youtube.com/watch?v=H4RssRXLWhQ")
                           
    superbad = Movie("Superbad",
                     "https://upload.wikimedia.org/wikipedia/en/8/8b/Superbad_Poster.png",
                     "https://www.youtube.com/watch?v=zFjaJbihWwc")
                     
    hot_fuzz = Movie("Hot Fuzz",
                     "https://upload.wikimedia.org/wikipedia/en/c/c9/HotFuzzUKposter.jpg",
                     "https://www.youtube.com/watch?v=ayTnvVpj9t4")
                     
    eraser = Movie("Eraser",
                   "https://upload.wikimedia.org/wikipedia/en/2/2c/Eraser_%28movie_poster%29.jpg",
                   "https://www.youtube.com/watch?v=31_OEhX30sY")
                           
    movie_list = [terminator2, desperate_measures, the_other_guys, the_naked_gun2, superbad, hot_fuzz, eraser]
    fresh_tomatoes.open_movies_page(movie_list)
    

if __name__ == "__main__":
    main()
