-- Tipo de usuário
CREATE TYPE user_type AS ENUM ('Padrão', 'PRO');
-- Criação do tipo ENUM para categorias de despesas
CREATE TYPE expense_category AS ENUM ('Compras', 'Alimentação', 'Remédios', 'Lazer', 'Outros');

-- Tabela de Usuarios
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_login VARCHAR(60) NOT NULL,
    user_pass VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    user_firstname VARCHAR(255) NOT NULL,
    user_lastname VARCHAR(255) NOT NULL,
    user_access_level user_type NOT NULL DEFAULT 'Padrão'
);

-- Tabela de Gastos
CREATE TABLE expenses (
    expense_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    description VARCHAR(255),
    expense_date DATE NOT NULL DEFAULT CURRENT_DATE,
    category expense_category NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);