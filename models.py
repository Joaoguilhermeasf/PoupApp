from main import db

class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer(), primary_key=True)
    user_login = db.Column(db.String(60), nullable=False)
    user_pass = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False)
    user_firstname = db.Column(db.String(255), nullable=False)
    user_lastname = db.Column(db.String(255), nullable=False)
    user_access_level = db.Column(
        db.Enum('Padrão', 'PRO', name='user_type'),
        nullable=False,
        server_default='Padrão'
    )

    def __repr__(self):
        return '<user_id: %r>' % self.user_id

class Expense(db.Model):
    __tablename__ = 'expenses'

    expense_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.String(255))
    expense_date = db.Column(db.Date, nullable=False, default=db.func.current_date())
    category = db.Column(db.Enum('Compras', 'Alimentação', 'Remédios', 'Lazer', 'Outros', name='expense_category'), nullable=False)

    user = db.relationship('Users', backref=db.backref('expenses', lazy=True))