
import sys
import shelve
import logging.config
import requests
import bottle
from bottle import request, get, put, delete, abort

# Set up app and logging
def shelf(callback):
    def wrapper(*args, **kwargs):
        with shelve.open(app.config['shelve.dbmfile']) as db:
            print('hey')
            bottle.local.db = db
            body = callback(*args, **kwargs)
            bottle.local.db = None
        return body
    return wrapper
# Make sure that each route has bottle.local.db set




# Return errors in JSON
#
# Adapted from # <https://stackoverflow.com/a/39818780>
#
def json_error_handler(res):
    if res.content_type == 'application/json':
        return res.body
    res.content_type = 'application/json'
    if res.body == 'Unknown Error.':
        res.body = bottle.HTTP_CODES[res.status_code]
    return bottle.json_dumps({'error': res.body})



# Disable Resource warnings produced by Bottle 0.12.19 when reloader=True
#
# See
#  <https://docs.python.org/3/library/warnings.html#overriding-the-default-filter>



app = bottle.default_app()
app.config.load_config('./etc/kv.ini')

logging.config.fileConfig(app.config['logging.config'])
app.install(shelf)
app.default_error_handler = json_error_handler
resp = requests.get("http://localhost:5100")
for key, value in resp.json().items():
    list = value
    
db = bottle.local.db

for key in list:
    print({key: db.get(key)})