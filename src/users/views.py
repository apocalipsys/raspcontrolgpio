from flask import Blueprint,redirect,render_template,url_for,flash,session,current_app,request
from src.users.forms import LoginForm,RegisterForm,CambiarPassForm
from src.models import Users
from flask_login import login_user,logout_user
from src.decorators import requires_admin
from src import db
from flask_login import login_required
from src import login_manager
import os
from werkzeug.security import generate_password_hash

users = Blueprint('users',__name__)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@users.route('/')
@users.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Users.query.filter_by(username=username).first()
        if form.check_user(username) and user.check_password(password):
            login_user(user)
            print('sorete')
            session['username'] = user.username
            if session['username'] == os.environ.get('ADMIN'):
                next = request.args.get('next')
                if next == None or not next[0] == '/':
                    next = url_for('core.home', user=session['username'])
                    flash('Eres el administrador', 'dark')
                return redirect(next)
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('core.home',user=session['username'])
                flash(f'Bienvenido {session["username"]}', 'info')
            return redirect(next)

        else:
            flash('Nombre de usuario o password incorrectos','warning')
            return render_template('login.html',form=form)
    return render_template('login.html',form=form)

@login_required
@requires_admin
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = Users(form.username.data,form.password.data)
        if form.check_user(user.username):
            flash('El nombre de usuario ya esta en uso','warning')
            return render_template('register.html',form=form)
        else:
            db.session.add(user)
            db.session.commit()
            flash('El usuario ha sido agregado satisfactoriamente','success')
            return redirect(url_for('.login'))
    return render_template('register.html',form=form)



@login_required
@users.route('/cambiarpass/<string:username>',methods=['GET','POST'])
def cambiarpass(username):

    form = CambiarPassForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=username).first()
        old_password =  form.old_password.data

        if form.old_password.data == form.password.data:
            flash('El password nuevo no debe ser igual que el password viejo, porfavor intente denuevo.', 'danger')
            return redirect(url_for('core.home', user=session['username']))

        if user.check_password(old_password):
            Users.query.filter_by(username= username).update({Users.password_hash:generate_password_hash(form.password.data)
                                                              },synchronize_session=False)
            db.session.commit()
            flash('Password cambiado satisfactoriamente.','success')
            return redirect(url_for('core.home',user=session['username']))
        else:

            flash('El password viejo no es correcto, porfavor vuelva a intentarlo.','info')

    return render_template('cambiar_password.html',form=form)

@login_required #YOU HAVE TO COMMENT THIS TO REGISTER AN ADMIN
@requires_admin #YOU HAVE TO COMMENT THIS TO REGISTER AN ADMIN
@users.route('/delete/<int:userid>')
def delete(userid):
    user = Users.query.filter(Users.id == userid).first()
    db.session.delete(user)
    db.session.commit()
    flash('El usuario ha sido borrado', 'success')

    return redirect(url_for('.list'))

@login_required
@requires_admin
@users.route('/users_list')
def list():
    query = Users.query.filter(Users.username != os.environ.get('ADMIN'))
    return render_template('userslist.html',users=query)



@login_required
@users.route('/mensaje')
def mensaje():
    pass



@login_required
@users.route('/logout')
def logout():
    logout_user()
    flash(f'Chau {session["username"]}', 'primary')

    session['username'] = ''

    return redirect(url_for('.login'))



