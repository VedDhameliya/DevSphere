from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.extensions import db
from app.models.team import Team
from app.models.project import Project
from app.models.project_membership import ProjectMembership
from app.models.team_membership import TeamMembership

teams_bp = Blueprint("teams", __name__, url_prefix="/teams")


@teams_bp.route("/project/<int:project_id>", methods=["GET"])
@login_required
def list_teams(project_id):
    project = Project.query.get_or_404(project_id)

    membership = ProjectMembership.query.filter_by(
        project_id=project.id,
        user_id=current_user.id
    ).first()

    if project.owner_id != current_user.id and not membership:
        flash("You do not have access to this project.", "error")
        return redirect(url_for("projects.list_projects"))

    teams = Team.query.filter_by(project_id=project.id).all()

    return render_template(
        "teams/list.html",
        project=project,
        teams=teams
    )


@teams_bp.route("/project/<int:project_id>/create", methods=["GET", "POST"])
@login_required
def create_team(project_id):
    project = Project.query.get_or_404(project_id)

    membership = ProjectMembership.query.filter_by(
        project_id=project.id,
        user_id=current_user.id
    ).first()

    if project.owner_id != current_user.id and not membership:
        flash("You do not have access to this project.", "error")
        return redirect(url_for("projects.list_projects"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        if not name:
            flash("Team name is required.", "error")
            return redirect(url_for("teams.create_team", project_id=project.id))

        team = Team(
            name=name,
            description=description,
            project_id=project.id
        )

        db.session.add(team)
        db.session.flush()

        team_membership = TeamMembership(
            user_id=current_user.id,
            team_id=team.id
        )

        db.session.add(team_membership)
        db.session.commit()

        flash("Team created successfully!", "success")
        return redirect(url_for("teams.list_teams", project_id=project.id))

    return render_template("teams/create.html", project=project)