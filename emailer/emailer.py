import smtplib
from email.mime.text import MIMEText

with open ('test_msg.txt', 'r') as myfile:
    body = myfile.read()

with open ('email_address.txt', 'r') as myfile2:
    data = myfile2.read()
    email_addy = data.split(" ")

with open ('creds.txt', 'r') as auth:
    cred = auth.read()
    my_creds = cred.split(" ")

from_address = my_creds[0]
user_name = my_creds[1]
passwd = my_creds [2]

for e in email_addy:
    from_address = from_address
    msg = MIMEText(body)
    msg['Subject'] = 'Follow UP'
    msg['From'] = from_address
    msg['To'] =e

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(user_name, passwd)
    server.sendmail(from_address, e, msg.as_string())
    server.quit()
    print("Mail sent")


    