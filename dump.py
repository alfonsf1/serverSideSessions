import shelve

with shelve.open('./var/kv.dbm') as db:
    for k in db.keys():
        print(f'{{\'{k}\': \'{db[k]}\'}}')


