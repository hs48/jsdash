from flask import Flask, render_template, url_for
from markupsafe import escape
from hlogo import logo

app = Flask(__name__)
app.static_folder = 'static'
app.debug = True
#to enable debug
#flask --app app run --debug

@app.route('/')
def index():
	return render_template("index-2.html")


#print(help(app))
#print(help(render_template))
url_chng = url_for

@app.route("/<name>")
def hello(name):
	return f"Hello, {escape(name)}!"


@app.route("/user/<username>")
def show_user_profile(username):
	return f'User {escape(username)}'


@app.route("/post/<int:post_id>")
def show_post(post_id):
	return f'Post {post_id}'
		

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return f'Subpath {escape(subpath)}'


@app.route('/projects/')
def projects():
	return 'The project page'


@app.route('/about/')
def about():
	logo.logo()
	return render_template("about.html")
		