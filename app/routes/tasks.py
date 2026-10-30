from flask import Blueprint, abort, jsonify
from flask_login import current_user, login_required

from app.models.project import Project
from app.models.project_membership import ProjectMembership
from app.models.task import Task


tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/projects/<int:project_id>/tasks", methods=["GET"])
@login_required
def list_tasks(project_id):
    project = Project.query.get(project_id)

    if project is None:
        abort(404)

    is_owner = project.owner_id == current_user.id

    is_member = ProjectMembership.query.filter_by(
        project_id=project.id,
        user_id=current_user.id,
    ).first() is not None

    if not is_owner and not is_member:
        abort(404)

    tasks = Task.query.filter_by(
        project_id=project.id
    ).order_by(Task.id.desc()).all()

    return jsonify([
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "assigned_to": task.assigned_to,
        }
        for task in tasks
    ])