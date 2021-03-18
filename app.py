#!/usr/bin/env python3

from os import kill
import sys
import logging.config

import bottle
from bottle import HTTPResponse, get, post, request, response, template, redirect
import requests
import uuid
import shelve


# Set up app and logging
app = bottle.default_app()
app.config.load_config('./etc/app.ini')

logging.config.fileConfig(app.config['logging.config'])

KV_URL = app.config['sessions.kv_url']

# Disable Resource warnings produced by Bottle 0.12.19 when reloader=True
#
# See
#  <https://docs.python.org/3/library/warnings.html#overriding-the-default-filter>
#
if not sys.warnoptions:
    import warnings
    warnings.simplefilter('ignore', ResourceWarning)


@get('/')
def show_form():
    sessionID1 = str(uuid.uuid4())
    sessionID2 = str(uuid.uuid4())
    cookie1 = request.cookies.get("count1", default=sessionID1)
    cookie2 = request.cookies.get('count2', default=sessionID2)
    
    # session = requests.Session()
    # response = session.get('http://localhost:5000')
    # sessionID1 = request.cookies.get("count1")
    # sessionID2 = request.cookies.get('count2')
    
    
    
    
    # print(sessionID1)
    # print(sessionID2)
    # if not sessionID1:
    #     sessionID1 = str(uuid.uuid4())
    #     response.set_cookie('count1', str(sessionID1))

    # if not sessionID2:
    #     sessionID2 = str(uuid.uuid4())
    #     response.set_cookie('count2', str(sessionID2))


    print("session1/Showform: ",sessionID1)
    print("session2/showform: ", sessionID2)

    # response = requests.get('http://localhost:5000')
    # print(response.cookies)



    with shelve.open('./var/kv.dbm') as db:
        if cookie1 not in db:
            db[cookie1] = 0
        
        if cookie2 not in db:
            db[cookie2] = 0
        count1 = db[cookie1]
        count2 = db[cookie2]
        
        count1 += 1
        db[cookie1] = int(count1)
        response.set_cookie('count1', cookie1)
        response.set_cookie('count2', cookie2)

 
        # response.set_header('Set-Cookie', f"{sessionID1}, {sessionID2}")
        
        
        return template('counter.tpl', counter1=count1, counter2=count2)


 



    # count1 = int(count1) + 1

    # response.set_cookie('count1', str(count1))


@post('/increment')
def increment_count2():
    # session = requests.Session()
    # response = session.get('http://localhost:5000')
    #print(response)
    # checkSessionID = response.get_cookie('count2')
    # sessionID = str(uuid.uuid4())
    # count2 = request.get_cookie('count2', default=sessionID)
    # count2 = int(count2) + 1
    sessionID1 = str(uuid.uuid4())
    sessionID2 = str(uuid.uuid4())
    cookie2 = request.get_cookie('count2', default=sessionID2)
    cookie1 = request.get_cookie('count1', default=sessionID1)
    print('sessionID2/increment: ', sessionID2)
    print('sessionID1/increment: ', sessionID1)
    # response.set_header('Set-Cookie', f"{sessionID1}, {sessionID2}")
    with shelve.open('./var/kv.dbm') as db:
        count2 = db[cookie2]

        count2 += 1

        db[cookie2] = int(count2)
        response.set_cookie('count2', cookie2)
        # response.set_header('Set-Cookie', f"{sessionID1}, {sessionID2}")
        return redirect('/')

    # response.set_cookie('count2', str(count2))



@post('/reset')
def reset_counts():

    with shelve.open('./var/kv.dbm') as db:
        getSessionID1 = request.get_cookie('count1')
        getSessionID2 = request.get_cookie('count2')
        

        db.pop(getSessionID1, None)
        db.pop(getSessionID2, None)
        response.delete_cookie('count1')
        response.delete_cookie('count2')

        return redirect('/')


# a0125de5-8b5c-47e8-972e-c98d05b8c932
# "6205d68b-bfa4-451f-9932-9dd28b5e6abe"