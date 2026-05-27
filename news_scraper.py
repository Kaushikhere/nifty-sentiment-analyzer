import requests 
from bs4 import BeautifulSoup
import pandas as pd 

url = "https://economictimes.indiatimes.com/markets/stocks/news"
response = requests.get(url)
#print(response.status_code)
#print(response.text[:500])

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("div", class_= "eachStory")
#print(len(articles))
#print(articles[0])
#print(articles[0].find("a").text)
#print(articles[0].find("time").text)

data = []
for a in articles:
    headline = a.find("a").text
    date = a.find("time").text
    data.append({"headline": headline, "date": date})

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'], format = 'mixed')
df['date'] = df['date'].dt.date
df.to_csv("news_data.csv", index = False)
print(df.head())

