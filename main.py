from flask import Flask, render_template
from forms import UserForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

@app.route('/')
def index():
    form = UserForm()
    return render_template('index.html', form=form)

from users import *
from dashboard import *

if __name__ == '__main__':
    app.run(debug=True)