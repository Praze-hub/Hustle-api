# ArtisanConnect API

A Django REST Framework-based backend for connecting skilled artisans (tailors, barbers, etc.) with potential customers. The platform allows artisans to showcase their skills through portfolios and allows customers to search, rate, and connect with artisans based on location, skill, and quality.

---

## 🚀 Project Idea

Many skilled workers struggle to gain visibility and access to customers. **ArtisanConnect** solves this by allowing artisans to:

- Create a profile and portfolio showcasing their work
- Upload images of completed jobs
- Receive customer ratings and reviews

Customers can:

- Search and filter artisans by location, skill, and rating
- View artisan portfolios
- Submit feedback and ratings

---

## 🔧 Technologies Used

### 💻 Backend
- **Python 3.8+**
- **Django 4.x**
- **Django REST Framework (DRF)**
- **SimpleJWT** – Token-based authentication
- **dj-rest-auth + allauth** – For social login (Google, Facebook, Twitter)
- **PostgreSQL** – Relational database
- **django-cors-headers** – CORS handling for frontend/backend integration
- **Pillow** – Image uploads
- **django-filter** – Advanced filtering

---

## 📦 Features & Implementation

### ✅ User Authentication
- Custom user model using email as username
- JWT-based login, logout, registration
- Email verification on signup
- Social login with Google (others configurable)

### ✅ Artisan Portfolio
- Artisans can register and create a portfolio
- Portfolios include name, location, skill, and image uploads
- Customers can view artisan portfolios
- File uploads handled with `MultiPartParser` and `ImageField`

### ✅ Ratings and Reviews
- Customers can rate artisans (1–5 stars) and leave a comment
- Each customer can rate an artisan only once (`unique_together` constraint)
- Average rating is calculated and displayed on artisan profiles

### ✅ Search & Filter
- Customers can:
  - Search artisans by `skills`, `location`
  - Filter by minimum rating (`min_rating`)
- Implemented using `django-filter`, `SearchFilter`, and `OrderingFilter`

### ✅ API Documentation
- Swagger or DRF's browsable API for testing endpoints

---

## 🛠 Setup & Run

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/artisanconnect-api.git
   cd artisanconnect-api
