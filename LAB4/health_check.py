#!/usr/bin/env python3

import psutil
import os
import emails
import requests

def page(subject_line):
    message = emails.generate_error_report('automation@example.com', recipient, subject_line, body)
    emails.send_email(message)

def connected_to_localhost(url='http://127.0.0.1', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

recipient = "{}@example.com".format(os.environ.get('USER'))
body = 'Please check your system and resolve the issue as soon as possible.'
if psutil.cpu_percent() > 80:
    subject_line = 'Error - CPU usage is over 80%'
    page(subject_line)
elif psutil.disk_usage('/').free/ psutil.disk_usage('/').total < 0.2:
    subject_line = 'Error - Available disk space is less than 20%'
    page(subject_line)
elif psutil.virtual_memory().free / (1024 * 1024) < 500:
    subject_line = 'Error - Available memory is less than 500MB'
    page(subject_line)
elif not connected_to_localhost():
    subject_line = 'Error - localhost cannot be resolved to 127.0.0.1'
    page(subject_line)


