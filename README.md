# Python Developer Portfolio

A production-minded Django portfolio for a fresher software developer. Content is managed through Django Admin, while the public site uses a custom responsive interface built with Django Templates, CSS and lightweight JavaScript.

## Features

- Dynamic profile, skills, projects, education, certifications and achievements
- Project case study pages with editable feature lists and links
- CSRF-protected contact form stored in the database with optional email notification
- Responsive dark developer aesthetic with reduced-motion support
- SEO metadata, `robots.txt`, sitemap and favicon
- SQLite for local development; `DATABASE_URL` or MySQL environment variables for deployment
- WhiteNoise static files, Gunicorn, build script and GitHub Actions checks

## Local setup

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Open `http://127.0.0.1:8000/` and use `/admin/` to add your profile and portfolio content. Add your resume PDF through the Profile record. Do not put real credentials in `.env.example` or source control.

## Production

Set `DEBUG=False`, a long random `SECRET_KEY`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, and either `DATABASE_URL` or the documented MySQL variables. Run `bash build.sh`, then serve `config.wsgi:application` with Gunicorn. Platforms such as Render or Railway can use the included `Procfile` and `build.sh`; use managed PostgreSQL or MySQL rather than SQLite for persistent production data.

### Render deployment

1. Push this folder to a GitHub repository.
2. In Render, choose **New > Blueprint** and select the repository.
3. Render will read `render.yaml`, create the web service and PostgreSQL database, and generate the secret key.
4. After the first deploy, open the service Shell and run `python manage.py createsuperuser`.
5. Add your resume and portfolio images through `/admin/`. For durable uploaded media on a scaled deployment, configure object storage such as S3 or Cloudinary.

## GitHub

```powershell
git init
git add .
git commit -m "Build Django developer portfolio"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your repository URL. Configure deployment secrets in the hosting platform, never in the repository.
