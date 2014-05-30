from bs4 import BeautifulSoup
from season_info import season_info
import requests
import json_attributes


#function to get content from the url in text form using the 'requests' api. 
#cannot use BeautifulSoup as it is not an HTTPClient
#accepts url and returns HTML code as a string
def get_content(url):
    r = requests.get(url)
    return r.text


#function to get the overview info as mentioned on the IMDb page
def get_overview(page_content):
    #get the HTML code which gives an overview of the show/movie
    start_index = page_content.find("overview-top")
    end_index = page_content.find("overview-bottom")
    
    #pass it to soup
    soup = BeautifulSoup(page_content[start_index:end_index])
    
    #create json object. check class JSONAttributes(). it just contains variables to store values
    json_temp = json_attributes.JSONAttributes()
    
    #get the time tag. i.e. the duration of the show
    tag = soup.time
    
    #get the genre of the show/movie
    genre=soup.findAll(itemprop='genre')
    
    #get the rating of the show/movie
    rating = soup.find(name='div',attrs={'class','star-box-giga-star'})
    
    #get a short description of the show/movie
    description = soup.find(itemprop='description')
    
    #get title of the series
    title = soup.find(itemprop='name')
    
    #get the director if its a movie
    director = soup.find(itemprop='director')
    temp_soup = BeautifulSoup(str(director))
    director = temp_soup.find('a')
    
    #get the short cast list
    temp_names = soup.findAll(itemprop='actors')
    temp_soup = BeautifulSoup(str(temp_names[0]))
    actor_names = temp_soup.findAll('a')
    
    #set the values in the json object
    json_temp.duration = tag.text.strip()
    for item in genre:
        json_temp.genre.append(item.text)
    json_temp.rating = rating.text.strip()
    json_temp.description = description.text.strip()
    json_temp.title = title.text.strip()
    if director == None:
        json_temp.director = ''
    else:
        json_temp.director = director.text.strip()
    for i in range(0,len(actor_names)-1):
        json_temp.actors.append(actor_names[i].text.strip())
    return json_temp


#get info for seasons and episodes
def get_seasons_info(page_content,json,url):
    #traverse to get the number of seasons by searching number of links in the titleTVSeries block
    start_index = page_content.find('titleTVSeries')
    page_content = page_content[start_index:-1]
    end_index = page_content.find('/div')
    soup = BeautifulSoup(page_content[:end_index])
    number_of_seasons = soup.findAll('a')
    
    # change the url and store in another variable
    # usually imdb pages for seasons are in the format http://www.imdb.com//title/title_code/episode?season=n where n is a number
    index = url.find('?')
    new_url = url[:index]
    #add the episode info to an object of season_info. add this object to the json_attributes.seasons(this is a list of seasons)
    for i in range(0,len(number_of_seasons)):
        season = season_info()
        url = new_url+'episodes?season='+str(i+1)
        season_content = get_content(url)
        soup = BeautifulSoup(season_content)
        episode_list = soup.find(name='div',attrs={'class','eplist'})
        name = episode_list.findAll(itemprop='name')
        airdate = episode_list.findAll(name='div',attrs={'class','airdate'})
        description = episode_list.findAll(itemprop='description')
        for j in range(0,len(name)):
            season.season_number = i+1
            season.episode_name.append(name[j].text.strip())
            season.episode_airdate.append(airdate[j].text.strip())
            temp_description = description[j].text.replace('"','') 
            season.episode_overview.append(temp_description.strip())
        json.seasons.append(season)
    return json

#write data into file as json object
def write_json(json):
    
    file = open(json.title+'.json','w')
    file.write('{\n')
    file.write('"title":"'+json.title+'",\n')
    file.write('"duration":"'+json.duration+'",\n')
    file.write('"genre":[')
    file.write(','.join('"'+x+'"' for x in json.genre))
    file.write('],\n')
    file.write('"rating":"'+json.rating+'",\n')
    file.write('"description":"'+json.description+'",\n')
    file.write('"director":"'+json.director+'",\n')
    file.write('"actors":[')
    file.write(','.join('"'+x+'"' for x in json.actors))
    file.write('],\n')
    file.write('"seasons":[')
    file.write(','.join('['+episode_list_as_string(season)+']\n' for season in json.seasons))
    file.write(']\n}')
    file.close()
    print('Writing done')
 
#return an episode list as string   
def episode_list_as_string(season):
    string = (',').join('\n{"number":"'+str(i+1)+
                            '","episode_title":"'+season.episode_name[i]+
                            '","airdate":"'+season.episode_airdate[i]+
                            '","episode_overview":"'+season.episode_overview[i]+'"}' 
                            for i in range(0,len(season.episode_name)))
    return string
    


# ask the user for input. user can input show name or movie name.
user_input = input("Enter the name of the movie/series to create the JSON")
url = "http://www.imdb.com/find?q="+user_input

#content will store the HTML code for the url passed. we then parse the HTML code
content = get_content(url)

#on IMDb's search result page, the first result's tag is odd. hence we find the tag which starts with findResult odd
start_index = content.find("findResult odd")
end_index = content.find("img src=")

#pass the content from start_index till end_index to soup for processing a tree structure
soup=BeautifulSoup(content[start_index:end_index])

#get the 'a' tag from the soup
tag = soup.a

#get the attribute 'href' i.e. next link from the tag
url = "http://www.imdb.com/"+tag['href']

#get content from new url which will now be the show/movie page on IMDb
content = get_content(url)

#get overview info and season+episode list
json = get_overview(content)
json = get_seasons_info(content,json,url)
write_json(json)