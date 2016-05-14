import webbrowser


class Movie():
    """ ... Movie() Docstring ...
    the movie class takes the movie information provided by
    entertainment_center.py and assigns the variables.
    """
    def __init__(self,
                 movie_title,
                 release_year,
                 cast,
                 movie_storyline,
                 poster_image,
                 trailer):
        """ ... Construct Docstring ...
        Create instance of movie object with additional data
        assign data to variables to be pulled later while creating 
        the web page
        """
        self.title = movie_title
        self.year = release_year
        self.cast = cast
        self.storyline = movie_storyline
        self.trailer = trailer
        self.poster = poster_image

    def show_trailer(self):
        # open the movie trailer when the poster is clicked on
        webbrowser.open(self.trailer)
