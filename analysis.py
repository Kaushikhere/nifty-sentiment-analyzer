import pandas as pd

sentiment_df = pd.read_csv("news_sentiment.csv")
price_df = pd.read_csv("nifty_price_data.csv")
merge_df = pd.merge(sentiment_df, price_df, on = "date")

#print(merge_df.head())

merge_df['sentiment_score'] = merge_df['sentiment'].map({'positive': 1, 'neutral': 0, 'negative': -1})

#print(merge_df[['sentiment', 'sentiment_score']].head(10))

daily_sentiment = merge_df.groupby('date')['sentiment_score'].mean()
#print(daily_sentiment)

price_df['Next_Day_Return'] = price_df['Daily_Return'].shift(-1)

#print(daily_sentiment)
#print(price_df[['date', 'Daily_Return', 'Next_Day_Return']].tail(5))

daily_sentiment = daily_sentiment.reset_index()
final_df = pd.merge(daily_sentiment, price_df[['date', 'Next_Day_Return']], on='date')
print(final_df)