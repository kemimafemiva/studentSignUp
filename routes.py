from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.security import generate_password_hash
from models import User
from repo import save_user, get_user_by_username

user_bp = Blueprint('user', __name__)
sign_up_page = 'sign_up_page.html'

@user_bp.route('/')
def home():
    return render_template('index.html')

@user_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        faculty = request.form.get('faculty')
        department = request.form.get('department')
        level_raw = request.form.get('level')

        if not username or not password:
            flash('All fields are required.', 'error')
            return render_template(sign_up_page, username=username, email=email, faculty=faculty,
                       department=department, level=level_raw)
        
        if get_user_by_username(username):
            flash('Username is taken. Please try with another username', 'warning')
            return render_template(sign_up_page, username=username, email=email, faculty=faculty,
                       department=department, level=level_raw)

        if not level_raw or not level_raw.isdigit() or not (1 <= int(level_raw) <= 4):
            flash('Level must be between 1 and 4.', 'error')
            return render_template(sign_up_page, username=username, email=email, faculty=faculty,
                       department=department, level=level_raw)

        hashed_pw = generate_password_hash(password)
        user = User(
            username=username,
            email=email,
            password=hashed_pw,
            faculty=faculty,
            department=department,
            level=int(level_raw)
        )
        save_user(user)
        flash("Signup successful!", 'success')
        return render_template(sign_up_page, username='', email='', faculty='', department='', level='')
    
    return render_template(sign_up_page)
