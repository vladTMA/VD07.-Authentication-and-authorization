# Flask Auth App  
Приложение с регистрацией, авторизацией и редактированием профиля пользователя.  
Проект создан на Flask с использованием SQLAlchemy, Flask-Login, Flask-WTF и Bootstrap.

---

## ✨ Функциональность

- Регистрация пользователя  
- Авторизация / выход из аккаунта  
- Редактирование профиля  
- Изменение имени, email и пароля  
- Загрузка аватара пользователя  
- Отображение аватара в аккаунте  
- Плавные анимации интерфейса  
- Реалистичные снежинки на фоне  
- Адаптивный дизайн на Bootstrap  

---

## 🧩 Стек технологий

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- WTForms
- Bootstrap 5
- SQLite
- CSS-анимации + JavaScript

---

## 📁 Структура проекта

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

## 🚀 Запуск проекта

### 1. Установить зависимости

```bash
pip install -r requirements.txt
```

### 2. Создать базу данных

```bash
python create_db.py
```

### 3. Запустить приложение

```bash
python main.py
```

Приложение будет доступно по адресу:


http://127.0.0.1:5000/
```
```
## 🐳 Установка и запуск через Docker

### 1. Собрать образ

```bash
docker build -t flask-auth-app .
```

### 2. Запустить контейнер

```bash
docker run -p 5000:5000 flask-auth-app
```

### 3. Открыть приложение
```
http://localhost:5000/

```

## 🎨 Скриншоты

| Главная страница | Страница регистрации |
|------------------|----------------------|
| ![Главная](screenshots/home.png) | ![Регистрация](screenshots/registration.png) |

---

### Дополнительно

| Страница входа | Страница аккаунта |
|----------------|-------------------|
| ![Вход](screenshots/enter.png) | ![Аккаунт](screenshots/account.png) |

---

## 🖼 Аватар пользователя

- Файл по умолчанию: `static/avatars/default.png`
- Пользователь может загрузить новый аватар в разделе **Редактирование профиля**
- Файл сохраняется в `static/avatars/`
- Имя файла хранится в базе данных

---

## ❄️ Эффекты и анимации

- Плавное появление страницы (fade-in)
- Реалистичные снежинки (JS + CSS)
- Hover‑эффекты для карточек
- Мягкая зимняя цветовая тема

---

## 🔐 Безопасность

- Пароли хэшируются через Flask-Bcrypt  
- Формы защищены от CSRF  
- Доступ к аккаунту — только для авторизованных пользователей  

---

## 📌 Планы на улучшение

- Предпросмотр аватара перед загрузкой  
- Удаление старого аватара  
- Поддержка тёмной темы  
- Подключение API  
- Docker‑контейнеризация  

---

## 📧 Контакты

Автор: Владимир  
Email: **vladtma@tutamail.com**
```

