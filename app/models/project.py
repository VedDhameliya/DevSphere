
from app.extensions import db


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    memberships = db.relationship(
        "ProjectMembership",
        backref="project",
        lazy=True,
        cascade="all, delete-orphan"
    )

    teams = db.relationship(
        "Team",
        backref="project",
        lazy=True
    )

    tasks = db.relationship(
        "Task",
        backref="project",
        lazy=True
    )

    messages = db.relationship(
        "Message",
        backref="project",
        lazy=True
    )
