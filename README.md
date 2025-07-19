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

## Setting up docker
docker build -t hustle .
docker run -p 8000:8000 hustle




