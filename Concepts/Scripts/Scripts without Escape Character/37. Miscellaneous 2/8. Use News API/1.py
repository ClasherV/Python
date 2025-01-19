import requests
import json
querry=input("What type of News are You Interested in?: ")
url=f"https://newsapi.org/v2/everything?q={querry}&from=2024-12-19&sortBy=publishedAt&apiKey=API_KEY"
r=requests.get(url)
news=json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------------------------------------------------\n")