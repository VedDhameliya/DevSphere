
from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    profile = db.relationship(
        "Profile",
        backref="user",
        uselist=False
    )
    assigned_tasks = db.relationship(
        "Task",
        backref="assignee",
        foreign_keys="Task.assigned_to",
        lazy=True
    )
    sent_messages = db.relationship(
        "Message",
        backref="sender",
        lazy=True
    )
