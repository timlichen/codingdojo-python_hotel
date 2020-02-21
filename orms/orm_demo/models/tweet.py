from core import db, likes_table
from sqlalchemy.sql import func

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    
    # One to many relationship
    author_id = db.Column(db.Integer,
                          db.ForeignKey("user.id", ondelete="cascade"), nullable=False)
    author = db.relationship('User', foreign_keys=[author_id], backref='user_tweets')

    # many to many relationship to users
    users_who_like_this_tweet = db.relationship('User', secondary=likes_table)