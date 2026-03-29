from newsapi import NewsApiClient
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

newsapi = NewsApiClient(api_key="dc07296225d04fa29972591a48c73041")

sia = SentimentIntensityAnalyzer()

def get_news():

    articles = newsapi.get_everything(
        q="Reliance Industries",
        language='en',
        sort_by='publishedAt',
        page_size=20
    )

    headlines = []

    for article in articles['articles']:
        headlines.append(article['title'])

    return headlines


def analyze_sentiment(headlines):

    sentiments = []

    for text in headlines:

        score = sia.polarity_scores(text)

        sentiments.append(score['compound'])

    df = pd.DataFrame({
        "headline": headlines,
        "sentiment": sentiments
    })

    df.to_csv("data/news_sentiment.csv", index=False)

    print("News sentiment saved to data/news_sentiment.csv")

    return df