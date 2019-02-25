import os


class Config:
    SECRET_KEY = 'c1b8206999dec363dc25cd24be32743b'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'lslestercayabyab@gmail.com'
    MAIL_PASSWORD = 'yvesipis3232'