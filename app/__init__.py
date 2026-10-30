from flask import Flask, render_template

from app import models
from app.extensions import db, login_manager, migrate
from app.routes.auth import auth_bp
from app.routes.tasks import tasks_bp
from app.routes.projects import projects_bp


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devsphere.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Register routes from the different teams.
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(projects_bp)

    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    @app.route("/")
    def home():
        return "Welcome to DevSphere!"

    return app