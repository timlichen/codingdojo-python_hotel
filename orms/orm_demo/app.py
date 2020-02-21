from core import app, db
from models.user import User
from models.tweet import Tweet

"""
High Level - What is an ORM?

pip install flask-sqlalchemy
pip install flask-migrate
flask db init

intro to modularity

model structures, tables, etc.

"""

@app.route("/create_user")
def create_user():
    # new_user = User(first_name="Tim", last_name="Chen", email="tim@email.com")
    # db.session.add(new_user)
    # db.session.commit()
    
    user = User.query.get(1)
    return 'hey'

@app.route("/create_tweet")
def create_tweet():
    # Join user and tweet - 1-n relationship
    
    # user = User.query.get(1)
    # tweet = Tweet(content="my tweet", author=user.id)
    # tweet = Tweet(content="my tweet", author_id=1)
    
    # db.session.add(tweet)
    # db.session.commit()
    # tweet = Tweet.query.get(1)
    # print(tweet.author.first_name)
    # user = User.query.get(1)

    return "yep"

@app.route("/like_tweet")
def like_tweet():
    # Join User to Tweet
    # Bidirectionality - user -> tweet, tweet -> user
    tweet = Tweet.query.get(1)
    user = User.query.get(1)

    tweet.users_who_like_this_tweet.append(user)
    
    print(user.tweets_this_user_likes)
    print(tweet.users_who_like_this_tweet)

    db.session.commit()

    return "k"

@app.route("/read_tweet")
def read_tweet():
    """
    tweet = Tweet.query.get(1)
    tweets = Tweet.query.all()
    tweets = Tweet.query.filter(content="my tweet").all)()

    user = User.query.get(1)

    user.user_tweets
    tweet.author
    """
    return "yep"

@app.route("/read_tweet")
def update_tweet():
    """
    tweet = Tweet.query.get(1)
    tweet.content = "new tweet content"

    db.session.commit()
    """
    return "yep"

@app.route("/delete_tweet")
def delete_tweet():
    
    """
    tweet = Tweet.query.get(1)
    db.session.delete(tweet)
    db.session.commit()
    """

    return "yep"

@app.route("/follow_user")
def follow_user():
    # n-n relationship, self join
    # https://docs.sqlalchemy.org/en/13/orm/join_conditions.html#self-referential-many-to-many-relationship
    """
    new_user = User(first_name="Tom", last_name="Chan", email="tom@email.com")
    db.session.add(new_user)
    db.session.commit()

    u1 = User.query.get(1)
    u2 = User.query.get(2)

    u1.right_users.append(u2)
    db.session.commit()

    u1.right_users
    u2.left_users

    u1.right_users.remove(u2)
    db.session.commit()

    u1.right_users
    u2.left_users
    """

    return 'hey'

@app.route("/reset_app")
def flush_data():
    tweets = Tweet.query.all()
    users = User.query.all()

    for t in tweets:
        db.session.delete(t)
        db.session.commit() 
    
    for u in users:
        db.session.delete(u)
        db.session.commit() 

    print(Tweet.query.all())
    print(User.query.all())

    return "yolo"
        

if __name__ == '__main__':
    app.run(debug=True)


