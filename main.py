import stock_data
import news_sentiment
import train_model

def main():

    print("Downloading stock data...")
    stock_data.get_stock_data()

    print("Fetching news...")
    headlines = news_sentiment.get_news()

    print("Analyzing sentiment...")
    news_sentiment.analyze_sentiment(headlines)

    print("Training model...")
    train_model.train()

    print("Project finished successfully!")

if __name__ == "__main__":
    main()