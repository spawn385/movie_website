

class Movie():
    '''This class represents a movie that is available for you to watch.
       title: title of the movie
       poster_image_url: Url link to the movie's poster image
       trailer_youtube_url: Url link to the youtube's trailer '''
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
