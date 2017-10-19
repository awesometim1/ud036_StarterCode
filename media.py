import webbrowser

class Movie():


    #Initializes the Movie Object
    def __init__(self , movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Opens the trailer of the Movie object
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
