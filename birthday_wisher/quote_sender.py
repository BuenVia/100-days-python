"""martymcfly1985@myyahoo.com
Delorean1985

biffbuchanan1985@gmail.com
Delorean_1985"""

import smtplib
import datetime as dt
import random

my_email = "biffbuchanan1985@gmail.com"
password = "ttqlmucjwavxzxza"

now = dt.datetime.now()
if now.weekday() == 0:
    with open("./birthday_wisher/quotes.txt") as data_file:
        data = data_file.readlines()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="martymcfly1985@myyahoo.com",
            msg=f"Subject:Inspirational Quote\n\n{random.choice(data)}"
        )