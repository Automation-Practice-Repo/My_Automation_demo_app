# My Auto Prac - Task Management Application

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7.svg)](https://render.com)

A production-ready **full-stack Flask web application** for managing tasks with user authentication, complete CRUD operations, and a responsive user interface.

🚀 **Live Demo**: [https://my-automation-demo-app.onrender.com/](https://my-automation-demo-app.onrender.com/)

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### User Management
- ✅ User registration with email validation
- ✅ Secure login/logout with session management
- ✅ Password hashing with Werkzeug
- ✅ Role-based access control

### Task Management (Full CRUD)
- ✅ **Create** - Add tasks with title, description, priority, and due date
- ✅ **Read** - View all tasks with real-time search and filtering
- ✅ **Update** - Modify task status (pending, in_progress, completed) and details
- ✅ **Delete** - Remove tasks permanently
- ✅ **Filter** - By status, priority, or search keywords
- ✅ **Sort** - By creation date and priority

### Dashboard & Analytics
- ✅ Task statistics (total, completed, pending, in_progress)
- ✅ Quick overview cards
- ✅ Interactive task list with sorting

### REST API
- ✅ Full JSON API for programmatic access
- ✅ Authentication-protected endpoints
- ✅ Advanced filtering and search
- ✅ CORS ready

### Frontend
- ✅ Responsive design (mobile, tablet, desktop)
- ✅ Modern, clean UI with Bootstrap styling
- ✅ Real-time search functionality
- ✅ Form validation

---

## 🛠 Tech Stack

**Backend**
- Flask 2.3.3
- Flask-SQLAlchemy (ORM)
- Flask-Login (Authentication)
- Werkzeug (Security)

**Database**
- SQLite (Development)
- PostgreSQL (Production Ready)

**Frontend**
- HTML5
- CSS3
- Vanilla JavaScript

**Deployment**
- Render.com (Production)
- Gunicorn (WSGI Server)

**Tools & Libraries**
- python-dotenv (Environment Variables)
- email-validator (Email Validation)
- Flask-WTF (Form Protection)

---

## 📁 Project Structure

```
my_auto_prac/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── models.py                # Database models (User, Task)
│   ├── routes.py                # All routes & API endpoints
│   ├── templates/               # HTML templates
│   │   ├── base.html            # Base template
│   │   ├── login.html           # Login page
│   │   ├── register.html        # Registration page
│   │   ├── dashboard.html       # Main dashboard
│   │   ├── new_task.html        # Create task form
│   │   └── edit_task.html       # Edit task form
│   └── static/
│       ├── css/
│       │   └── style.css        # Global styling
│       └── js/
│           └── script.js        # Frontend utilities
├── tests/                       # Unit tests
├── run.py                       # Application entry point
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
├── Procfile                     # Render deployment config
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
├── CONTRIBUTING.md              # Contributing guidelines
└── README.md                    # This file
```

---

## 🚀 Installation

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Virtual environment (recommended)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Automation-Practice-Repo/My_Automation_demo_app.git
   cd my_auto_prac
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file** (optional)
   ```bash
   echo "FLASK_ENV=development" > .env
   echo "SECRET_KEY=your-secret-key-here" >> .env
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Access the app**
   - Open your browser: `http://localhost:3000`
   - Register a new account
   - Start managing tasks!

---

## 📖 Usage

### Web Interface Workflow

1. **Register** - Create a new account with username, email, and password
2. **Login** - Sign in with your credentials
3. **Dashboard** - View all your tasks and statistics
4. **Create Task** - Click "+ New Task" button to add a new task
5. **Edit Task** - Click "Edit" to modify task details or status
6. **Delete Task** - Click "Delete" to remove a task
7. **Search** - Use the search box to find tasks by keyword
8. **Filter** - Sort by status or priority

### Example Workflow

```
1. Register → username: john_doe, email: john@example.com, password: secure123
2. Login → Enter credentials
3. Dashboard → See "0 tasks" initially
4. New Task → Title: "Learn Flask", Priority: "High", Due: Tomorrow
5. View Task → Dashboard shows 1 pending task
6. Edit Task → Change status to "In Progress"
7. Complete Task → Change status to "Completed"
8. View Stats → Dashboard shows "1/1 completed"
```

---

## 🔌 API Documentation

### Base URL
- Development: `http://localhost:3000`
- Production: `https://my-automation-demo-app.onrender.com`

### Authentication Routes

#### Register
```http
POST /register
Content-Type: application/x-www-form-urlencoded

username=john&email=john@example.com&password=secure123&confirm=secure123
```

#### Login
```http
POST /login
Content-Type: application/x-www-form-urlencoded

username=john&password=secure123
```

#### Logout
```http
GET /logout
```

### Task API Routes (JSON)

#### Get All Tasks
```http
GET /api/tasks
Query Parameters:
  - status: pending | in_progress | completed
  - priority: low | medium | high
  - search: keyword

Example:
GET /api/tasks?status=pending&priority=high
```

Response:
```json
[
  {
    "id": 1,
    "title": "Learn Flask",
    "description": "Complete Flask tutorial",
    "status": "pending",
    "priority": "high",
    "created_at": "2026-06-24T10:00:00",
    "updated_at": "2026-06-24T10:00:00",
    "due_date": "2026-06-30T00:00:00"
  }
]
```

#### Create Task
```http
POST /api/tasks
Content-Type: application/json

{
  "title": "Learn Flask",
  "description": "Complete Flask tutorial",
  "priority": "high",
  "due_date": "2026-06-30T10:00:00"
}
```

#### Get Single Task
```http
GET /api/tasks/1
```

#### Update Task
```http
PUT /api/tasks/1
Content-Type: application/json

{
  "title": "Learn Flask Advanced",
  "status": "in_progress",
  "priority": "medium"
}
```

#### Delete Task
```http
DELETE /api/tasks/1
```

#### Get Statistics
```http
GET /api/stats
```

Response:
```json
{
  "total": 10,
  "completed": 5,
  "pending": 3,
  "in_progress": 2,
  "high_priority": 4
}
```

---

## 🌐 Deployment

### Deploy to Render.com (Recommended)

Render.com offers a free tier and is the easiest way to deploy Flask apps.

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/my_auto_prac.git
   git push -u origin main
   ```

2. **Connect to Render**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub
   - Click "New +" → "Web Service"
   - Select your GitHub repository
   - Configuration:
     - **Name**: my-auto-prac
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn run:app`
   - Click "Deploy"

3. **Access your app**
   - Render provides a URL: `https://your-app-name.onrender.com`
   - Your app is now LIVE! 🎉

### Deploy to Other Platforms

**PythonAnywhere**
```bash
# Upload files, create venv, configure WSGI
# Visit: https://www.pythonanywhere.com
```

**Heroku**
```bash
# Note: Free tier deprecated, but still possible with credits
heroku create my-auto-prac
git push heroku main
```

**AWS/Digital Ocean/Others**
- See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions

---

## 💻 Development

### Run in Development Mode
```bash
FLASK_ENV=development python run.py
```

### Debug Mode
```bash
FLASK_DEBUG=1 python run.py
```

### Database Management

**View SQLite Database**
```bash
sqlite3 my_auto_prac.db
```

**Reset Database**
```bash
rm my_auto_prac.db
python run.py  # Creates new database
```

### Run Tests (if available)
```bash
pytest tests/
```

### Code Style
```bash
# Format code
black app/

# Check style
flake8 app/
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit (`git commit -m 'Add amazing feature'`)
5. Push (`git push origin feature/amazing-feature`)
6. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use different port
PORT=8000 python run.py
```

### Database Locked
```bash
# Reset database
rm my_auto_prac.db
python run.py
```

### Dependencies Issue
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Login Not Working
- Check if database exists: `ls -la my_auto_prac.db`
- Verify Flask-Login configuration
- Check browser cookies enabled

---

## 📞 Support

- **Issues**: Open an issue on [GitHub Issues](https://github.com/Automation-Practice-Repo/My_Automation_demo_app/issues)
- **Discussions**: Use [GitHub Discussions](https://github.com/Automation-Practice-Repo/My_Automation_demo_app/discussions)
- **Email**: support@example.com

---

## 📊 Project Statistics

- **Lines of Code**: ~1500
- **Database Tables**: 2 (User, Task)
- **API Endpoints**: 10+
- **HTML Templates**: 7
- **Features**: 20+

---

## 🎉 Acknowledgments

- Flask Community
- Bootstrap CSS Framework
- Render.com for free hosting

---

## 📈 Roadmap

- [ ] Dark mode support
- [ ] Task categories/tags
- [ ] Team collaboration features
- [ ] Email notifications
- [ ] Mobile app (React Native)
- [ ] Advanced analytics
- [ ] Task templates
- [ ] Recurring tasks

---

**Happy Task Managing!** 🚀

Last Updated: June 24, 2026  
Current Version: 1.0.0

