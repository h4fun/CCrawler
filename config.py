from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_RUI']=\
'sqlite:///'+os.path.abspath(os.path.dirname(__file__))

