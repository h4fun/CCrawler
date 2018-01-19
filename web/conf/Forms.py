# coding=utf-8

from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import  Required,Length,EqualTo,InputRequired,DataRequired
from flask_wtf import FlaskForm

class Login_Form(FlaskForm):

    UserName = StringField('UserName', validators=[Length(min=3,max=15,message=u"用户名长度为3-15个字")])
    UserPass = StringField('UserPass', validators=[Length(min=4,max=18,message=u"请填写密码")])

class RegistForm(FlaskForm):
    UserName = StringField(validators=[Length(min=3,max=15,message=u"len error")])
    UserPass = StringField(validators=[Length(min=6,max=18)])
    UserMail = StringField(validators=[Length(min=6,max=20,message=u"len error")])
    UserPassConfirm = StringField(validators=[Length(min=6,max=18)])
