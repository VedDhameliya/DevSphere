from app import models
from flask import Flask, render_template
from app.extensions import db, login_manager, migrate


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-secret-key"

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///devsphere.db"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))
    
    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return render_template("home.html")

    return app