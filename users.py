from main import app, db
from flask import render_template, request, url_for, redirect
from models import Users
from forms import RegForm, UserForm
from flask_login import login_user, logout_user, login_required,current_user
from flask_login import UserMixin
from flask_bcrypt import check_password_hash,generate_password_hash

class User(UserMixin):
    def __init__(self, user_login, user_firstname, user_lastname, user_pass, user_email):
        self.user_login = user_login
        self.user_firstname = user_firstname
        self.user_lastname = user_lastname
        self.user_pass = user_pass
        self.user_email = user_email

    def get_id(self):
           return (self.user_login)

    @staticmethod
    def get(login):
        print('User login: ',login)
        user_record = Users.query.filter_by(user_login=login).first()
        if user_record:
            return User(user_record.user_login, user_record.user_firstname, user_record.user_lastname, user_record.user_pass, user_record.user_email)
        return None

#TODO: Terminar, criptografar senha, verificações devidas
@app.route('/cadastrar/', methods=['GET', 'POST'])
def cadastrar():
    form = RegForm()
    if request.method == 'POST':
      user_login = form.user_login.data
      user_firstname = form.user_firstname.data
      user_lastname = form.user_lastname.data
      user_pass = str(generate_password_hash(form.user_pass.data).decode("utf-8"))
      user_repeat_password = str(generate_password_hash(form.user_repeat_password.data).decode("utf-8"))
      user_email = form.user_email.data

      user = Users.query.filter_by(user_login=user_login).first()
      if user:
         return render_template('cadastrar.html', form=form, error='Houve um problema ao tentar se cadastrar.\nTente novamente.')

      new_user = Users(
            user_login=user_login,
            user_firstname=user_firstname,
            user_lastname=user_lastname,
            user_pass=user_pass,
            user_email=user_email
      )
      db.session.add(new_user)
      db.session.commit()
      #print(f"{user_login} {user_firstname} {user_lastname} {user_email}")
      return redirect(url_for('index'))

    return render_template('cadastrar.html', form=form)

@app.route("/autenticar", methods=['GET', 'POST'])
def autenticar():
    print('Tentando autenticação...')
    if request.method == 'POST':
        form = UserForm(request.form)
        user = Users.query.filter_by(user_login=form.login.data).first()
        if user:
            print('user ok')
            password = check_password_hash(user.user_pass, form.password.data)
            if password:
                print('pass ok')
                log_user = User(user.user_login, user.user_firstname, user.user_lastname, user.user_pass, user.user_email)
                login_user(log_user)
                print('Usuário logado:', user)
                return redirect(url_for('dashboard'))
            else:
                print('Senha incorreta, tente novamente!')
                return redirect(url_for('index', error = "Usuário ou senha incorretos.\nPor favor, tente novamente"))
        else:
            print('Erro de login, tente novamente!')
            return redirect(url_for('index', error = "Erro ao tentar efetuar login.\nPor favor, tente novamente"))

    return redirect(url_for('index'))


@app.route('/deslogar')
@login_required
def deslogar():
    print('Saindo da conta...')
    logout_user()
    form = UserForm()
    print('Conta deslogada!')
    return render_template('index.html', form=form, error="")