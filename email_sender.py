
import smtplib

from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Tricia Miller'
email['to'] = 'yeshuasglory@gmail.com'
email['subject'] = 'Hooray!'
email.set_content('I did it!')

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
    smtp.login('yeshuasglory@gmail.com', '************')
    smtp.send_message(email)
    print('Email sent!')