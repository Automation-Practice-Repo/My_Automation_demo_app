# My Auto Prac - Task Management Application

A full-stack Flask web application for managing tasks with user authentication, CRUD operations, and a clean UI.

## Features

✅ **User Management**
- User registration & login
- Secure password hashing
- Session management

✅ **Task Management (All CRUD Operations)**
- Create tasks with title, description, priority, and due date
- Read/View all tasks with filtering
- Update task status (pending, in_progress, completed)
- Delete tasks
- Search and filter tasks

✅ **Dashboard & Statistics**
- Task statistics (total, completed, pending, in_progress)
- Interactive task list
- Real-time search

✅ **REST API**
- Full JSON API for all operations
- Authentication protected endpoints
- Filter, search, and sort capabilities

✅ **Modern UI**
- Responsive design
- Beautiful dashboard
- Form validation

## Project Structure

```
my_auto_prac/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models (User, Task)
│   ├── routes.py            # All routes & API endpoints
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── new_task.html
│   │   └── edit_task.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── script.js
├── run.py                   # Application entry point
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
└── .gitignore

```

## Installation & Setup

### 1. Clone or Extract the Project
```bash
cd my_auto_prac
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python run.py
```

The app will be available at: **http://localhost:5000**

## Usage

### Web Interface
1. **Register** - Create a new account
2. **Login** - Sign in with your credentials
3. **Dashboard** - View all your tasks and statistics
4. **Create Task** - Click "+ New Task" button
5. **Edit/Delete** - Manage existing tasks
6. **Search** - Use the search box to find tasks

### API Endpoints

#### Authentication
- `POST /register` - Create account
- `POST /login` - Login user
- `GET /logout` - Logout user

#### Tasks (Web Routes)
- `GET /dashboard` - View all tasks
- `GET /task/new` - Create task form
- `POST /task/new` - Submit new task
- `GET /task/<id>/edit` - Edit task form
- `POST /task/<id>/edit` - Update task
- `POST /task/<id>/delete` - Delete task

#### Tasks (JSON API)
- `GET /api/tasks` - Get all tasks (with filters: `?status=pending&priority=high&search=text`)
- `POST /api/tasks` - Create task (JSON)
- `GET /api/tasks/<id>` - Get single task
- `PUT /api/tasks/<id>` - Update task (JSON)
- `DELETE /api/tasks/<id>` - Delete task
- `GET /api/stats` - Get statistics

### Example API Request

```bash
# Get all pending tasks
curl http://localhost:5000/api/tasks?status=pending

# Create a new task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Task",
    "description": "Task description",
    "priority": "high",
    "due_date": "2026-12-31T10:00:00"
  }'

# Update a task
curl -X PUT http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'

# Delete a task
curl -X DELETE http://localhost:5000/api/tasks/1
```

## Database

The application uses SQLite by default (file: `my_auto_prac.db`). The database is automatically created on first run.

### Models
- **User**: id, username, email, password_hash, created_at, tasks
- **Task**: id, title, description, status, priority, user_id, created_at, updated_at, due_date

## Deployment to Cloud

### Deploy to Heroku

1. **Install Heroku CLI**
   ```bash
   brew tap heroku/brew && brew install heroku
   ```

2. **Create Procfile**
   ```bash
   echo "web: gunicorn run:app" > Procfile
   ```

3. **Add gunicorn to requirements.txt**
   ```bash
   echo "gunicorn==21.2.0" >> requirements.txt
   ```

4. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: My Auto Prac"
   git remote add origin https://github.com/username/my_auto_prac.git
   git push -u origin main
   ```

5. **Deploy with Heroku**
   ```bash
   heroku login
   heroku create my-auto-prac
   git push heroku main
   heroku open
   ```

### Deploy to Other Platforms

- **AWS**: Use Elastic Beanstalk or EC2
- **DigitalOcean**: Use App Platform or Droplets
- **PythonAnywhere**: Simple Python hosting
- **Render.com**: Simple deployment

## Development

### Run in Development Mode
```bash
FLASK_ENV=development python run.py
```

### Run Tests
```bash
pytest tests/
```

### Access SQLite Database
```bash
sqlite3 my_auto_prac.db
```

## Configuration

Edit `config.py` to change:
- Database URI
- Secret key
- Session settings
- Debug mode

## Common Issues

### Port 5000 Already in Use
```bash
python run.py --port 5001
```

### Database Locked Error
Delete `my_auto_prac.db` and restart:
```bash
rm my_auto_prac.db
python run.py
```

## Technologies Used

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (development), PostgreSQL (production)
- **Security**: Werkzeug password hashing, Flask-Login sessions

## License

MIT License - Feel free to use for personal and commercial projects

## Support

For issues or questions, please open an issue on GitHub.

---

Happy task management! 🎉
