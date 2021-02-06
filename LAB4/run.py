#!/usr/bin/env python3

import os
import requests
import json

url = 'http://localhost/fruits/'
description_directory = '/home/student-00-72706b664a64/supplier-data/descriptions/'
image_catalog = '/home/student-00-72706b664a64/supplier-data/images/'
description_data = []

#collect data in dictionary format from text files
for file in os.listdir(description_directory):
    with open(description_directory + file, 'r') as description:
        description_list = []
        description_dictionary = {}
        for line in description:
            description_list.append(line)
        description_dictionary["name"] = description_list[0].strip()
        description_dictionary["weight"] = int(description_list[1].strip(' lbs\n'))
        description_dictionary["description"] = description_list[2].strip()
        if file.endswith('.txt'):
            stripped_name = file[:-4]
        description_dictionary["image_name"] = stripped_name + '.jpeg'
        description_data.append(description_dictionary)

#send description data in json format
for data in description_data:
    print(type(data))
    response = requests.post(url, json=data)
    print(response.status_code)
    if response.status_code == 201:
        print("Post for fruit {} is created".format(data['name']))
    else:
        print("Post for fruit {} failed".format(data['name']))

