from twilio.rest import Client
import requests

# Constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "xxx"
NEWS_API_KEY = "xxxx"

# Fetch stock data
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSCO.LON",
    "outputsize": "full",
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

# Convert dictionary to a list
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

# Price difference
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"

diff_percent = round((difference / yesterday_closing_price) * 100)

# Fetch news if change is significant
news_params = {
    "q": COMPANY_NAME,   # changed "title" → "q" (correct parameter for NewsAPI)
    "apiKey": NEWS_API_KEY,
}

if abs(diff_percent) > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    # Format articles
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}"
        for article in three_articles
    ]

    # Send SMS via Twilio
    account_sid = "xx"
    auth_token = "xxxx"

    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+xxx",  # Your Twilio number
            to="+xxxx"     # Your verified number
        )
