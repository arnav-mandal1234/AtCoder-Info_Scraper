import requests
from bs4 import BeautifulSoup as soup

class user:
    username = ""
    rank = ""
    rating = ""
    twitter = ""
    country = ""
    max_rating = ""
    url = ""

    def __init__(self, username,  rank, rating, max_rating, twitter, country, url):
        self.username = username
        self.rank = rank
        self.rating = rating
        self.max_rating = max_rating
        self.twitter = twitter
        self.country = country
        self.url = url


user_url = []
user_details = []

for i in range(1,9):
    r = requests.get("https://atcoder.jp/ranking?p="+str(i))
    sauce = soup(r.content, "html.parser")
    body = sauce.find_all("a",  {"class": "username"})
    for username in body:
        user_url.append(username.get("href"))


for i in range (0, 768):
    r = requests.get("https://atcoder.jp"+user_url[i])
    print(user_url[i])
    sauce = soup(r.content, "html.parser")
    info = sauce.find_all("dl",  {"class": "dl-horizontal"})

    rank = " "
    rating = " "
    twitter = " "
    country = " "
    max_rating = " "
    url = " "

    for j in info:
        text = ""
        for k in j.children:
            if k.name == 'dd':
                if text == "Country":
                    country = k.text
                if text == "twitter ID":
                    twitter = k.text
                if text == "Rank":
                    rank = k.text
                if text == "Rating":
                    rating = k.text
                if text == "Highest Rating":
                    max_rating = k.text

            if k.name == 'dt':
                text = k.text

    if twitter != " ":
        twitter = twitter.split("@")[1]
    user_details.append(user(user_url[i].split("/")[2],rank, rating, max_rating, twitter, country, user_url[0]))

with open("user_details.csv", "w") as out_file:
    string=""
    for user in user_details:
        string += user.username
        string +="," + user.rank
        string += "," + user.rating
        string += "," + user.max_rating
        string += "," + user.twitter
        string += "," + user.country
        string += "\n"
    out_file.write(string)



