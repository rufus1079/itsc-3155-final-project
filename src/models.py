from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable = False)
    username = db.Column(db.String(255), nullable =False)
    passwords = db.Column(db.String(255), nullable=False)
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
    user_id = db.Column(db.Integer, db.ForeignKey("user_id"), nullable = False)
    group_id = db.Column(db.Integer, db.ForeignKey("group_id"), nullable = True)
    title = db.Column(db.String(255), nullable = False)
    content = db.Column(db.String(255), nullable = False)

    def __init__(self, user_id: int, post_id: int, group_id: int, title : str, content: str):
        self.user_id = user_id
        self.post_id = post_id
        self.group_id = group_id
        self.title = title
        self.content = content
        
    def __repr__(self) -> str:
        return f'Post(user_id={self.user_id}, post_id={self.post_id}, group_id={self.group_id}, title={self.title}, content ={self.content}'

class Group(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_id"), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey("post_id"), nullable = False)
    group_name = db.Column(db.String(255), nullable = False)
    descript = db.Column(db.String(255), nullable = False)

    def __init__(self, user_id: int, post_id: int, group_id: int, group_name : str, descript: str):
        self.user_id = user_id
        self.post_id = post_id
        self.group_id = group_id
        self.group_name = group_name
        self.descript = descript
        
    def __repr__(self) -> str:
        return f'Group(user_id={self.user_id}, post_id={self.post_id}, group_id={self.group_id}, group_name={self.group_name}, descript={self.descript}'