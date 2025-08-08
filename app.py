########### Folder structure for our project

# studentSignUp/
# │
# ├── app.py                # Main entry point of the Flask app. Imports necessary files and dependencies to initialize the DB, register routes, and run the app.
# ├── routes.py             # Blueprint for the home and signup page routes, with basic business logic.
# ├── repo.py               # Handles database read and write operations.
# ├── models.py             # Defines the database model for the user.
# ├── db_config.py          # Loads environment variables from .env, creates the DB URL, and configures the database.
# ├── create_table.sql      # SQL script to create the database (if not existing) and the user table.
# ├── requirements.txt      # Lists Python dependencies required by the project.
# ├── Dockerfile            # Instructions for building the Docker image for the Flask app.
# ├── extensions.py         # Initializes Flask extensions, such as SQLAlchemy.
# ├── docker-compose.yml    # Defines and manages the MySQL and Flask services in Docker containers.
# ├── .env                  # Environment variables used for DB connection and Flask config.
# │
# ├── templates/
# │   ├── index.html        # Home page template.
# │   └── sign_up_page.html # Signup page template.
# │
# └── scripts/
#     ├── set_up_mac.sh      # Shell script for macOS: sets up virtualenv, installs requirements, starts Docker, loads env vars, creates MySQL DB & user table, runs the app.
#     └── set_up_windows.bat # Batch script for Windows: same as above for Windows environments.

################################################################################################################################################
# Here is the commented out content of routes.py, so you can see how we used request.form to validate the signup inputs and how generate_password_hash is being used
####################### Commented contents of repo.py for visual reference only starts here
# from flask import Blueprint, render_template, request, redirect, flash
# from werkzeug.security import generate_password_hash
# from models import User
# from repo import save_user, get_user_by_username
# user_bp = Blueprint('user', __name__)
# sign_up_page = 'sign_up_page.html'
# @user_bp.route('/')
# def home():
#     return render_template('index.html')
# @user_bp.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('password')
#         faculty = request.form.get('faculty')
#         department = request.form.get('department')
#         level_raw = request.form.get('level')

#         if not username or not password:
#             flash('All fields are required.', 'error')
#             return render_template(sign_up_page, username=username, email=email, faculty=faculty,
#                        department=department, level=level_raw)
        
#         if get_user_by_username(username):
#             flash('Username is taken. Please try with another username', 'warning')
#             return render_template(sign_up_page, username=username, email=email, faculty=faculty,
#                        department=department, level=level_raw)

#         if not level_raw or not level_raw.isdigit() or not (1 <= int(level_raw) <= 4):
#             flash('Level must be between 1 and 4.', 'error')
#             return render_template(sign_up_page, username=username, email=email, faculty=faculty,
#                        department=department, level=level_raw)

#         hashed_pw = generate_password_hash(password)
#         user = User(
#             username=username,
#             email=email,
#             password=hashed_pw,
#             faculty=faculty,
#             department=department,
#             level=int(level_raw)
#         )
#         save_user(user)
#         flash("Signup successful!", 'success')
#         return render_template(sign_up_page, username='', email='', faculty='', department='', level='')
#     return render_template(sign_up_page)

####################### Commented contents of repo.py for visual reference only ends here
################################################################################################################################################


from flask import Flask
from extensions import db # import initialized SQLAlchemy
from db_config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS # import db connection configurations
from routes import user_bp # import home and signup page routes.

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# SQLAlchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)

# Register all routes
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)