from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField, EmailField, SelectField, DecimalField, DateField, ValidationError

class UserForm(FlaskForm):
    login = StringField('Login: ',[validators.DataRequired(),validators.Length(min=1,max=60)])
    password = PasswordField('Senha: ',[validators.DataRequired()])
    entrar = SubmitField('Entrar')
    cadastrar = SubmitField('Inscrever-se')


class RegForm(FlaskForm):
    user_login = StringField('Usuário: ',[validators.DataRequired(),validators.Length(min=1,max=60)])
    user_firstname = StringField('Nome: ',[validators.DataRequired(),validators.Length(min=1,max=255)])
    user_lastname = StringField('Sobrenome: ',[validators.DataRequired(),validators.Length(min=1,max=255)])
    user_email = EmailField('Email: ', [validators.DataRequired()])
    user_pass = PasswordField('Senha: ', [validators.DataRequired()])
    user_repeat_password = PasswordField('Repita a senha: ',[validators.DataRequired()])
    cadastrar = SubmitField('Cadastrar')

class RegExpenseForm(FlaskForm):
    expense_category = SelectField('Categoria: ',[validators.DataRequired()], choices=[('Compras', 'Compras'),('Alimentação', 'Alimentação'), ('Remédios', 'Remédios'), ('Lazer', 'Lazer'),('Outros', 'Outros')])
    expense_amount = DecimalField('Valor gasto: ', [validators.DataRequired()])
    expense_description = StringField('Descrição: ',[validators.DataRequired(),validators.Length(min=1,max=255)])
    expense_date = DateField('Data do Gasto: ',[validators.DataRequired()])

    cadastrar = SubmitField('Adicionar Gasto')

class ResetarForm(FlaskForm):
    email = EmailField('Email', [validators.DataRequired()])
    submit = SubmitField('Recuperar Senha')

class ResetarSenhaForm(FlaskForm):
    password = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=6)])
    confirm_password = PasswordField('Repita a Senha', [validators.DataRequired(), validators.EqualTo('password')])
    submit = SubmitField('Alterar Senha')