import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def train():

    stock = pd.read_csv("data/stock_data.csv")
    sentiment = pd.read_csv("data/news_sentiment.csv")

    sentiment_score = sentiment['sentiment'].mean()

    stock['sentiment'] = sentiment_score

    X = stock[['Open','High','Low','Volume','sentiment']]
    y = stock['Close']

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

    model = RandomForestRegressor()

    model.fit(X_train,y_train)

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test,predictions)

    print("Model MSE:", mse)

    print("Sample predictions:", predictions[:5])