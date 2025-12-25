# routes.py
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required

from app import app, db, bcrypt
from app.models import User
from app.forms import RegistrationForm, LoginForm, EditProfileForm

import os
from werkzeug.utils import secure_filename


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Успешная регистрация!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash("Введены неверные данные", "danger")

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html')

@app.route('/account/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()

    if form.validate_on_submit():

        # Обновление имени и email
        current_user.username = form.username.data
        current_user.email = form.email.data

        # Обновление пароля
        if form.new_password.data:
            hashed = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
            current_user.password = hashed

        # Обновление аватара
        if form.avatar.data:
            filename = secure_filename(form.avatar.data.filename)
            avatar_path = os.path.join(app.root_path, 'static/avatars', filename)
            form.avatar.data.save(avatar_path)
            current_user.avatar = filename

        db.session.commit()
        flash('Профиль обновлён!', 'success')
        return redirect(url_for('account'))

    # Заполняем форму текущими данными
    form.username.data = current_user.username
    form.email.data = current_user.email

    return render_template('edit_profile.html', form=form)



