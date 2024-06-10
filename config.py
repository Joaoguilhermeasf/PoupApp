SECRET_KEY = 'ryanzada'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'postgresql',
        usuario = 'postgres',
        senha = '9933',
        servidor = '127.0.0.1',
        database = 'poupapp'
    )

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'lucasfernandess203@gmail.com'
MAIL_PASSWORD = 'pvaj ncgs elgm ovnp'