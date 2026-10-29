from app import create_app
from app.extensions import db
from app.models import User, Profile,Project,ProjectMembership,Team,Task, Message,TeamMembership
def test_model_foreign_keys():
    app = create_app()
    assert TeamMembership.__tablename__ == "team_memberships"
    assert "team_memberships" in db.metadata.tables 

    with app.app_context():
        assert "owner_id" in Project.__table__.columns

        assert Profile.__tablename__ == "profiles"

        assert "profiles" in db.metadata.tables

        assert ProjectMembership.__tablename__ == "project_memberships"

        assert "project_memberships" in db.metadata.tables
        
        assert "users.id" in {
            str(foreign_key.target_fullname)
            for foreign_key in Project.__table__.columns["owner_id"].foreign_keys
        }

        assert "projects.id" in {
            str(foreign_key.target_fullname)
            for foreign_key in Team.__table__.columns["project_id"].foreign_keys
        }

        assert "projects.id" in {
            str(foreign_key.target_fullname)
            for foreign_key in Task.__table__.columns["project_id"].foreign_keys
        }

        assert "users.id" in {
            str(foreign_key.target_fullname)
            for foreign_key in Task.__table__.columns["assigned_to"].foreign_keys
        }

        assert "projects.id" in {
            str(foreign_key.target_fullname)
            for foreign_key in Message.__table__.columns["project_id"].foreign_keys
        }

        assert "users.id" in {
            str(foreign_key.target_fullname)
            for foreign_key in Message.__table__.columns["sender_id"].foreign_keys
        }
