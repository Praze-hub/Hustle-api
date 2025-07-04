# 🛠️ Hustle API

A Django-based backend API that helps **artisans** (tailors, barbers, carpenters, etc.) showcase their skills and connect with **customers** looking for trusted service providers.

---

## 🚀 Project Overview

Many skilled individuals lack visibility and customer reach. This platform aims to:

- Let artisans create portfolios to show off past work.
- Allow customers to find artisans by **skill, location, and rating**.
- Enable service **booking and WhatsApp communication**.
- Provide **star rating/reviews** from verified customers.

---

## 🧰 Tech Stack

| Tool/Framework | Purpose |
|----------------|---------|
| **Django** | Web framework |
| **Django REST Framework (DRF)** | API development |
| **Simple JWT** | Authentication |
| **PostgreSQL** | Database |
| **Django AllAuth + dj-rest-auth** | Social & email authentication |
| **django-cors-headers** | CORS handling for frontend |
| **Cloudinary / local uploads** | Image hosting (configurable) |

---

## 🧑‍💻 Features & Implementation

### ✅ Custom User Authentication
- Users sign up with email, password, phone number.
- JWT-based login, logout, and email verification.
- User types: `ARTISAN` and `CUSTOMER`.

### ✅ Artisan Portfolio
- Artisans create a portfolio linked to their user.
- Upload images of previous jobs.
- Auto-generate WhatsApp contact link from phone number.
- View portfolio includes:
  - Full name, skills, location, profile images, reviews.

### ✅ Image Uploads
- DRF with `MultiPartParser` and `FormParser` for image fields.
- PortfolioImage model linked to ArtisanPortfolio.

### ✅ Ratings System
- Only **authenticated customers** can rate artisans.
- Limit: One rating per customer per artisan.
- Average rating and reviews displayed on artisan profile.

### ✅ Search & Filtering
- Customers can search by `skills`, `location`, or rating via query params.
- Powered by DRF’s `SearchFilter` and custom filtering in views.

### ✅ Booking & Communication
- Customers can request service from an artisan.
- Artisan can accept or decline.
- Contact handled through WhatsApp link for now (no in-app messaging).

---

## ⚙️ Local Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/artisan-connect.git
   cd artisan-connect
