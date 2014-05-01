from bs4 import BeautifulSoup
import requests

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
print(tag.text)
tag = soup.span
print(tag)