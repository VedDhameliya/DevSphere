# DevSphere — Application Architecture

## 1. Project Overview

DevSphere is a developer collaboration platform designed for college students and student teams.

The platform will allow users to:
- Register and log in.
- Create and manage developer profiles.
- Create projects and teams.
- Assign and manage tasks.
- Communicate through chat.
- Manage platform activities through an admin dashboard.

## 2. Technology Stack

- Backend: Python and Flask
- Frontend: HTML, CSS, Bootstrap, JavaScript
- Database: PostgreSQL
- ORM: Flask-SQLAlchemy
- Authentication: Flask-Login
- Database migrations: Flask-Migrate
- Testing: pytest
- Version control: Git and GitHub

## 3. Application Architecture

DevSphere will use a modular monolithic architecture.

All features will be developed inside one Flask application, but each feature will have its own module.

The application will contain:
- Authentication and profiles
- Projects and teams
- Task management
- Chat and admin dashboard

## 4. Team Responsibilities

### Team 1 — Authentication and Profiles
Responsible for:
- User registration
- Login and logout
- User profiles
- Authentication and access control

### Team 2 — Projects and Teams
Responsible for:
- Project creation and management
- Team creation and management
- Team membership
- Project-team relationships

### Team 3 — Task Management
Responsible for:
- Creating tasks
- Assigning tasks to team members
- Updating task status
- Managing task deadlines

### Team 4 — Chat and Admin
Responsible for:
- Project/team chat
- Message history
- Admin dashboard
- Administrative operations

## 5. Shared Database Models

The application will use the following shared models:

- User
- Profile
- Team
- TeamMembership
- Project
- ProjectMembership
- Task
- Message

Shared models and relationships must be agreed upon before feature implementation.

## 6. Development Workflow

- All development will take place on separate Git branches.
- No team will commit directly to main.
- Each feature will be submitted through a Pull Request.
- Changes must be reviewed before merging.
- Automated tests must pass before merging.
- Teams will coordinate shared code and database changes.

## 7. Parallel Development

All four teams may develop their assigned features simultaneously after the shared foundation is established.

Teams must follow the agreed folder structure, database conventions, and application interfaces.

## 8. Integration

All features will be integrated into the main branch through Pull Requests.

The complete application will be tested after integration to verify that all features work together.