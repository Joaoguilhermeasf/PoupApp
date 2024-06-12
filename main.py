from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_login import login_manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'index'
bcrypt = Bcrypt(app)

@login_manager.user_loader
def load_user(user_login):
    return User.get(user_login)


from views import *
from users import *
from views_expenses import *


if __name__ == '__main__':
    app.run(debug=True)