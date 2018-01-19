from flask import Flask
from flask_sqlalchemy import sqlalchemy
import flask_sqlalchemy as fsa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mima@localhost:3306/test'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 10


db = fsa.SQLAlchemy(app)

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def password(self,password):
        # self.password_hash = generate_password_hash(password)
#
    # def verify_password(self,password):
    #     print 'verifying-----'
    #     return check_password_hash(self.password_hash,password)

