class JSONAttributes:
    title = ''
    duration = ''
    genre = []
    rating= 0.0
    description = ''
    actors = []
    
    def __init__(self):
        self.title = ''
        self.duration = ''
        self.genre = []
        self.rating = 0.0
        self.description = ''
        self.actors = []
        
    def print_all(self):
        print("Title: ",self.title)
        print("Duration: ",self.duration)
        print("Genre: ",self.genre)
        print("Rating: ",self.rating)
        print("Description: ",self.description)
        print("Actors: ",self.actors)