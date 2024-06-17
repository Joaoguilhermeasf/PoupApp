SECRET_KEY = 'ryanzada'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'postgresql',
        usuario = 'postgres',
        senha = 'giatech',
        servidor = '127.0.0.1',
        database = 'poupapp'
    )

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'poupapp.info@gmail.com'
MAIL_PASSWORD = 'chqf hege bkjg qncy'