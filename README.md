# raspremote

admin: martincholoco
contrasenia: 1234
# 
Base de datos hecha en postgreSql.

## Para que funcione:

# 1 - Crear base de datos: create database raspberryremote.
# 2 - Borrar la carpeta migrations.
# 3 - En la carpeta de la app: export FLASK_APP=app.py.
# 4 - en /src/__init__.py editar la linea:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xxx:xxx@localhost/raspberryremote'
y reemplazar xxx el nombre de usuario y la contrasenia con los que creaste la base de datos en postgre
# 5 - flask db init.
# 6 - flask db migrate -m "algo"
