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
> 7. Once the app is running you have to register the admin that you configured in the .env file
> 8. uncomment
