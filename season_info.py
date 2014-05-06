class season_info:
    season_number = 0
    episode_name = []
    episode_overview = []
    episode_airdate = []
    
    def print_all(self):
        for i in range(0,len(self.episode_name)):
            print('Episode: ',i+1)
            print('Title: ',self.episode_name[i])
            print('Air date: ',self.episode_airdate[i])
            print('Overview: ',self.episode_overview[i])