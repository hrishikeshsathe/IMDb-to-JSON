from bs4 import BeautifulSoup
import requests
import json_attributes

# function to get content from the url in text form using the 'requests' api. 
# cannot use BeautifulSoup as it is not an HTTPClient
# accepts url and returns HTML code as a string
def get_content(url):
    r = requests.get(url)
    return r.text

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

#get the HTML code which gives an overview of the show/movie
start_index = content.find("overview-top")
end_index = content.find("overview-bottom")

#pass it to soup
soup = BeautifulSoup(content[start_index:end_index])

#create json object. check class JSONAttributes(). it just contains variables to store values
json = json_attributes.JSONAttributes()

#get the time tag. i.e. the duration of the show
tag = soup.time

#get the genre of the show/movie
genre=soup.findAll(itemprop='genre')

#get the rating of the show/movie
rating = soup.find(name='div',attrs={'class','star-box-giga-star'})

#get a short description of the show/movie
description = soup.find(itemprop='description')

#get the show/movie title and a short cast list
names = soup.findAll(itemprop='name')

#set the values in the json object
json.duration = tag.text.strip()
for item in genre:
    json.genre.append(item.text)
json.rating = rating.text.strip()
json.description = description.text.strip()
json.title = names[0].text
for i in range(1,len(names)):
    json.actors.append(names[i].text)

print("Overview info:-")
json.print_all()





