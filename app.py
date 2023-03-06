from flask import Flask, render_template, url_for
from markupsafe import escape

print(help(escape)) 


app = Flask(__name__)
app.static_folder = 'static'
app.debug = True

#set the rule for redirect

app.add_url_rule('/favicon.ico', redirect_to = url_for("static", filename='favicon.ico'))
print("passed")

#to enable debug
#flask --app app run --debug
#memories
#there will be a database connected
#

print(type(f'post'))


@app.route('/')
def index():
	return render_template("index-2.html")


@app.route("/<name>")
def hello(name):
	print("called")
	print({escape(name)})
	return f"Hello, {escape(name)}!"


@app.route("/user/<username>")
def show_user_profile(username):
	return f'User {escape(username)}'


@app.route("/data/<int:col_number>")
def ge_col(col_number):
	return f'User {escape(username)}'


@app.route("/post/<int:post_id>")
def show_post(post_id):
	return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return f'Subpath {escape(subpath)}'

@app.route('/favicon.ico')
def get_favicon():
	#favicon is located in assets
	#process the favicon
	loc = os.path.join(app.root_path, "static")
	m = 'image/vnd.microsoft.icon'
	return send_from_directory(loc, 'favicon.ico', mimetype = m)

@app.route('/projects/')
def projects():
	return 'The project page'


@app.route('/path/')
@app.route('/about/')
def about():
	return '<br><h2>The about page</h2>'


		
		






