from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}'

# 1)  what will `http://localhost:5000` page return ?
# 2) what will `http://localhost:5000/about` return ?
# 