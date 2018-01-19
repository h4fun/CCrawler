from flask import Flask, _app_ctx_stack, current_app
import MySQLdb
import sqlalchemy.pool as pool

app = Flask(__name__)
#app.config.from_pyfile('config.py')


@app.teardown_appcontext
def close_database_connection(error=None):
    con = getattr(_app_ctx_stack, 'database', None)
    if con:
        con.close()


def getconn(db_conf=None):
    if db_conf is None:
        db_conf = current_app.config['DB_CONFIG']
    conn = MySQLdb.connect(**db_conf)
    return conn

mypool = pool.QueuePool(getconn, max_overflow=10, pool_size=5)
app.db_pool = mypool


def get_db():
    ctx = _app_ctx_stack.top
    con = getattr(ctx, 'database', None)
    if con is None:
        con = current_app.db_pool.connect()
        ctx.database = con
    return con


@app.route('/')
def index():
    con = get_db()
    cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    rv = cursor.execute('select 1')
    return str(rv)


if __name__ == "__main__":
