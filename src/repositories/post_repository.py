from src.models import db, User, Post
class post_repository:

    def get_all_posts(self):
        movies = Post.query.all()
        return movies

    def get_post_by_id(self, movie_id):
        movie = Post.query.get(movie_id)
        return movie

    def create_post(self, title, director, rating):
        movie = Post(title, director, rating)
        db.session.add(movie)
        db.session.commit()
        return movie

    def search_posts(self, title):
        movie = Post.query.filter(Post.title.ilike(f'%{title}%')).all()
        return movie


# Singleton to be used in other modules
post_repository_singleton = post_repository()