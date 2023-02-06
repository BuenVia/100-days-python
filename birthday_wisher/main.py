##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random
import smtplib

my_email = "biffbuchanan1985@gmail.com"
my_password = "ttqlmucjwavxzxza"

today = dt.datetime.now()
month = today.month
day = today.day
if day < 10:
    date = f"0{day}"
else: 
    date = f"{day}"

letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
person_list = []


with open("./birthday_wisher/birthdays.csv") as data_file:
    data = data_file.readlines()
    for item in data[1:]:
        details = item.split(',')
        new_item = {
            "name": details[0],
            "email": details[1],
            "year": details[2],
            "month": details[3],
            "day": details[4].strip()
        }
        person_list.append(new_item)


for person in person_list:
    if person["day"] == date:
        with open(f"./birthday_wisher/letter_templates/{random.choice(letter_list)}") as letter_file:
            letter = letter_file.readlines()
            x = letter[0].replace("[NAME]", person["name"])
            letter[0] = x

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=person["email"],
                    msg=f"Subject:Happy Birthday\n\n{''.join(letter)}"
                )
            

