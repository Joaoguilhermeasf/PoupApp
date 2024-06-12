from flask import render_template, url_for, redirect, session, jsonify, request
from main import app, db
from flask_login import login_required, current_user
from forms import RegExpenseForm
from models import Expense, Users
from datetime import datetime

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
    data = datetime.now()
    mesAtual = data.month
    anoAtual = data.year

    series_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    series_dates = ['1/1/', '2/1/', '3/1/', '4/1/', '5/1/', '6/1/', '7/1/', '8/1/', '9/1/', '10/1/', '11/1/', '12/1/', '1/1/']
    gastosPorPessoa = Expense.query.filter_by(user_id=current_user.user_id).all()

    for indice, data in enumerate(series_dates):
        if indice == 12:
            anoAtual += 1
            series_dates[indice] += str(anoAtual)
        else:
            series_dates[indice] += str(anoAtual)

    print(series_dates)
    
    for gastos in gastosPorPessoa:
        series_values[datetime.strptime(str(gastos.expense_date), "%Y-%m-%d").date().month-1] += float(gastos.amount)


    return jsonify({'series_values': series_values, 'series_dates': series_dates, 'mesAtual': mesAtual})