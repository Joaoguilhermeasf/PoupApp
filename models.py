from main import db

class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer(), primary_key=True)
    user_login = db.Column(db.String(60), nullable=False)
    user_pass = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False)
    user_firstname = db.Column(db.String(255), nullable=False)
    user_lastname = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<user_id: %r>' % self.user_id