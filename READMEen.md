
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
project/
│   main.py
│   create_db.py
│   config.py
│   README.md
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
| ![Home](ыcreenshots/home.png) | ![Registration](screenshots/registration.png) |

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

