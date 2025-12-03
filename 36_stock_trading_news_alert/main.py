from operator import truediv

import requests, os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
#-----------------------------------------------------------------------------------------------------------------------
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#alphavantage API parameters
av_api_access_key = os.environ["ALPHAVANTAGE_TOKEN"]
av_api_endpoint = "https://www.alphavantage.co/query?"
av_api_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": av_api_access_key,
}

#stock price change calculation
def check_stock_price_change():
    # # alphavantage API request
    # av_api_request = requests.get(av_api_endpoint, params=av_api_parameters)
    # av_api_request.raise_for_status()
    #
    # # alphavantage API data processing
    # av_data = av_api_request.json()
    # av_data_timeseries = av_data['Time Series (Daily)']
    # av_data_days = [value for (key, value) in av_data_timeseries.items()]
    # stock_price_yesterday = float(av_data_days[0]["4. close"])
    # stock_price_twodaysago = float(av_data_days[1]["4. close"])
    stock_price_yesterday = 429.15
    stock_price_twodaysago = 470.18
    stock_price_change = round(((stock_price_yesterday - stock_price_twodaysago)/stock_price_twodaysago)*100, 0)
    if abs(stock_price_change) >= 5:
        return True, stock_price_change

#-----------------------------------------------------------------------------------------------------------------------
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#newsapi API parameters
newsapi_api_access_key = os.environ["NEWSAPI_TOKEN"]
newsapi_endpoint = "https://newsapi.org/v2/everything?"
newsapi_parameters = {
    "q": COMPANY_NAME,
    "apiKey": newsapi_api_access_key,
    "language": "en",
}

def get_news():
    # newsapi API request
    newsapi_api_request = requests.get(newsapi_endpoint, params=newsapi_parameters)
    newsapi_api_request.raise_for_status()

    # newsapi data processing
    newsapi_data = newsapi_api_request.json()
    newsapi_data_articles = newsapi_data['articles']
    newsapi_news = {newsapi_data_articles[news_number]["title"]: newsapi_data_articles[news_number]["description"]
            for news_number in range(3)}
    return newsapi_news
#-----------------------------------------------------------------------------------------------------------------------
## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

#twilio API parameters
account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_TOKEN"]
twilio_nr = "+17439626778"
client = Client(account_sid, auth_token)

def send_sms(body):
    client.messages.create(body=body, from_=twilio_nr, to=os.environ["MY_PHONE_NUMBER"])

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

def stock_trading_news_alert():
    change_significant, change = check_stock_price_change()
    if change_significant:
        news = get_news()
        if change < 0:
            header = f"{STOCK}: 🔻{change}%\n"
        else:
            header = f"{STOCK}: 🔺{change}%\n"
        for title in news:
            message = (f"Headline: {title}\n"
                        f"Brief: {news[title]}")
            sms_text = header + message
            #print(sms_text)
            send_sms(sms_text)

stock_trading_news_alert()

