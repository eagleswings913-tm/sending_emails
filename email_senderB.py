
# customize the email for each person

import smtplib
from string import Template
from pathlib import Path
from email.message import EmailMessage

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Tricia Miller'
email['to'] = 'yeshuasglory@gmail.com'
email['subject'] = 'Hooray!'
email.set_content(html.substitute({'name': 'TimTim'}), 'html')

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
    smtp.login('yeshuasglory@gmail.com', 'xzxl lmrl yese fnsx')
    smtp.send_message(email)
    print('Email sent!')