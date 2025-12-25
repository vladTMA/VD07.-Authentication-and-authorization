# config.py
import os

class Config:
    # Секретный ключ для защиты форм и сессий
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'

    # Путь к базе данных
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'

    # Отключаем лишние уведомления SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
