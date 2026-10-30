
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.extensions import db
from app.models.project import Project
from app.models.project_membership import ProjectMembership


projects_bp = Blueprint("projects", __name__, url_prefix="/projects")


@projects_bp.route("/")
@login_required
def list_projects():
    projects = Project.query.filter(
        (Project.owner_id == current_user.id) |
        (Project.memberships.any(user_id=current_user.id))
    ).all()

    return render_template("projects/list.html", projects=projects)


@projects_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_project():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        if not name:
            flash("Project name is required.", "error")
            return redirect(url_for("projects.create_project"))

        project = Project(
            name=name,
            description=description,
            owner_id=current_user.id
        )

        db.session.add(project)
        db.session.flush()

        membership = ProjectMembership(
            user_id=current_user.id,
            project_id=project.id,
            role="owner"
        )

        db.session.add(membership)
        db.session.commit()

        flash("Project created successfully!", "success")
        return redirect(url_for("projects.list_projects"))

    return render_template("projects/create.html")

