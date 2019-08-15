from typing import Callable
from flask import session, flash, redirect, url_for,current_app,request,jsonify
import functools
from src import app

##decorador para admin
def requires_admin(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args,**kwargs):
        if session.get('name') != current_app.config.get('ADMIN',''):
            flash('You need to be the admin to in here')
            return redirect(url_for('users_blueprint.login'))
        return f(*args,**kwargs)
    return decorated_function

##API##
api_pass = 'perromonstruo'
def protected(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == app.config.get('ADMIN', '') and auth.password == api_pass:
            return f(*args, **kwargs)
        return jsonify({"message": "Authentication failed, capo"}), 401
    return decorated_function

