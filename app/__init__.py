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
	
	from app.api.auth import bp as auth_bp
	app.register_blueprint(auth_bp, url_prefix='/auth')
	
	from app.api.questions import bp as questions_bp
	app.register_blueprint(questions_bp, url_prefix='/questions')

	return app