# studentSignUp
A simple Flask web student signup application with the following features:

- Homepage with Bootstrap styling
- Signup form with username and password
- Form validation using `request.form`
- MySQL database integration hosted on docker
- Password hashing using `Werkzeug`
- Requirements specified in `requirements.txt`
- MySQL table creation via `create_table.sql`
- Environment configuration via `.env`

---

## Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Git

---

## Folder Structure

```
studentSignUp/
│
├── app.py
├── routes.py
├── repo.py
├── models.py
├── db_config.py
├── create_table.sql
├── requirements.txt
├── Dockerfile
├── extensions.py
├── docker-compose.yml
├── .env
│
├── templates/
│   ├── index.html
│   ├── signup.html
│
└── scripts/
    ├── set_up_mac.sh
    └── set_up_windows.bat
```

---

## Setup Instructions

### Clone the Repository

```
git clone https://github.com/kemimafemiva/studentSignUp.git
cd studentSignUp
```

---

## Environment Variables

Create a `.env` file in root with:

```
MYSQL_USER=youruser              # replace with your user
MYSQL_PASSWORD=yourpassword      # replace with your password
MYSQL_ROOT_PASSWORD=yourrootpw   # replace with root password
MYSQL_DATABASE=students_db
MYSQL_HOST=mysql
MYSQL_PORT=3307

FLASK_ENV=development
FLASK_APP=app.py
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5002
```

> These are loaded via `dotenv` in `db_config.py`.

---

## Running the App

### Mac/Linux

```
chmod +x scripts/set_up_mac.sh
./scripts/set_up_mac.sh
```

### Windows (Command Prompt)

```
scripts\set_up_windows.bat
```

> This will:
> - Create a virtual environment
> - Install dependencies
> - Start Docker containers
> - Wait for MySQL to initialize
> - Create tables via `create_table.sql`
> - Launch the Flask app

---

## MySQL Database

The MySQL instance is defined in `docker-compose.yml` and configured via the `.env` file.

- Hostname (inside container): `mysql`
- Port (from `.env`): `3307`
- Table schema: `create_table.sql`

---

## Sample Signup Form Fields

- Username
- Email
- Password
- Faculty
- Department
- Level (1–4 only)

---

## To Stop the App

```
docker-compose stop
```

Or to clean everything:

```
docker-compose down -v
```

---

## Notes

- Passwords are securely hashed using `generate_password_hash` from `Werkzeug`.
- Flash messages are used for displaying feedback to users.
- `create_table.sql` is the authoritative schema for `tbl_user`.

---

## Example Usage

Visit:  
 `http://localhost:5002` — Homepage  
 `http://localhost:5002/signup` — Signup form