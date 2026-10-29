from app.extensions import db


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)

    bio = db.Column(db.Text, nullable=True)

    skills = db.Column(db.Text, nullable=True)

    portfolio_url = db.Column(db.String(255), nullable=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=True,
        nullable=False
    )