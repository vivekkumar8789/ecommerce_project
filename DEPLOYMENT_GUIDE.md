# E-Shop Django Project - Free Deployment Guide

## Option 1: PythonAnywhere (Recommended - Easiest)

### Step 1: Create a free account
1. Visit https://www.pythonanywhere.com/
2. Click "Create a free account"
3. Choose a username (this becomes part of your URL)
4. Verify your email

### Step 2: Upload your project
1. Login to PythonAnywhere
2. Go to "Files" tab
3. Upload your entire `ecommerce_project` folder

### Step 3: Create a web app
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.11+

### Step 4: Configure WSGI file
1. In Web tab, find the WSGI configuration file
2. Replace content with:

```python
import os
import sys

path = '/home/YOUR_USERNAME/ecommerce_project'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ecommerce_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Step 5: Install dependencies
1. In "Web" tab, click "Start a new console"
2. Run:
```bash
pip install django pillow
```

### Step 6: Collect static files
1. In console run:
```bash
cd /home/YOUR_USERNAME/ecommerce_project
python manage.py collectstatic --noinput
```

### Step 7: Configure static files
1. In Web tab, add Static files mapping:
   - URL: `/static/`
   - Directory: `/home/YOUR_USERNAME/ecommerce_project/store/static/`

### Step 8: Reload the web app
1. Click "Reload" button in Web tab
2. Visit: `https://YOUR_USERNAME.pythonanywhere.com/`

---

## Option 2: Render.com (Good Alternative)

### Step 1: Create account
1. Visit https://render.com/
2. Sign up with GitHub or email

### Step 2: Connect GitHub
1. Fork your project to GitHub
2. Connect your GitHub account to Render

### Step 3: Create new web service
1. Click "New +"
2. Select "Web Service"
3. Connect your repository
4. Set build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
5. Set start command: `gunicorn ecommerce_project.wsgi:application`

### Step 4: Set environment variables
1. Add `SECRET_KEY` = Your Django secret key
2. Add `DEBUG` = `False`
3. Add `ALLOWED_HOSTS` = Your render domain

---

## Important Notes

1. **SQLite Database**: Current project uses SQLite which is local file-based. For production, data will reset when app restarts.
2. **Static Files**: Must be collected before deployment
3. **Secret Key**: Should use environment variable in production
4. **ALLOWED_HOSTS**: Must include your domain

Your project is ready! Choose PythonAnywhere for easiest setup.
