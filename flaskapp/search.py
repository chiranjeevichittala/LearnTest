import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('', __name__, url_prefix='/')


# @app.route('/refresh', methods=('GET', 'POST'))
def search():
    user_input = request.get('test', '')
    return render_template('search/register.html')


# @app.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('search/login.html')

