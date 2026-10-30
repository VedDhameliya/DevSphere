
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import login_required, current_user

from app.extensions import db
from app.models.project import Project

projects_bp = Blueprint("projects", __name__)


@projects_bp.route("/projects")
@login_required
def project_list():
    projects = Project.query.filter_by(
        owner_id=current_user.id
    ).all()

    return render_template(
        "projects/list.html",
        projects=projects
    )


@projects_bp.route("/projects/create", methods=["GET", "POST"])
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
        db.session.commit()

        flash("Project created successfully!", "success")

        return redirect(url_for("projects.project_list"))

    return render_template("projects/create.html")
