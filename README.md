# Hustle 🛠️ – Connect Artisans with Customers

**Hustle** is a platform that empowers local artisans (e.g., tailors, barbers, mechanics) to showcase their work online through personalized portfolios. Customers can easily find and hire trusted artisans in their area. Built with Django Rest Framework and PostgreSQL, containerized using Docker, and deployed on Render.

---

## 🧠 Problem Statement

Many artisans in underserved communities lack digital visibility, while customers find it hard to locate reliable service providers. **Hustle** bridges this gap by:
- Giving artisans a professional online presence.
- Allowing customers to discover artisans based on skills and location.
- Building transparency and trust through ratings and portfolios.

---

## 🌟 Features

### 🧑‍🎨 For Artisans
- Create profile and upload service portfolio
- Add proof of work (images)
- Receive star ratings and reviews
- Secure authentication

### 👥 For Customers
- Search artisans by location and service
- View artisan profiles and ratings
- Rate and review artisans

### ⚙️ Tech/Admin
- API-first architecture with Django Rest Framework
- Admin interface via Django admin
- Dockerized setup with PostgreSQL database
- Render deployment with CI/CD
- Static/media file management

---

## 🧰 Tech Stack

| Layer          | Technology                     |
|----------------|-------------------------------|
| Backend        | Django, Django Rest Framework |
| Database       | PostgreSQL                    |
| Deployment     | Render + Docker               |
| Auth           | JWT / Token-based auth        |
| API Docs       | Swagger / DRF-YASG            |
| Env Mgmt       | `python-decouple` / `environ` |

---

## 🐳 Docker Setup

### Dockerfile
```dockerfile
FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /Hustle

RUN apt-get update && apt-get install -y \
    build-essential libpq-dev libffi-dev gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /Hustle/staticfiles
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh", "-c", "gunicorn core.wsgi:application --bind 0.0.0.0:8000"]

## Project structure
Hustle/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
├── artisans/
├── media/         # Uploaded images
├── staticfiles/   # Collected static files
├── templates/
├── Dockerfile
├── requirements.txt
└── manage.py

