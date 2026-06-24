# Deployment Guide

This guide covers deploying **My Auto Prac** to various cloud platforms.

## Table of Contents

1. [Render.com](#rendercom-recommended)
2. [PythonAnywhere](#pythonanywhere)
3. [Railway.app](#railwayapp)
4. [Heroku](#heroku)
5. [AWS](#aws)
6. [Environment Variables](#environment-variables)
7. [Database Setup](#database-setup)
8. [Troubleshooting](#troubleshooting)

---

## Render.com (RECOMMENDED) ⭐

Render.com is the easiest and most reliable option for deploying Flask apps with a free tier.

### Prerequisites

- GitHub account
- Code pushed to GitHub
- Render.com account

### Deployment Steps

1. **Sign up at Render.com**
   - Visit https://render.com
   - Click "Sign up"
   - Connect with GitHub

2. **Create Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect your GitHub repository
   - Select "My_Automation_demo_app" repo

3. **Configure Service**

   Fill in the following:

   | Field | Value |
   |-------|-------|
   | **Name** | my-auto-prac |
   | **Region** | Your closest region |
   | **Branch** | main |
   | **Runtime** | Python 3 |
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `gunicorn run:app` |

4. **Environment Variables**

   Add these in "Environment" section:
   
   ```
   FLASK_ENV=production
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///my_auto_prac.db
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait 2-5 minutes for deployment
   - Your app will be live at: `https://my-auto-prac.onrender.com`

### Post-Deployment

- Test your app in browser
- Check logs if there are issues
- Set up auto-deploy from main branch (optional)

### Pros & Cons

✅ **Pros:**
- Free tier available
- Easy GitHub integration
- Auto-redeploy on push
- Good documentation

❌ **Cons:**
- Free tier spins down after 15 mins inactivity
- Limited disk space
- No PostgreSQL in free tier

### Cost

- **Free Tier**: Basic web service with limitations
- **Paid Tier**: Starting $7/month for better performance

---

## PythonAnywhere

PythonAnywhere is easy for beginners and ideal for Python applications.

### Prerequisites

- PythonAnywhere account (free or paid)
- Your code

### Deployment Steps

1. **Sign up at PythonAnywhere**
   - Visit https://www.pythonanywhere.com
   - Create account (free plan available)

2. **Upload Your Code**

   Option A: Upload ZIP
   ```bash
   # Create ZIP of your project
   zip -r my_auto_prac.zip my_auto_prac/
   # Upload via PythonAnywhere file browser
   ```

   Option B: Clone from GitHub (Recommended)
   ```bash
   # In PythonAnywhere bash console
   git clone https://github.com/YOUR_USERNAME/My_Automation_demo_app.git
   cd My_Automation_demo_app
   ```

3. **Create Virtual Environment**
   ```bash
   mkvirtualenv my_auto_prac --python=/usr/bin/python3.9
   pip install -r requirements.txt
   ```

4. **Create Web App**
   - Go to "Web apps" tab
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select "Python 3.9"
   - Choose "Flask"

5. **Configure WSGI File**

   Edit WSGI file at `/var/www/your_username_pythonanywhere_com_wsgi.py`:

   ```python
   import sys
   
   path = '/home/your_username/My_Automation_demo_app'
   if path not in sys.path:
       sys.path.insert(0, path)
   
   from run import app as application
   ```

6. **Reload Web App**
   - Go to "Web apps" tab
   - Click "Reload"
   - Your app is live at: `https://your_username.pythonanywhere.com`

### Post-Deployment

- Test at your PythonAnywhere URL
- Configure custom domain (if using paid)
- Set up SSL certificate

### Pros & Cons

✅ **Pros:**
- Free tier generous
- Easy setup
- Great for beginners
- No credit card needed

❌ **Cons:**
- Slower than alternatives
- Limited free tier customization
- Free uses shared server

### Cost

- **Free Tier**: Limited but functional
- **Paid Tier**: Starting $5/month

---

## Railway.app

Railway offers free credits and easy deployment.

### Prerequisites

- GitHub account
- Railway account
- Free credits

### Deployment Steps

1. **Sign up at Railway.app**
   - Visit https://railway.app
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Connect your repository

3. **Configure Project**

   Railway auto-detects Flask/Python:
   - Sets up Python environment
   - Installs dependencies
   - Configures start command

4. **Add Environment Variables**

   In Railway dashboard:
   ```
   FLASK_ENV=production
   SECRET_KEY=your-secret-key-here
   ```

5. **Deploy**
   - Click "Deploy"
   - Wait for build and deployment
   - Get your app URL from Railway dashboard

### Post-Deployment

- Monitor deployments in Railway dashboard
- View logs and metrics
- Set up custom domain (optional)

### Pros & Cons

✅ **Pros:**
- Free $5 monthly credit
- Fast deployment
- Auto-deploys on push
- Good performance

❌ **Cons:**
- Credits run out eventually
- Less beginner-friendly
- Limited free tier docs

### Cost

- **Free Tier**: $5/month credit (runs out)
- **Paid Tier**: Pay-as-you-go pricing

---

## Heroku

**Note:** Heroku removed their free tier in November 2022, but still accepts paid plans.

### Alternative

If you want the Heroku experience at free cost, use Render or Railway instead.

### If Using Paid Heroku

1. **Install Heroku CLI**
   ```bash
   brew tap heroku/brew && brew install heroku
   ```

2. **Login**
   ```bash
   heroku login
   ```

3. **Create App**
   ```bash
   heroku create my-auto-prac
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

5. **Open App**
   ```bash
   heroku open
   ```

---

## AWS

AWS offers free tier with more power but more complexity.

### Prerequisites

- AWS account
- AWS CLI installed
- Elastic Beanstalk knowledge (recommended)

### Using Elastic Beanstalk

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize Project**
   ```bash
   cd my_auto_prac
   eb init -p python-3.9 my-auto-prac
   ```

3. **Create Environment**
   ```bash
   eb create production
   ```

4. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to EB"
   eb deploy
   ```

### Using Docker + EC2

```bash
# Build Docker image
docker build -t my-auto-prac .

# Push to ECR
aws ecr get-login-password | docker login --username AWS --password-stdin YOUR_ECR_URI
docker tag my-auto-prac:latest YOUR_ECR_URI/my-auto-prac:latest
docker push YOUR_ECR_URI/my-auto-prac:latest

# Deploy to EC2 or ECS
# ... (Follow AWS documentation)
```

### Cost

- **Free Tier**: 12 months free t2.micro
- **After Free Tier**: Variable based on usage

---

## Environment Variables

### Required Variables

```bash
# Flask Configuration
FLASK_ENV=production
SECRET_KEY=your-very-secret-key-change-this

# Database (if not using default SQLite)
DATABASE_URL=postgresql://user:pass@host/db

# Optional
DEBUG=False
```

### How to Generate Secret Key

```python
import secrets
print(secrets.token_hex(32))
```

Or use a secure random generator:

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Setting Environment Variables

**Render.com:**
- Go to Service → Environment
- Add variables in UI

**PythonAnywhere:**
- Edit wsgi.py to include variables
- Or use .env file (not recommended)

**Railway:**
- Click Service → Variables
- Add in UI

**Local Development:**
```bash
# Create .env file
echo "FLASK_ENV=development" > .env
echo "SECRET_KEY=dev-key" >> .env

# Load with python-dotenv (automatic in our app)
```

---

## Database Setup

### Local Development

SQLite (default):
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///my_auto_prac.db'
```

### Production

PostgreSQL recommended:

1. **Create PostgreSQL Database**
   
   Via cloud provider (e.g., Railway PostgreSQL add-on)

2. **Set DATABASE_URL**
   ```
   postgresql://username:password@host:5432/database_name
   ```

3. **Update requirements.txt**
   ```
   pip install psycopg2-binary
   echo "psycopg2-binary==2.9.9" >> requirements.txt
   ```

4. **Initialize Database**
   ```python
   from run import app, db
   with app.app_context():
       db.create_all()
   ```

5. **Migrate Data**
   ```bash
   # From local SQLite to PostgreSQL
   # Use db_migrate script or manual copy
   ```

---

## Troubleshooting

### 503 Service Unavailable

**Cause:** App not running or starting up

**Solution:**
- Check logs in deployment dashboard
- Verify all environment variables set
- Ensure dependencies installed
- Check Python version compatibility

### ModuleNotFoundError

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
# Ensure requirements.txt in root
# Verify all dependencies listed
pip install -r requirements.txt

# Check build command in deployment settings
```

### Database Connection Error

**Error:** `Can't connect to database`

**Solution:**
```bash
# Verify DATABASE_URL format
# For PostgreSQL: postgresql://user:pass@host/db
# For SQLite: sqlite:///path/to/db.db

# Check if database exists
# Test connection locally first
```

### Port Already in Use

**Error:** `Address already in use`

**Solution:**
- Change port in run.py or environment variable
- Kill process using port: `lsof -i :5000`

### Static Files Not Loading

**Error:** CSS/JS files return 404

**Solution:**
```bash
# Ensure static/ folder in app directory
# Verify URLs use url_for() helper
# In production, might need to serve with nginx

# In Flask template:
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

### Slow Deploy Time

**Cause:** Large dependencies or slow network

**Solution:**
- Use caching in build process
- Separate dev and production requirements
- Create requirements-prod.txt with only necessary packages

---

## Monitoring & Maintenance

### Log Monitoring

- Check deployment logs regularly
- Set up log alerts (if available)
- Monitor error rates

### Performance Monitoring

- Monitor response times
- Check CPU/Memory usage
- Track database queries

### Updates

- Keep dependencies updated
- Monitor security updates
- Test updates in staging first

---

## Next Steps

1. ✅ Deploy to Render.com (easiest)
2. Set up custom domain
3. Configure SSL certificate
4. Set up monitoring
5. Create backup strategy

---

**Happy Deploying!** 🚀

For platform-specific help:
- Render: https://render.com/docs
- PythonAnywhere: https://www.pythonanywhere.com/help/
- Railway: https://docs.railway.app/
- AWS: https://docs.aws.amazon.com/
