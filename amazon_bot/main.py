import requests
from bs4 import BeautifulSoup
import smtplib


MY_EMAIL = "mclifford1984@gmail.com"
MY_PASSWORD = "wzvrjkdhsldyczne"
URL = "https://www.amazon.co.uk/Cabin-Max-Travel-Luggage-Backpack/dp/B072KKHPGX?th=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=URL, headers=HEADERS)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

get_price = soup.find(name="span", class_="a-offscreen")
price = float(get_price.getText()[1:])

get_product_name = soup.find(name="span", id="productTitle")
product_name = get_product_name.getText().lstrip()

print(price, product_name)

if price < 36:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="matthewclifford@hotmail.co.uk",
        msg=f"Subject: Price Drop!!!\n\nThe item you want is now on sale. \n\nItem: {product_name} \n\nPrice: £{price}"
    )