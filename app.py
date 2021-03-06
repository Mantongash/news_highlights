from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route("/index")
def index():
    newsapi = NewsApiClient(api_key="519b09bcd038461aa28d5cf702b9e0e9")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines["articles"]

    desc = []
    news = []
    img = []
    url = []
    pubAt = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])
        url.append(myarticles["url"])
        pubAt.append(myarticles["publishedAt"])

    mylist = zip(news, desc, img, url, pubAt)

    return render_template("index.html", context=mylist)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/bbc")
def bbc():
    newsapi = NewsApiClient(api_key="519b09bcd038461aa28d5cf702b9e0e9")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines["articles"]

    desc = []
    news = []
    img = []
    url = []
    pubAt = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])
        url.append(myarticles["url"])
        pubAt.append(myarticles["publishedAt"])

    mylist = zip(news, desc, img, url, pubAt)

    return render_template("bbc.html", context=mylist)


@app.route("/abc")
def abc():
    newsapi = NewsApiClient(api_key="519b09bcd038461aa28d5cf702b9e0e9")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")

    articles = topheadlines["articles"]

    desc = []
    news = []
    img = []
    url = []
    pubAt = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])
        url.append(myarticles["url"])
        pubAt.append(myarticles["publishedAt"])

    mylist = zip(news, desc, img, url, pubAt)

    return render_template("abc.html", context=mylist)


@app.route("/cnn")
def cnn():
    newsapi = NewsApiClient(api_key="519b09bcd038461aa28d5cf702b9e0e9")
    topheadlines = newsapi.get_top_headlines(sources="associated-press")

    articles = topheadlines["articles"]

    desc = []
    news = []
    img = []
    url = []
    pubAt = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])
        url.append(myarticles["url"])
        pubAt.append(myarticles["publishedAt"])

    mylist = zip(news, desc, img, url, pubAt)

    return render_template("cnn.html", context=mylist)


if __name__ == " __main__":
    app.debug = True
    app.run
