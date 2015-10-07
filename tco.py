#!/usr/bin/env python

import requests
from flask import Flask
import json
app = Flask(__name__)
app.debug = True

TCO = ['199.59.150.44', '199.59.148.12']
SLUGS = {}

@app.route("/hello")
def hello():
    return app.make_response('hello')


def save(db):
    json.dump(db, open('db.json', 'w'))


@app.route("/<slug>")
def default(slug):
    db = json.load(open('db.json', 'r'))
    if slug in db:
        db[slug]['count'] += 1;
        save(db)
        return app.make_response((' old redir4u',
            db[slug]['status_code'],
            {'location': db[slug]['location']}))
    redir = requests.get('http://' + TCO[0] + '/' + slug,
            headers={'Host': 't.co','User-Agent':'me','Accept':'*/*'},
            allow_redirects=False)
    db[slug] = {'count': 1,
        'status_code': redir.status_code,
        'location': redir.headers.get('location', None)}
    save(db)
    if 'location' in redir.headers:
        location = redir.headers['location']
        return app.make_response(("redir4u",
            redir.status_code,
            {'location': location}))
    else:
        return app.make_response('no location found for ' + slug + '''
                here is some bs:''' + str(redir.headers))

if __name__ == "__main__":
    app.debug = True
    app.run()
