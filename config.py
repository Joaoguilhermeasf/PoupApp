SECRET_KEY = 'ryanzada'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'postgresql',
        usuario = 'uwm61dodfhfqbcxtcfea',
        senha = 'HN7NnLb7U8ZeUyszPrVUH3RNxgcuLF',
        servidor = 'bnh3np1gwjm3tmxli5ie-postgresql.services.clever-cloud.com',
        database = 'bnh3np1gwjm3tmxli5ie'
    )

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'poupapp.info@gmail.com'
MAIL_PASSWORD = 'chqf hege bkjg qncy'