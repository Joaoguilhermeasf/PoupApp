SECRET_KEY = 'ryanzada'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'postgresql',
        usuario = 'postgres',
        senha = '9933',
        servidor = '127.0.0.1',
        database = 'poupapp'
    )