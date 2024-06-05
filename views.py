from flask import render_template, url_for, redirect, session
from main import app
from flask_login import login_required
from forms import UserForm

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/login/<error>")
@app.route("/login/")
def login(error=""):
    form = UserForm()
    success = session.pop('success', None)
    return render_template("index.html", form=form, error=error, success=success)

@app.route('/dashboard/', methods=['GET', 'POST'])
@login_required
def dashboard():
   return render_template('dashboard.html')