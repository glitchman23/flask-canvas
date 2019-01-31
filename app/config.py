import os

class Config:
	SECRET_KEY = '92d55cfc39b5c5a115ff84baebd0b834'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	from app.users.routes import users
	from app.main.routes import main

	app.register_blueprint(users)
	app.register_blueprint(main)