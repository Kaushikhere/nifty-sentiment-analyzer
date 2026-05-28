import pandas as pd
from transformers import pipeline

sentiment_pipeline = pipeline("text-classification", model = "ProsusAI/finbert")

df = pd.read_csv("news_data.csv")

#test = sentiment_pipeline("ONGC shares fall 4% despite profit jump")
#print(test)

labels = []
scores = []
for headline in df['headline']:
    result = sentiment_pipeline(headline)
    labels.append(result[0]['label'])
    scores.append(result[0]['score'])

df['sentiment'] = labels
df['score'] = scores
print(df.head())
df.to_csv("news_sentiment.csv", index=False)
print(df['sentiment'].head(10))
