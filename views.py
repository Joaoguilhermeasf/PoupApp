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
    form = UserForm()
    success = session.pop('success', None)
    return render_template("index.html", form=form, error=error, success=success)

@app.route('/dashboard/', methods=['GET', 'POST'])
@login_required
def dashboard():
   user = current_user
   return render_template('dashboard.html', user=user)

@app.route('/gastos')
def info_gastos():
    series_values = [25.00, 22, 4, 7, 12, 12, 12, 12, 12, 12, 12, 12, 12]
    series_dates = ['1/1/2000', '2/1/2000', '3/1/2000', '4/1/2000', '5/1/2000', '6/1/2000', '7/1/2000', '8/1/2000', '9/1/2000', '10/1/2000', '11/1/2000', '12/1/2000', '1/1/2001']

    # Retornar esses dados como JSON
    return jsonify({'series_values': series_values, 'series_dates': series_dates})