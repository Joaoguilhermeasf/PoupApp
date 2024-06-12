from main import app, db
from flask import render_template, request, url_for, redirect, session
from models import Users
from forms import RegForm, UserForm, ResetarForm, ResetarSenhaForm
from flask_login import login_user, logout_user, login_required
from flask_login import UserMixin
from flask_bcrypt import check_password_hash,generate_password_hash
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

mail = Mail(app)
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

class User(UserMixin):
    def __init__(self, user_id, user_login, user_firstname, user_lastname, user_pass, user_email, user_access_level):
        self.user_id = user_id
        self.user_login = user_login
        self.user_firstname = user_firstname
        self.user_lastname = user_lastname
        self.user_pass = user_pass
        self.user_email = user_email
        self.user_access_level = user_access_level

    def get_user_id(self):
        return (self.user_id)

    def get_id(self):
           return (self.user_login)

    def get_access_level(self):
        return (self.user_access_level)

    @staticmethod
    def get(login):
        print('User login: ',login)
        user_record = Users.query.filter_by(user_login=login).first()
        if user_record:
            return User(user_record.user_id, user_record.user_login, user_record.user_firstname, user_record.user_lastname, user_record.user_pass, user_record.user_email, user_record.user_access_level)
        return None

#TODO: Terminar, criptografar senha, verificações devidas
@app.route('/cadastrar/', methods=['GET', 'POST'])
def cadastrar():
    form = RegForm()

    if request.method == 'POST' and form.validate():
      user_login = form.user_login.data
      user_firstname = form.user_firstname.data
      user_lastname = form.user_lastname.data
      user_pass = form.user_pass.data
      user_repeat_password = form.user_repeat_password.data
      user_email = form.user_email.data

      if user_pass != user_repeat_password:
        return render_template('cadastrar.html', form=form, error='As senhas devem ser iguais.\nTente novamente.')

      user = Users.query.filter_by(user_email=user_email).first()
      if user:
        return render_template('cadastrar.html', form=form, error='O email já está cadastrado.\nTente novamente.')

      user = Users.query.filter_by(user_login=user_login).first()
      if user:
         return render_template('cadastrar.html', form=form, error='Houve um problema ao tentar se cadastrar.\nTente novamente.')


      new_user = Users(
            user_login=user_login,
            user_firstname=user_firstname,
            user_lastname=user_lastname,
            user_pass=str(generate_password_hash(user_pass).decode('utf-8')),
            user_email=user_email,
      )

      db.session.add(new_user)
      db.session.commit()
      #print(f"{user_login} {user_firstname} {user_lastname} {user_email}")
      session['success'] = 'Usuário cadastrado com sucesso.'
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
                log_user = User(user.user_id, user.user_login, user.user_firstname, user.user_lastname, user.user_pass, user.user_email, user.user_access_level)
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


@app.route('/resetar_senha/', methods=['GET', 'POST'])
def resetar_senha():
    form = ResetarForm()

    if form.validate_on_submit():
        email = form.email.data
        token = s.dumps(email, salt='poupapp-recuperar-senha')
        link = url_for('resetar_token', token=token, _external=True)
        corpo_email = render_template('template_email.html', link=link)
        msg = Message('PoupApp: Recuperação de Senha', sender='poupapp.info@gmail.com', recipients=[email])
        msg.html = corpo_email
        mail.send(msg)

        return redirect(url_for('login'))
    return render_template('resetar_senha.html', form=form)

@app.route('/resetar_senha/<token>', methods=['GET', 'POST'])
def resetar_token(token):
    try:
        email = s.loads(token, salt='poupapp-recuperar-senha', max_age=3600)
    except:
        return redirect(url_for('resetar_senha'))

    form = ResetarSenhaForm()
    if form.validate_on_submit():
        if email:
            user = Users.query.filter_by(user_email=email).first()
        else:
            return redirect(url_for('login', error='Email inválido.\nTente novamente.'))

        if user:
            user.user_pass = str(generate_password_hash(form.password.data).decode('utf-8'))
            db.session.commit()
            session['success'] = 'Senha alterada com sucesso.'
            return redirect(url_for('login'))

        return redirect(url_for('login', error='Usuário não encontrado com esse email.\nTente novamente.'))
    return render_template('resetar_token.html', form=form)

@app.route('/deslogar')
@login_required
def deslogar():
    print('Saindo da conta...')
    logout_user()
    print('Conta deslogada!')
    return redirect(url_for('index', error=""))