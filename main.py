import smtplib
import random
import pandas as pd
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

day = dt.datetime.now().day
month = dt.datetime.now().month

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

# == ------------------ Read All Files --------------------- == #

with open("letter_templates/letter_1.txt") as massage_one:
    read_massage_one = massage_one.read()

with open("letter_templates/letter_2.txt") as massage_tow:
    read_massage_two = massage_tow.read()

with open("letter_templates/letter_3.txt") as massage_three:
    read_massage_three = massage_three.read()

# == ----------------- Show name of date ------------------- == #

df = pd.read_csv("birthdays.csv")
condition = (df["day"] == day) & (df["month"] == month)

birthday_people = df.loc[condition, ["name", "email"]]

# --------------------------- == Choose The Letter == ---------------------------- #
for index, row in birthday_people.iterrows():
    name = row["name"]
    email = row["email"]
    letters = {
        "letter_one": read_massage_one.replace("[NAME]", name),
        "letter_two": read_massage_two.replace("[NAME]", name),
        "letter_three": read_massage_three.replace("[NAME]", name)
    }

    MASSAGE = random.choice(list(letters.values()))

    # Improved print statements for better clarity
    print(f"Sending birthday message to {name} ({email})")
    print(f"Message:\n{MASSAGE}")
    print("-" * 50)

    # ---------------------------- == Send Message == ------------------------------------ #
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Happy Birthday {name}\n\n{MASSAGE}")

    # Confirmation print statement after sending email
    print(f"Message sent to {name} at {email}")
    print("=" * 50)




