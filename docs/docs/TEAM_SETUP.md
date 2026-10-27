# DevSphere — Team Setup Guide

Welcome to DevSphere! Follow these instructions to set up the project on your computer.

## Prerequisites

- Git
- Python installed
- Visual Studio Code
- GitHub account with repository access

## 1. Clone the repository

Open GitHub Desktop and clone the DevSphere repository:

https://github.com/VedDhameliya/DevSphere

Open the cloned folder in VS Code.

## 2. Create a virtual environment

Open the VS Code terminal in the project folder and run:

```powershell
python -m venv .venv
```

## 3. Activate the virtual environment

For Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

## 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## 5. Run the application

```powershell
python -m flask --app app run --debug
```

Open the following address in your browser:

http://127.0.0.1:5000

## 6. Run tests

```powershell
python -m pytest
```

## Git workflow

- Always start new work from the latest `main` branch.
- Create a separate branch for each task.
- Commit your changes to your branch.
- Push your branch to GitHub.
- Create a Pull Request to merge into `main`.
- Do not commit directly to `main`.

## Important

- Never commit `.venv/`.
- Never commit `.env` files or passwords.
- Install new dependencies and update `requirements.txt` when adding packages.
