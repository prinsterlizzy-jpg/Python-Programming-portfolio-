# CBT System

This project contains a Flask backend and a sample React frontend for a Computer-Based Test (CBT) system.

## Backend
- Located in `/backend`
- Run with Python 3.10+
- Install dependencies: `pip install -r backend/requirements.txt`
- Initialize DB (first run) - database is auto-created by the app
- Start server: `python backend/app.py` (default: http://127.0.0.1:5000)

Default accounts:
- admin / admin123
- student / student123

## Frontend (sample)
- Located in `/frontend`
- Created for use with `create-react-app`
- `npm install` then `npm start`

## Notes
- For mobile upload: use GitHub repo → Add file → Create new file → paste contents → Commit.

.gitignore

__pycache__/
*.pyc
*.db
node_modules/
.env


backend/requirements.txt
Flask==2.3.2
Flask-Cors==3.0.10
werkzeug==2.3.7
openpyxl==3.1.2
