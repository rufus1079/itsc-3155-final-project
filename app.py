from flask import Flask, render_template, request
from src.models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:@localhost:5432/Final_project_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/user_login')
def user_login():
    return render_template('user_login.html')

@app.get('/sign_up')
def sign_up():
    return render_template('register.html')

@app.get('/posts')
def list_all_posts():
    return render_template('list_all_posts.html')

@app.get('/posts/<int:post_id>')
def get_single_post(post_id):
    return render_template('post.html')

@app.get('/profile/<int:user_id>')
def get_single_user(user_id):
    return render_template('profile.html')

@app.post('/register')
def register():
    pass

@app.post('/posts')
def create_post():
    pass

@app.get('/posts/search')
def search_posts():
    return render_template('post_search.html')


