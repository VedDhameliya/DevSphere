
from flask import Flask, render_template

from app import models
from app.extensions import db, login_manager, migrate


def create_app():
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devsphere.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    # Team 1: Authentication routes
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    # Team 3: Project routes
    from app.routes.projects import projects_bp
    app.register_blueprint(projects_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

<<<<<<< Updated upstream
    return app
=======
    return app
>>>>>>> Stashed changes
