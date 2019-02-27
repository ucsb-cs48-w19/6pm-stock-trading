import pytest
import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, LoginManager, login_required
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, FloatField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from werkzeug.urls import url_parse
#Added imports for postgres hsoting
from flask_sqlalchemy import SQLAlchemy
from app import about
def test_stocktemp_about():
    assert about() == render_template("about.html")
