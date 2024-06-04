from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField, IntegerField, DateField, BooleanField, RadioField, SelectField, TextAreaField, SelectField

class UserForms(FlaskForm):
    login = StringField('Login: ',[validators.DataRequired(),validators.Length(min=1,max=20)])
    password = PasswordField('Senha: ',[validators.DataRequired()])
    entrar = SubmitField('Entrar')
    cadastrar = SubmitField('Cadastrar')