from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField, EmailField

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
    user_pass = PasswordField('Senha: ',[validators.DataRequired()])
    user_repeat_password = PasswordField('Repita a senha: ',[validators.DataRequired()])
    cadastrar = SubmitField('Cadastrar')