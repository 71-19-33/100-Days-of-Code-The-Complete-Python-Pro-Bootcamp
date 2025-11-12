import smtplib

my_email = "dempwolff@pm.me"

connection = smtplib.SMTP("smtp.protonmail.ch")
connection.starttls()
connection.login(user=my_email, password=<PASSWORD>)

#LESSON SKIPPED