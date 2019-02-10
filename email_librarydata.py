import smtplib
import ssl

# Required for gmail ssl
port = 465

from_email = 'ait.library.reissuer@gmail.com'
pwd = 'aitlibrary'

def create_message(days_remaining, title_str, author_str, return_date):
    return """\
    Subject: AIT Library Reissuer Info

    It works?"""

def email_data(to_email, days_remaining, title_str, author_str, return_date):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(from_email, pwd)
        message = create_message(days_remaining, title_str, author_str, return_date)
        server.sendmail(from_email, to_email, message)

    print("Email containing details has been sent to provided email id.")
