import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt

yf.download("TICKER", start="YYYY-MM-DD", end = "YYYY-MM-DD")

nifty = yf.download("^NSEI", start = "2024-01-01", end = "2025-01-01")
print(nifty.head(5))

nifty = nifty[['Close', 'Volume']]
print(nifty.head(5))

nifty['Daily_Return'] = nifty['Close'].pct_change()*100
print(nifty['Daily_Return'])

nifty = nifty.dropna()

nifty.to_csv ("nifty_price_data.csv")

plt.plot(nifty['Close'])
plt.title('Nifty 50 - 2024')
plt.show