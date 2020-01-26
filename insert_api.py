
from flask import Flask, jsonify
from flask_script import Manager, Command, Option
from newsapi import NewsApiClient
from pymongo import MongoClient

app = Flask(__name__)

manager = Manager(app)

@manager.command
def bussiness_news():

    connect = MongoClient()
    db = connect.newsapi
    collection = db.newsapi_data

    headers = {'Authorization': '7cb11b15c84a4ff1af515df4c4dbaf47'}

    top_headlines_url = 'https://newsapi.org/v2/top-headlines'
    everything_news_url = 'https://newsapi.org/v2/everything'
    sources_url = 'https://newsapi.org/v2/sources'
    

    newsapi = NewsApiClient(api_key="7cb11b15c84a4ff1af515df4c4dbaf47")
    topheadlines = newsapi.get_top_headlines(country="us", category="business")

    articles = topheadlines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

        document = {
            'title' : news,
            'description' : desc,
            'urlToImage': img
        }

    collection.insert_one(document)

    print('data has been entered')

@manager.command
def technology_news():

    connect = MongoClient()
    db = connect.newsapi
    collection = db.newsapi_data

    headers = {'Authorization': '7cb11b15c84a4ff1af515df4c4dbaf47'}

    top_headlines_url = 'https://newsapi.org/v2/top-headlines'
    everything_news_url = 'https://newsapi.org/v2/everything'
    sources_url = 'https://newsapi.org/v2/sources'
    

    newsapi = NewsApiClient(api_key="7cb11b15c84a4ff1af515df4c4dbaf47")
    topheadlines = newsapi.get_top_headlines(country="us", category="technology")

    articles = topheadlines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

        document = {
            'title' : news,
            'description' : desc,
            'urlToImage': img
        }

    collection.insert_one(document)

    print('data has been entered')
    
if __name__ == '__main__':
    manager.run()