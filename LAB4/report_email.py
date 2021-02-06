#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib
import reports
import emails
import datetime
import sys

def main(argv):
    attachment = '/tmp/processed.pdf'
    today = datetime.date.today()
    title = today.strftime("Processed update on %B %d, %Y")
    description_list = []
    description_directory = '/home/student-00-72706b664a64/supplier-data/descriptions/'
    for file in os.listdir(description_directory):
        with open(description_directory + '/' + file, 'r') as description_file:
            description_files = []
            for line in description_file:
                description_files.append(line)
            description_list.append('name: ' + description_files[0].capitalize() +'<br/>')
            description_list.append('weight: ' + description_files[1] + '<br/>')
            description_list.append('<br/>')
    paragraph = ' '.join(description_list)
    print(paragraph)
    reports.generate_report(attachment, title, paragraph)
    recipient = "{}@example.com".format(os.environ.get('USER'))
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate_email('automation@example.com', recipient, "Upload Completed - Online Fruit Store", body, attachment)
    emails.send_email(message)

if __name__ == "__main__":
    main(sys.argv)

