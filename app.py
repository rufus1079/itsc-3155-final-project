import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, abort, redirect, session
from flask_bcrypt import Bcrypt
from src.models import db
from src.repositories.post_repository import post_repository_singleton
from src.repositories.user_repository import user_repository_singleton
from src.repositories.group_repository import group_repository_singleton

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('APP_SECRET_KEY')

db.init_app(app)


bcrypt = Bcrypt(app)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/user_login')
def user_login():
    return render_template('userlogin.html')

@app.get('/sign_up')
def sign_up():
    return render_template('register.html')

@app.get('/posts')
def list_all_posts():
    all_posts = post_repository_singleton.get_all_posts()
    return render_template('list_all_posts.html', posts = all_posts)

@app.get('/groups')
def list_all_groups():
    all_groups = group_repository_singleton.get_all_groups()
    return render_template('list_all_groups.html', groups = all_groups)

@app.get('/make_post')
def make_post():
    if 'user' not in session:
        return redirect('/user_login')
    return render_template('create_post.html')

@app.get('/make_group')
def make_group():
    if 'user' not in session:
        return redirect('/user_login')
    return render_template('create_group.html')

@app.get('/posts/<int:post_id>')
def get_single_post(post_id):
    post = post_repository_singleton.get_post_by_id(post_id)
    if 'user' in session:
        return render_template('post_auth.html', post = post)
    return render_template('post.html', post = post)

@app.get('/profile/<int:user_id>')
def get_single_user(user_id):
    user = user_repository_singleton.get_user_by_id(user_id)
    if 'user' in session:
        return render_template('profile_auth.html', user = user)
    return render_template('profile.html', user = user)

@app.get('/group/<int:group_id>')
def get_group_user(group_id):
    group = group_repository_singleton.get_group_by_id(group_id)
    if 'user' in session:
        return render_template('group_auth.html', group = group)
    return render_template('group.html', group = group)

@app.post('/register')
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    if username == '' or password == '' or email == '':
        abort(400)

    hashed_bytes = bcrypt.generate_password_hash(password, int(os.getenv('BCRYPT_ROUNDS')))
    hashed_password = hashed_bytes.decode('utf-8')

    existing_user = user_repository_singleton.get_user_by_username(username)
    if existing_user:
        return redirect('/')
    created_user = user_repository_singleton.create_user(username, hashed_password, email)
    return redirect(f'/profile/{created_user.user_id}')

@app.post('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    existing_user = user_repository_singleton.get_user_by_username(username)

    if not existing_user:
        return redirect('/')

    if not bcrypt.check_password_hash(existing_user.password, password):
        return redirect('/')
    
    session['user'] = {
        'user_id': existing_user.user_id
    }

    return redirect('/')

@app.post('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@app.post('/join_group')
def join_group():
    member_key = session['user'].keys()
    member = user_repository_singleton.get_user_by_id(session['users'][member_key[0]])
    group_repository_singleton.join_group(member)
    return redirect('/group/<int:group_id>')

@app.post('/remove_member')
def remove_member(member):
    group_repository_singleton.remove_member(member)
    return redirect('/groups')

@app.post('/create_post')
def create_post():
    user_key = session['user'].keys()
    user_id = session['users'][user_key[0]]
    title = request.form.get('title')
    content = request.form.get('description')
    if title == '' or content == '':
        abort(400)
    created_post = post_repository_singleton.create_post(user_id, title, content)
    return redirect(f'/posts/{created_post.post_id}')

@app.post('/create_group')
def create_group(): 
    name = request.form.get("group_name")
    descript= request.form.get("description")
    user_key = session['user'].keys()
    user_id = session['users'][user_key[0]]
    member = user_repository_singleton.get_user_by_username(user_id)
    if name == '' or descript == '':
        abort(400)
    created_group = group_repository_singleton.create_group(user_id, name, descript, member)
    return redirect(f'/posts/{created_group.group_id}')  

@app.post('/delete_user')
def delete_user(user_id):
    user_repository_singleton.delete_user(user_id)
    session.pop('user')
    return redirect('/')

@app.post('/delete_post')
def delete_post(post_id):
    post_repository_singleton.delete_post(post_id)
    return redirect('/')

@app.post('/delete_group')
def delete_group(group_id):
    group_repository_singleton.delete_group(group_id)
    return redirect('/')

@app.get('/search')
def search():
    found_posts = []
    q = request.form.get('search')
    if q != '':
        found_posts = post_repository_singleton.search_posts(q)
    
    found_groups_by_name = []
    if q != '':
        found_groups_by_name = group_repository_singleton.search_groups_by_name(q)
    
    found_groups_by_descript = []
    if q != '':
        found_groups_by_descript = group_repository_singleton.search_groups_by_descript(q)
    
    found_groups = found_groups_by_name
    for group in found_groups_by_descript:
        if group not in found_groups:
            found_groups.append(group)
    
    found_users = []
    if q != '':
        found_users = user_repository_singleton.search_users(q)
    return render_template('post_search.html', posts=found_posts, groups=found_groups, users=found_users, Search_query=q)



