#libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from yfinance import download

# names of stocks
stocks = ["AAPL", "MSFT", "GOOGL", "AMZN"]

# **Download Data from Yahoo Finance**
data = download(tickers=stocks,start="2024-01-01",end="2025-01-01")

close_price = data["Close"]
daily_returns = close_price.pct_change().dropna()
weights = np.array([0.30,0.40,0.2,0.1])

expected_return = np.sum(daily_returns.mean() * weights) * 252
portpolio_validity  = np.sqrt(np.dot(weights.T, np.dot(daily_returns.cov() * 252, weights)))

print(f"Expected Annual Return: {expected_return*100:.2f}%")
print(f"Portfolio Volatility: {portpolio_validity*100:.2f}%")

portpoilio_growth = (1 + daily_returns).cumprod()
portpoilio_growth.plot(figsize=(10,6))
plt.title("Portfolio Growth Over Time")
plt.xlabel("Date")
plt.ylabel("Growth")
plt.legend(stocks)
plt.show()