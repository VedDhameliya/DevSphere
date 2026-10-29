
from app.extensions import db


class TeamMembership(db.Model):
    __tablename__ = "team_memberships"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    team_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.id"),
        nullable=False
    )

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "team_id",
            name="unique_user_team_membership"
        ),
    )
    user = db.relationship(
        "User",
        backref="team_memberships"
    )
