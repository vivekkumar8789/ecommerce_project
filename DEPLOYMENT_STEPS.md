# E-Shop - Free Deployment Options

Your Django ecommerce project is ready for deployment! Here are the best free hosting options:

## ⭐ Recommended: PythonAnywhere (Easiest for Django)

### Why PythonAnywhere?
- Specifically designed for Python/Django
- Free tier includes: 100 MB database, 512 MB static files
- No credit card required
- Simple web interface (no command line needed)
- Free .pythonanywhere.com domain

### Deployment Steps:

#### 1. Sign up for free account
```
Visit: https://www.pythonanywhere.com
Create account (use your email)
Verify email
```

#### 2. Upload your project
```
1. Login to dashboard
2. Click "Files" tab
3. Click "Upload a file"
4. Upload your entire ecommerce_project folder
5. Extract it
```

#### 3. Create a Web App
```
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.11 (or latest)
```

#### 4. Configure WSGI (Web Server Gateway Interface)
```
1. After creating web app, find "WSGI configuration file"
2. Open the WSGI file
3. Replace content with:
```

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

#### 5. Install Dependencies
```
1. In Web tab, scroll to "Consoles"
2. Click "Start a new console"
3. Run command:
   pip install django pillow gunicorn
```

#### 6. Collect Static Files
```
1. In console, run:
   cd /home/YOUR_USERNAME/ecommerce_project
   python manage.py collectstatic --noinput
```

#### 7. Map Static Files
```
1. Back in Web tab
2. Scroll to "Static files" section
3. Add mapping:
   - URL: /static/
   - Directory: /home/YOUR_USERNAME/ecommerce_project/staticfiles
```

#### 8. Reload Web App
```
1. Click green "Reload" button
2. Visit: https://YOUR_USERNAME.pythonanywhere.com/
```

---

## Alternative Option 1: Render.com

### Setup:
1. Visit https://render.com
2. Sign up with GitHub
3. Fork your project to GitHub
4. Connect repo to Render
5. Set build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
6. Set start command: `gunicorn ecommerce_project.wsgi:application`
7. Add environment variables

### Free tier includes:
- 0.5 GB RAM
- 0.5 GB disk
- Auto sleep after 15 min inactivity

---

## Alternative Option 2: Fly.io

### Setup:
1. Visit https://fly.io
2. Sign up (requires credit card for verification)
3. Install `flyctl` CLI
4. Run: `fly launch`
5. Deploy: `fly deploy`

### Free tier includes:
- 3 shared-cpu-1x 256MB VMs
- 160GB monthly bandwidth

---

## Important Production Notes

### 1. Database
Current project uses SQLite (local file database)
- For production, data resets when app restarts
- For persistent data, upgrade to PostgreSQL

### 2. Static Files
Ensure static files are collected before deployment:
```bash
python manage.py collectstatic --noinput
```

### 3. Environment Variables
Set these in your platform's environment settings:
```
DEBUG=False
ALLOWED_HOSTS=your-domain.pythonanywhere.com
SECRET_KEY=your-secret-key-from-settings.py
```

### 4. HTTPS/SSL
- PythonAnywhere provides free SSL
- Check "Force HTTPS" in Web tab

---

## Quick Checklist Before Deployment

- [ ] requirements.txt created
- [ ] Static files collected
- [ ] settings.py configured for production
- [ ] .gitignore file created
- [ ] No sensitive data in code
- [ ] Database backed up (if needed)
- [ ] ALLOWED_HOSTS updated

---

## Troubleshooting

### "ModuleNotFoundError" on deploy
→ Make sure all dependencies are in requirements.txt

### Static files not loading
→ Run: `python manage.py collectstatic --noinput`

### 500 Internal Server Error
→ Check error logs in your hosting platform
→ Verify WSGI configuration
→ Check ALLOWED_HOSTS setting

### Database not persisting
→ Consider upgrading to PostgreSQL add-on

---

## Support Links

- Django Documentation: https://docs.djangoproject.com
- PythonAnywhere Help: https://help.pythonanywhere.com
- Render Documentation: https://docs.render.com
- Fly.io Documentation: https://fly.io/docs

---

**Your project is production-ready! Choose an option above and deploy in minutes.** 🚀
