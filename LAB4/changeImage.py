#!/usr/bin/env python3

import os
from PIL import Image
import subprocess

input_catalog = '/home/student-00-72706b664a64/supplier-data/images/'
output_catalog = '/home/student-00-72706b664a64/supplier-data/images/'

for file in os.listdir(input_catalog):
    try:
        im = Image.open(input_catalog + file)
        filename = file[:-5]
        im.resize((600,400)).convert('RGB').save(output_catalog + filename + '.jpeg')
        print("file {} converted".format(file))
    except OSError:
        continue


