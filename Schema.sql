-- Tabela de Usuarios
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_login VARCHAR(60) NOT NULL,
    user_pass VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    user_firstname VARCHAR(255) NOT NULL,
    user_lastname VARCHAR(255) NOT NULL
);