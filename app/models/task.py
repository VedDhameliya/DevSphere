
from app.extensions import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)

    status = db.Column(
        db.String(20),
        nullable=False,
        default="todo"
    )

    project_id = db.Column(
        db.Integer,
        db.ForeignKey("projects.id"),
        nullable=False
    )

    assigned_to = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )
