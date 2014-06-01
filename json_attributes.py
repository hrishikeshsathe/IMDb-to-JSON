
class JSONAttributes:
    title = ''
    duration = ''
    genre = []
    rating= 0.0
    description = ''
    actors = []
    seasons = []
    director = ''
    creators = []
    def __init__(self):
        self.title = ''
        self.duration = ''
        self.genre = []
        self.rating = 0.0
        self.description = ''
        self.actors = []
        self.director = ''
        self.creators = []
        
    def print_overview(self):
        print("Title: ",self.title)
        print("Duration: ",self.duration)
        print("Genre: ",self.genre)
        print("Rating: ",self.rating)
        print("Description: ",self.description)
        print("Creators: ",self.creators)
        print("Director: ",self.director)
        print("Actors: ",self.actors)
        
    
    def print_season_info(self):
        for season in self.seasons:
            print('Season: ',season.season_number)
            for i in range(0,len(season.episode_name)):
                print('Episode: ',i+1)
                print('Title: ',season.episode_name[i])
                print('Air date: ',season.episode_airdate[i])
                print('Overview: ',season.episode_overview[i])