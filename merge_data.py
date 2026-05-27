import pandas as pd
price_df = pd.read_csv("nifty_price_data.csv")
news_df = pd.read_csv("news_data.csv")

print(price_df.columns.tolist())
print(news_df.columns.tolist())

merged_df = pd.merge(price_df, news_df, on ="date")

print(merged_df.head())
print(merged_df.shape)
print(price_df.tail())