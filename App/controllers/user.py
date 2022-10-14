from App.models import User
from App.database import db

def create_Author(username, fullname, password, email, credentials):
    newAuthor = User(username=username, fullname=fullname, password= password, email=email, credentials=credentials)
    db.session.add(newAuthor)
    db.session.commit()
    return newAuthor

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toJSON() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None