from flask import render_template
from app import app
from models import User, Post

@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/posts')
def list_posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)
