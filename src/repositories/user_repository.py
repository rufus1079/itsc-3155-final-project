from src.models import db, User
class user_repository:

    def get_all_users(self):
        users = User.query.all()
        return users

    def get_user_by_id(self, user_id):
        user = User.query.get(user_id)
        return user
    
    def get_user_by_username(self, username):
        user = User.query.filter_by(username = username).first()
        return user

    def create_user(self, username, passwords, email):
        user = User(username, passwords, email)
        db.session.add(user)
        db.session.commit()
        return user
    
    def search_users(self, username):
        user = User.query.filter(User.name.ilike(f'%{username}%')).all()
        return user
    
    def delete_user(self, id):
        user = User.query.filter(User.id == id).delete()
        db.session.commit()
        return user

# Singleton to be used in other modules
user_repository_singleton = user_repository()