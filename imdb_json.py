from bs4 import BeautifulSoup
import requests
import json_attributes

def get_content(url):
    r = requests.get(url)
    return r.text


user_input = input("Enter the name of the movie/series to create the JSON")
url = "http://www.imdb.com/find?q="+user_input
content = get_content(url)

start_index = content.find("findResult odd")
end_index = content.find("img src=")

soup=BeautifulSoup(content[start_index:end_index])
tag = soup.a
url = "http://www.imdb.com/"+tag['href']
content = get_content(url)
start_index = content.find("overview-top")
end_index = content.find("overview-bottom")

soup = BeautifulSoup(content[start_index:end_index])
tag = soup.time
json = json_attributes.JSONAttributes()
json.duration = tag.text.strip()
genre=soup.findAll(itemprop='genre')
for item in genre:
    json.genre.append(item.text)
rating = soup.find(name='div',attrs={'class','star-box-giga-star'})
json.rating = rating.text.strip()

description = soup.find(itemprop='description')
json.description = description.text.strip()

names = soup.findAll(itemprop='name')
json.title = names[0].text

for i in range(1,len(names)):
    json.actors.append(names[i].text)

json.print_all()