from flask import Flask
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route("/")
def index():
        newsapi = NewsApiClient(api_key="519b09bcd038461aa28d5cf702b9e0e9")
        topheadlines = newsapi.get_top_headlines(source="al-jazeera-english")

        articles = topheadlines["articles"]

        desc = []
        news = []
        img = []

        for i in range(len(articles)):
            myarticles = articles[i]

            news.append(myarticles["title"])
            desc.append(myarticles["description"])
            img.append(myarticles["urlToImage"])

        mylist = zip(news, desc, img)
