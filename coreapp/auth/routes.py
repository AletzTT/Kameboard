from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from datetime import date

from coreapp import login_manager
from . import auth_bp
from .forms import SignupForm, LoginForm
from .models import User


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    form = SignupForm()
    if current_user.is_authenticated:
        flash('Ya has iniciado sesión')
        return redirect(url_for('public.index'))
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        if not password == form.confirm.data:
            flash('Las Contraseñas no coinciden')
        else:
        
            #Comprobar Correo y nombre de Usuario
            if not User.get_by_username(username) and not User.get_by_email(email):
                user = User(username, email)
                user.set_password(password)
                user.signup_date = date.today()
                user.save()
                flash('Se ha Registrado con Éxito, por favor Inicia Sesión')
                redirect(url_for('auth.login'))
            else:
                flash('El Nombre de Usuario y/o Correo Eléctrónico ya han sido registrados', 'error')

    return render_template("auth/signup_form.html", form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        flash('Ya has iniciado sesión', 'info')
        return redirect(url_for('public.index'))
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.get_by_username(username)
        if user is not None:
            if user.check_password(password):
                login_user(user)
                flash(f'Bienvenido {user.username}', 'info')
                return redirect(url_for('admin.dashboard'))
            else:
                flash('La contraseña es incorrecta', 'error')
        else:
            flash(f'No existe el usuario {username}', 'error')

    return render_template("auth/login_form.html", form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Se ha cerrado la sesión', 'info')
    return redirect(url_for('public.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))