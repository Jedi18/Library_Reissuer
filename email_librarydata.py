import smtplib
import ssl

# Required for gmail ssl
port = 465

from_email = 'ait.library.reissuer@gmail.com'
pwd = 'aitlibrary'

def create_message(books):
    message = '''Subject: AIT Library Reissuer Info\n\nYou have issued {} books'''.format(len(books))

    message_1 = '''\n\n'''

    for book in books:
        message_1 += '''{} by {} , return date - {}, days remaining - {}\n'''.format(book[0], book[1], book[2], book[3])

    message += message_1

    return message

def email_data(to_email, books):
    context = ssl.create_default_context()

    print(create_message(books))

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(from_email, pwd)
        message = create_message(books)
        server.sendmail(from_email, to_email, message)

    print("Email containing details has been sent to provided email id.")
