from flask import Flask, render_template, redirect, url_for, request
from forms import UserForm, RegForm

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def index():
    form = UserForm()
    return render_template('index.html', form=form)


@app.route('/cadastrar/', methods=['GET', 'POST'])
def cadastrar():
    form = RegForm()
    if request.method == 'POST':
        return 'CADASTRADO'

    return render_template('cadastrar.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)