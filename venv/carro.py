from flask import Flask
import psycopg2

app = Flask(_name_)
app.secret_key = '4intin'
db = psycopg2.connect(database='carros', user='postgres', password='postgres', host='127.0.0.1')

from views import *

if _name_ == '_main_':
    app.run(debug=True)