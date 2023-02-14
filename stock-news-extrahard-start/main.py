import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "6LZBKIIKYGUMS2FN"
MY_EMAIL = "biffbuchanan1985@gmail.com"
MY_PASSWORD = "ttqlmucjwavxzxza"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API_KEY
}

respone = requests.get("https://www.alphavantage.co/query", params=parameters)
respone.raise_for_status()
data = respone.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]
day_before = data_list[1]["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before))
diff_percent = (difference / float(yesterday_closing_price)) * 100

print(diff_percent)

if diff_percent > 1.1:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_parameters = {
        "function": "NEWS_SENTIMENT",
        "apikey": API_KEY
    }
    news_response = requests.get("https://www.alphavantage.co/query", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_list = news_data["feed"][:3]

    for article in news_list:
        print(article["title"])

    message = f"Subject: {STOCK}: {round(diff_percent)}% \n\nHeadline: {news_list[0]['title']} \nBrief: {news_list[0]['summary']}"

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="matthewclifford@hotmail.co.uk",
        msg=message
)



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

