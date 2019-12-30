from flask import Flask
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route("/")
  def index():
    newsapi = NewsApiClient(api_key = "519b09bcd038461aa28d5cf702b9e0e9")
    topheadlines = newsapi.get_top_headlines(source = "al-jazeera-english
")