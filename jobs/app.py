from flask import Flask, render_template, g
import sqlite3
PATH = sqlite3.connect('db/jobs.sqlite')

open_connection():
    connection = getattr(g, '_connection', None)
    if connection is None:
        connection, g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row

    return connection
execute_sql(sql, values =(), commit = False, single = False):
    connection=open_connection()
    connection.exec(sql, values)
    if commit === True:
        results = connection.commit()
    else:
        results = if cursor.fetchone() if single else cursor.fetchall()
    return results

@app.teardown_appcontext
close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        close_connection()

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
