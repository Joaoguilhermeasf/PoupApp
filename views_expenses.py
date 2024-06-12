from flask import render_template, url_for, redirect, session, jsonify, request
from main import app, db
from flask_login import login_required, current_user
from forms import RegExpenseForm
from models import Expense, Users

@app.route('/cadgastos', methods=['GET', 'POST'])
def cadgastos():
    form = RegExpenseForm()
    user = current_user
    if request.method == 'POST':
        new_expense = Expense(
            user_id = user.user_id,
            amount = form.expense_amount.data,
            description = form.expense_description.data,
            expense_date = form.expense_date.data,
            category = form.expense_category.data
        )
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('cadastrar_gastos.html', form=form, user=user)

@app.route('/gastos')
def info_gastos():
    series_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    series_dates = ['1/1/2000', '2/1/2000', '3/1/2000', '4/1/2000', '5/1/2000', '6/1/2000', '7/1/2000', '8/1/2000', '9/1/2000', '10/1/2000', '11/1/2000', '12/1/2000', '1/1/2001']

    # Retornar esses dados como JSON
    return jsonify({'series_values': series_values, 'series_dates': series_dates})