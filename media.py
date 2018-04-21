import webbrowser

class Movie():
    """This program contains movie information."""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    __name__ = "Movie Class"
    __module__ = "None"
#Inputs: variables given in entertainment_center to define movie information.
#Outputs: the correct movie information.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, first_week):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.earnings_first_week = first_week
#Inputs: None
#Outputs: opens a web browser with the movie trailer.
    def show_youtube_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
