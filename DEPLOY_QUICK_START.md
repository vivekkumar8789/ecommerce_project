# 🚀 E-Shop Quick Deployment Reference

## PythonAnywhere (RECOMMENDED - Easiest)

| Step | Action |
|------|--------|
| 1 | Go to https://www.pythonanywhere.com |
| 2 | Create free account |
| 3 | Files tab → Upload `ecommerce_project` folder |
| 4 | Web tab → Add new web app → Manual Python 3.11 |
| 5 | Edit WSGI config (see DEPLOYMENT_STEPS.md) |
| 6 | Start console → `pip install django pillow gunicorn` |
| 7 | Console → `cd /home/USERNAME/ecommerce_project && python manage.py collectstatic --noinput` |
| 8 | Web tab → Add static files mapping: `/static/ → /home/USERNAME/ecommerce_project/staticfiles` |
| 9 | Click Reload button |
| 10 | Visit `https://USERNAME.pythonanywhere.com` |

## Required Files Prepared ✅

- `requirements.txt` - All dependencies
- `Procfile` - For Render/Heroku
- `runtime.txt` - Python version
- `settings_production.py` - Production config
- `.gitignore` - For GitHub
- `staticfiles/` - Collected static files

## Alternative Platforms

### Render.com
1. Fork to GitHub
2. Connect repo
3. Build: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
4. Start: `gunicorn ecommerce_project.wsgi:application`

### Fly.io
1. Install flyctl
2. Run: `fly launch`
3. Run: `fly deploy`

## Key Settings for Production

```
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
STATIC_ROOT = '/path/to/staticfiles'
STATIC_URL = '/static/'
```

## Database Note
Current: SQLite (data resets on app restart)
Recommended: PostgreSQL add-on (for production)

## Files in Project
```
ecommerce_project/
├── requirements.txt          ← Dependencies
├── Procfile                  ← For Render
├── runtime.txt              ← Python version
├── .gitignore               ← For GitHub
├── DEPLOYMENT_STEPS.md      ← Full guide
├── staticfiles/             ← Collected assets
├── store/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── ecommerce_project/
    ├── settings.py
    ├── settings_production.py
    ├── urls.py
    └── wsgi.py
```

## Status Check
Run locally first:
```bash
python manage.py check
python manage.py runserver
```

Visit: http://localhost:8000

---

**Ready to deploy? Start with PythonAnywhere - it's the easiest!** 🎉
