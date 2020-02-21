from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

likes_table = db.Table('likes', 
              db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='cascade'), primary_key=True), 
              db.Column('tweet_id', db.Integer, db.ForeignKey('tweet.id', ondelete='cascade'), primary_key=True))
    