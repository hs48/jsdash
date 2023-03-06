class Analysis:
	def __init__(self, name, age):
		app = Flask(__name__)
		app.static_folder = 'static'
		app.debug = True
		#to enable debug
		#flask --app app run --debug
		@app.route('/')
		def index():
			return render_template("index-2.html")


		"""
		@app.route("/<name>")
		def hello(name):
			return f"Hello, {escape(name)}!"

		@app.route("/user/<username>")
		def show_user_profile(username):
			return f'User {escape(username)}'

		@app.route("/post/<int: post_id>")
		def show_post(post_id):
			return f'Post {post_id}'
		"""

		@app.route('/path/<path:subpath>')
		def show_subpath(subpath):
			return f'Subpath {escape(subpath)}'

		@app.route('/projects/')
		def projects():
			return 'The project page'

		@app.route('/about/')
		def about():
			logo = ""
			c = "H"
			thickness = 5
			for i in range(thickness):
    				logo += "\n" + (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)
			for i in range(thickness+1):
    				logo += "\n" +(c*thickness).center(thickness*2)+(c*thickness).center(thickness*6) 
			for i in range((thickness+1)//2):
    				logo += "\n" +(c*thickness*5).center(thickness*6) 
			for i in range(thickness+1):
    				logo += "\n" +(c*thickness).center(thickness*2)+(c*thickness).center(thickness*6) 
			for i in range(thickness):
    				logo += "\n" +((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)
			return f'<br><h2>The about page <br> {logo}</h2>'
		