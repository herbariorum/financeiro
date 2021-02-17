import os
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
# necessário para uploads de imagens
from flask_uploads import configure_uploads, UploadSet, IMAGES

db = SQLAlchemy()
ma = Marshmallow()

# upload de imagens
images = UploadSet('images', IMAGES)

def create_app():
	app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
	app.config.from_pyfile('../config.py')


	with app.app_context():
		db.init_app(app)
		ma.init_app(app)
		
		migrage = Migrate(app, db)
		
		
		from app.pages import pages as pages_blueprint
		app.register_blueprint(pages_blueprint, url_prefix='/pages')	
		
		from app.lancamentos import lancamento as lancamento_blueprint
		app.register_blueprint(lancamento_blueprint, url_prefix='/lancamentos')

		# para upload de imagens
		configure_uploads(app, images)

		@app.route('/')
		@app.route('/index')
		def index():
			return redirect(url_for('pages.home'))


		return app	