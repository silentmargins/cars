#!/usr/bin/env python3
import requests
import os

image_catalog = '/home/student-00-72706b664a64/supplier-data/images/'
url = 'http://localhost/upload/'
for file in os.listdir(image_catalog):
    if file.endswith('.jpeg'):
        with open(image_catalog + file, 'rb') as image:
            r = requests.post(url, files={'file':image})
        if r.status_code == 201:
            print("Post for {} is created".format(file))
        else:
            print("Posting of post {} failed".format(file))

