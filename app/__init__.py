from flask import Flask, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy

# instancia do Flask
app = Flask(__name__)
# caminho do DB
app.config ['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dbcliente"
# instancia do sqlalchemy
db = SQLAlchemy(app)

from app.controller import default