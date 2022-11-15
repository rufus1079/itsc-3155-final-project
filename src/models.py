from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable =False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    def __init__(self, user_id: int, username: str, password: str, email: int):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        
    def __repr__(self) -> str:
        return f'User(user_id={self.user_id}, username={self.username}, password={self.password}, email={self.email})'
    
class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, foreign_key=True)

    def __init__(self, user_id: int, post_id: int):
        self.user_id = user_id
        self.post_id = post_id
        
    def __repr__(self) -> str:
        return f'User(user_id={self.user_id}, post_id={self.post_id}'