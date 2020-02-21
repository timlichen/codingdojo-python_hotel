from core import db, likes_table
from sqlalchemy.sql import func

user_to_user = db.Table("user_to_user",
    db.Column("left_user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("right_user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    # c stands for column 
    right_users = db.relationship("User",
                        secondary="user_to_user",
                        primaryjoin="User.id==user_to_user.c.left_user_id",
                        secondaryjoin="User.id==user_to_user.c.right_user_id",
                        backref="left_users")

    tweets_this_user_likes = db.relationship('Tweet', secondary=likes_table)