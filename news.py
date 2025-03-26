# news
"""
pull newsfeed data
"""
import requests

from apiKeys import *
from logHandler import Logger

log = Logger(True, "news")



class News:
    def __init__(self):
        pass

    # Function to get the latest news
    def get_news(self):
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
            response = requests.get(url)
            data = response.json()
            if data["status"] == "ok" and data["totalResults"] > 0:
                articles = data["articles"][:5]
                news_summary = "Here are the top 5 news headlines: "
                for idx, article in enumerate(articles):
                    news_summary += f"\n{idx + 1}. {article['title']}"
                return news_summary
            else:
                return "I couldn't fetch the news at the moment."
        except Exception as e:
            print(f"Error fetching news: {e}")
            return "Unable to get the news right now."

