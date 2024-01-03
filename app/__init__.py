from flask import Flask, render_template
from config import Config

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	@app.route('/', methods=['GET'])
	def say_hello():
		return 'Hello world!'
	
	@app.route('/index', methods=['GET'])
	def get_index():
		return render_template('index.html')
	
	return app