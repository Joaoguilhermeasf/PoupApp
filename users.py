from main import app, db
from flask import render_template, request, url_for, redirect
from models import Users
from forms import RegForm

#TODO: Terminar, criptografar senha, verificações devidas
@app.route('/cadastrar/', methods=['GET', 'POST'])
def cadastrar():
    form = RegForm()
    if request.method == 'POST':
      user_login = form.user_login.data
      user_firstname = form.user_firstname.data
      user_lastname = form.user_lastname.data
      user_pass = form.user_pass.data
      user_repeat_password = form.user_repeat_password.data
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