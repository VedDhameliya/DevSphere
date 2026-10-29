from app.extensions import db


class ProjectMembership(db.Model):
    __tablename__ = "project_memberships"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    project_id = db.Column(
        db.Integer,
        db.ForeignKey("projects.id"),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        nullable=False,
        default="member"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "project_id",
            name="unique_user_project_membership"
        ),
    )

    user = db.relationship(
        "User",
        backref="project_memberships"
    )
    project = db.relationship(
        "Project",
        backref="memberships"
    )
        