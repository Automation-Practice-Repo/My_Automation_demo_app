from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    with app.app_context():
        from app import models
        from app.routes import auth_bp, task_bp, api_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(task_bp)
        app.register_blueprint(api_bp)

        db.create_all()

    return app
