import sqlite3

from flask import Flask
from flask import g

DATABASE = 'C:\\webroot\\dbs\\WhereAreThey.db'
app = Flask(__name__)


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def insert(table, fields=(), values=()):
    db = get_db()
    cur = db.cursor()
    query = u'INSERT INTO %s (%s) VALUES (%s)' % (
        table,
        ', '.join(fields),
        ', '.join(['?'] * len(values))
    )
    cur.execute(query, values)
    db.commit()
    id = cur.lastrowid
    cur.close()
    return id


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('WhereAreThey.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    # init_db()
    res = ""
    for crew in query_db('select * from crew'):
        res += "%s %s %s %s %s <BR>" % (crew[0], crew[1], crew[2], crew[3], crew[4])
    return res


@app.route('/kml')
def getKml():
    import simplekml
    kml = simplekml.Kml()
    # init_db()
    for crew in query_db('select * from crew'):
        # res += "%s %s %s %s %s <BR>" % (crew[0], crew[1], crew[2], crew[3], crew[4])
        kml.newpoint(name=crew[1], coords=[(crew[2], crew[3])])
    
    return kml.kml()


@app.route('/update/<name>/<x>/<y>/<info>')
def update(name, x, y, info):
    insert('crew', ('name', 'x', 'y', 'info'), (name, x, y, info))
    # return "%s %s %s %s" % (name, x, y, info)
    return "OK"


if __name__ == '__main__':
    app.run(host='192.168.43.206')
