from src.models import db, Users
class user_repository:

    def get_all_users(self):
        users = Users.query.all()
        return users

    def get_user_by_id(self, user_id):
        user = Users.query.get(user_id)
        return user
    
    def get_user_by_username(self, username):
        user = Users.query.filter_by(username=username).first()
        return user

    def create_user(self, username, passwords, email):
        user = Users(username, passwords, email)
        db.session.add(user)
        db.session.commit()
        return user
    
    def search_users(self, username):
        user = Users.query.filter(Users.name.ilike(f'%{username}%')).all()
        return user
    
    def delete_user(self, id):
        user = Users.query.filter(Users.user_id == id)
        db.session.delete(user)
        db.session.commit()
        return user

    def update_user(self, username, password, email):
        user = Users.query.filter(Users.id == id)
        user.username = username
        user.password = password
        user.email = email
        db.session.commit

# Singleton to be used in other modules
user_repository_singleton = user_repository()