import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import search_function
import time

sender_email = "jwood.droid@gmail.com"
password = "Ii3Jy4Masr7z"

receiver_email = "emerica4u@hotmail.com"

NUMBER_OF_RESULTS = 20
query_strings = ["Fragrance", "New Fragrance Release", "Discontinued Fragrance"]

for i in range(0, len(query_strings)):
    text = search_function.run_a_search(query_strings[i], NUMBER_OF_RESULTS)
    html = search_function.run_a_search_html(query_strings[i], NUMBER_OF_RESULTS)

    message = MIMEMultipart("alternative")
    message["Subject"] = f'{query_strings[i]} Watchdog'
    message["From"] = sender_email
    message["To"] = receiver_email

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    print(f"{[i + 1]} email(s) sorted.")
    time.sleep(5)


