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
        print(self.title)
        print(self.duration)
        print(self.genre)
        print(self.rating)
        print(self.description)
        print(self.actors)