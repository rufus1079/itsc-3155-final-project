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
    
    def delete_post(self, id):
        post = Post.query.filter(Post.id == id)
        db.session.delete(post)
        db.session.commit()
        return post

    def update_post(self, id, title, content):
        post = Post.query.filter(Post.id == id)
        post.title = title
        post.content = content
        db.session.commit
        

# Singleton to be used in other modules
post_repository_singleton = post_repository()