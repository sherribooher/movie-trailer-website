import webbrowser
"""Imports the webbrowser module"""


# Create the main class.
class Movie():
    """This class provides a way to store information about movies"""

    # Initialize the class.

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url,
                 movie_storyline, movie_duration):
        """Initializes the Movie class with the parameters given in parentheses.
        Attributes:
            movie_title: A string that supplies the movie's title
            poster_image_url: A URL that provides the movie's poster artwork
            trailer_youtube_url: A URL that will provide the movie's trailer
            movie_storyline: A string that describes the movie's plot
            movie_duration: A number that represents the movie's running time
        """

        self.movie_title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.movie_storyline = movie_storyline
        self.movie_duration = movie_duration

    # Create function to play the movie trailer from YouTube.
    def show_trailer(self):
        """Function that allows the movie's YouTube trailer to be viewed in the
        webbrowser
        """
        webbrowser.open(self.trailer_youtube_url)
