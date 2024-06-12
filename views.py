from flask import render_template, url_for, redirect, session, jsonify
from main import app
from flask_login import login_required, current_user
from forms import UserForm

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/login/<error>")
@app.route("/login/")
def login(error=""):
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = UserForm()
    success = session.pop('success', None)
    return render_template("index.html", form=form, error=error, success=success)

@app.route('/dashboard/', methods=['GET', 'POST'])
@login_required
def dashboard():
   user = current_user
   return render_template('dashboard.html', user=user)
