import search_function
import smtplib
import time

my_email = "jwood.droid@gmail.com"
password = "Ii3Jy4Masr7z"

my_main_email = "emerica4u@hotmail.com"

NUMBER_OF_RESULTS = 20
query_strings = ["New Fragrance Release", "Discontinued Fragrance"]

for i in range(0, len(query_strings)):
    email_text = search_function.run_a_search(query_strings[i], NUMBER_OF_RESULTS)


    message = f'Subject: {query_strings[i]} Watchdog\n\n{email_text}'
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_main_email, msg=message.encode("utf-8"))
    connection.close()
    time.sleep(10)
    print(f'Sorted.')
