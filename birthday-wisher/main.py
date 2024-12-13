import random
import datetime as dt
import smtplib
import pandas 

today = dt.datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row['month'],data_row['day']): data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthday_dict:
        name = birthday_dict[today_tuple]
        ra_nu = random.randint(1,3)
        file_path = f"letter_templates/letter_{ra_nu}.txt"
        with open(file_path) as letter:
                contents = letter.read()
                contents = contents.replace("[NAME]",name)

        with smtplib.SMTP("smtp.gmail.com") as connection:

        
                #tls -> transfer layer security
                connection.starttls()
                connection.login(user="mail",password="password")
                connection.sendmail(from_addr="sender mail",to_addrs=name['email'],msg=f"Subject:Happy Birthday!\n\n{contents}")







