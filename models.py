from datetime import datetime, timezone
from extensions import db

class User(db.Model):
    __tablename__ = 'tbl_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    faculty = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    level = db.Column(db.SmallInteger, nullable=False)  # TINYINT UNSIGNED equivalent
    createdAt = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updatedAt = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __init__(self, username, email, password, faculty, department, level):
        self.username = username
        self.email = email
        self.password = password
        self.faculty = faculty
        self.department = department
        self.level = level