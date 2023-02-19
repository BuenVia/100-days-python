import smtplib, os

MY_EMAIL = "biffbuchanan1985@gmail.com"
MY_PASSWORD = os.environ.get("GMAIL_BB_PASSWORD")

class NotificationManager:

    def __init__(self, message):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="matthewclifford@hotmail.co.uk",
            msg=message
        )