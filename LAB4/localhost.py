#!/usr/bin/env python3

import psutil
import shutil
import emails
import requests

def connected_to_localhost(url='http://127.0.0.1', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

if not connected_to_localhost():
    print("bad")
else:
    print("works")
