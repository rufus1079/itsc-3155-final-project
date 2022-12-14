from src.models import db, Post
class post_repository:

    def get_all_posts(self):
        posts = Post.query.all()
        return posts

    def get_post_by_id(self, post_id):
        post = Post.query.get(post_id)
        return post

    def create_post(self, title, content):
        post = Post(title, content)
        db.session.add(post)
        db.session.commit()
        return post

    def search_posts(self, title):
        post = Post.query.filter(Post.title.ilike(f'%{title}%')).all()
        return post


# Singleton to be used in other modules
post_repository_singleton = post_repository()