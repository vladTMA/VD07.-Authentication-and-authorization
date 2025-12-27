
# **README.md (English Version)**

# Flask Auth App  
A web application featuring user registration, authentication, and profile editing.  
Built with Flask, SQLAlchemy, Flask-Login, Flask-WTF, and Bootstrap.

---

## ✨ Features

- User registration  
- Login / logout  
- Profile editing  
- Change username, email, and password  
- Upload user avatar  
- Avatar displayed on the account page  
- Smooth UI animations  
- Realistic falling snow effect  
- Responsive Bootstrap layout  

---

## 🧩 Tech Stack

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- WTForms
- Bootstrap 5
- SQLite
- CSS animations + JavaScript

---

## 📁 Project Structure

```
---

# 🌟 Flask Auth App  
### Authentication, Authorization & Profile Editing with Avatar Upload

<p align="center">
  <img src="screenshots/home.png" width="600">
</p>

<p align="center">
  <a href="READMEru.md">🇷🇺 Русская версия</a> • 
  <a href="READMEen.md">🇬🇧 English version</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue">
  <img src="https://img.shields.io/badge/Flask-3.0-green">
  <img src="https://img.shields.io/badge/Bootstrap-5-blueviolet">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>

<p align="center">
  <a href="https://hub.docker.com/r/vladtma/flask-auth-app">
    <img src="https://img.shields.io/docker/pulls/vladtma/flask-auth-app?logo=docker&label=Docker%20Hub%20Pulls">
  </a>
</p>

---

## ✨ Overview

A clean and modern Flask application featuring:

- 🔐 User registration & login  
- 👤 Profile editing  
- 🖼 Avatar upload  
- ❄️ Snow animation (JS + CSS)  
- 🎨 Smooth UI effects  
- 📱 Responsive Bootstrap layout  
- 💾 SQLite + SQLAlchemy  
- 🔑 Password hashing (Flask‑Bcrypt)

Полные версии документации доступны по ссылкам выше.

---

## 🎨 Screenshots

| Home | Registration |
|------|--------------|
| ![](screenshots/home.png) | ![](screenshots/registration.png) |

| Login | Account |
|-------|---------|
| ![](screenshots/enter.png) | ![](screenshots/account.png) |

---

## 🚀 Quick Start (Local)

```bash
pip install -r requirements.txt
python create_db.py
python main.py
```

Open:

```
http://127.0.0.1:5000/
```

---

## 🐳 Docker (Local Build)

```bash
docker build -t flask-auth-app .
docker run -p 5000:5000 flask-auth-app
```

---

## 🐳 Docker Hub (Ready-to-use Image)

You can pull the ready-to-use Docker image from Docker Hub:

👉 **https://hub.docker.com/r/vladtma/flask-auth-app**

```bash
docker pull vladtma/flask-auth-app
docker run -p 5000:5000 vladtma/flask-auth-app
```

---

## 📁 Project Structure

```
project/
│   main.py
│   create_db.py
│   config.py
│   README.md
│   requirements.txt
│   Dockerfile
│   docker-compose.yml
│
├── .github/
│   └── workflows/
│           ci.yml
│
├── screenshots/
│       home.png
│       registration.png
│       enter.png
│       account.png
│
└── app/
    │   __init__.py
    │   routes.py
    │   models.py
    │   forms.py
    │
    ├── static/
    │       style.css
    │       snow.js
    │
    │   └── avatars/
    │           default.png
    │
    └── templates/
            base.html
            home.html
            login.html
            register.html
            account.html
            edit_profile.html
```

---

## 👤 Author

**Vladimir**  
📧 vladtma@tutamail.com

---
```

---

## 🚀 Running the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Create the database

```bash
python create_db.py
```

### 3. Start the application

```bash
python main.py
```

The app will be available at:

```
http://127.0.0.1:5000/
```

---

## 🐳 Docker Installation

### 1. Build the Docker image

```bash
docker build -t flask-auth-app .
```

### 2. Run the container

```bash
docker run -p 5000:5000 flask-auth-app
```

### 3. Open the app

```
http://localhost:5000/
```

---

## 🎨 Screenshots

### Main Pages

| Home Page                     | Registration Page |
|-------------------------------|-------------------|
| ![Home](screenshots/home.png) | ![Registration](screenshots/registration.png) |

---

### Additional Pages

| Login Page | Account Page |
|------------|--------------|
| ![Login](screenshots/enter.png) | ![Account](screenshots/account.png) |

---

## 🖼 User Avatar

- Default avatar: `static/avatars/default.png`
- Users can upload a new avatar in the **Edit Profile** section
- Uploaded files are stored in `static/avatars/`
- The filename is stored in the database

---

## ❄️ UI Effects

- Page fade‑in animation  
- Realistic falling snow (JS + CSS)  
- Hover effects for cards  
- Soft winter color theme  

---

## 🔐 Security

- Passwords hashed using Flask-Bcrypt  
- CSRF protection enabled  
- Account and profile editing available only to authenticated users  

---

## 📌 Future Improvements

- Avatar preview before upload  
- Automatic deletion of old avatars  
- Dark mode  
- API integration  
- Docker Compose support  

---

## 👤 Author

Developed by **Vladimir**  
Email: **vladtma@tutamail.com**
```

---

