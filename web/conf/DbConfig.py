from flask import Flask
from flask_sqlalchemy import sqlalchemy
import flask_sqlalchemy as fsa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ky3wamgv@localhost:3306/test'
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

    # def password(self,password):
        # self.password_hash = generate_password_hash(password)
#
    # def verify_password(self,password):
    #     print 'verifying-----'
    #     return check_password_hash(self.password_hash,password)


# if __name__ == '__main__':
    # u=User(username='test1',email='test1@qq.com',password='test1')
    # db.session.add(u)
    # db.session.commit()
