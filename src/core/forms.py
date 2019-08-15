from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired

from werkzeug.security import generate_password_hash,check_password_hash

class Ejecutar(FlaskForm):
    comando = StringField('Comando',validators=[DataRequired()])
    submit = SubmitField('Ejecutar')

class Parar(FlaskForm):
    submit = SubmitField('Parar')

class Seleccionar(FlaskForm):
    upload_file = FileField('Script',validators=[FileRequired()])
    submit = SubmitField('Subir script')