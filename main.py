from flask import Flask, render_template
from forms import UserForms

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def index():
    form = UserForms()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)