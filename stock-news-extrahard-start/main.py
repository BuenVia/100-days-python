import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

API_KEY = "6LZBKIIKYGUMS2FN"
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API_KEY
}

def get_date(num):
    date = datetime.now() - timedelta(num)
    while date.weekday() > 4:
        date -= timedelta(1)    
    return date.strftime("%Y-%m-%d")

respone = requests.get("https://www.alphavantage.co/query", params=parameters)
respone.raise_for_status()
stock_data = respone.json()
daily_stock_data = stock_data['Time Series (Daily)']
day_one = float(daily_stock_data[get_date(1)]['4. close'])
day_two = float(daily_stock_data[get_date(2)]['4. close'])
flux = ((day_two - day_one) * 100) / day_one

if flux > 5 or flux < -5:
    print("Get News", flux)
else:
    print("No", flux)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

