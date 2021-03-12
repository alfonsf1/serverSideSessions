#!/usr/bin/env python3
import sys
import shelve
import requests

firstArgv = sys.argv[1]
resp = requests.get(str(firstArgv))
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError("URL doesn't exist!")

list_of_keys = resp.json()['keys']


with shelve.open('./var/kv.dbm') as db:
    for key in list_of_keys:
        print(f'{{\'{key}\': \'{db[key]}\'}}')


#commands to run
# chmod 755 dump.py 
#./dump.py http://localhost:5100