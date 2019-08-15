# raspremote

admin: configure the name in .env

# 
Database made in postgreSql.

## To work:
> 1. Run psql: psql postgres your_user
> 2. Create database: create database raspberryremote.
> 3. In the folder app: export FLASK_APP=app.py.
> 4. In /src/__init__.py edit the line:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xxx:xxx@localhost/raspberryremote'
and replace xxx with the username and password with which you created the database
> 5. flask db init.
> 6. flask db migrate -m "something"
> 7. Before running the app you have to register the admin that you configured in the .env file.
  For this you have to comment lines 48 and 49 in /src/users/views.py, and uncomment the line 64 in /src/templates/base.html
  to enable the Register option.
> 8. Once you registered the administrator, uncomment lines 48 and 49 in /src/users/views.py, and comment again the line 64 in /src/templates/base.html. That way only your administrator will be able to register users from now on.


## SSH:
You have to configure the shh service on the remoteserver and add the username, password and ip (of the remoteserver) on the host where you are running this code, in the file /src/core/views.py
