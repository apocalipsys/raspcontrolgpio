from flask import Blueprint,render_template,url_for,redirect
from flask_login import login_required
from werkzeug.utils import secure_filename
from src import app
from src.core.forms import Ejecutar,Seleccionar
import paramiko
import time
import os

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
HOST = '192.168.x.xxx'
USERNAME = 'xxx'
PASSWORD = 'xxx'


core = Blueprint('core',__name__)


@login_required
@core.route('/home/<string:user>')
def home(user):
    return render_template('home.html',user=user)

@login_required
@core.route('/ejecutar/comando', methods=['POST','GET'])
def comando():

    form = Ejecutar()

    if form.validate_on_submit():
        client.connect(HOST,username=USERNAME,password=PASSWORD)
        comando = form.comando.data

        stdin,stdout,stderr = client.exec_command(comando)

        print('ejecutando')
        print(stdin)
        print(stderr)

        #for line in stdout:
        #    print (line.strip('\n'))

        return render_template('stdout.html',form=form, stdin=stdin,stdout=stdout,stderr=stderr)

    return render_template('comando.html',form=form)

@login_required
@core.route('/terminal', methods=['POST','GET'])
def terminal():
    client.connect(HOST, username=USERNAME, password=PASSWORD)
    transport = client.get_transport()
    ssh_session = transport.open_session()
    ssh_session.get_pty()
    shell = ssh_session.invoke_shell()
    print(shell)

    return render_template('terminal.html',shell=shell)




@login_required
@core.route('/subir_archivo', methods=['POST','GET'])
def upload():
    form = Seleccionar()
    if form.validate_on_submit():
        print('copiando')
        basedir = os.path.abspath(os.path.dirname(__file__))
        file = form.upload_file.data

        filename = secure_filename(file.filename)

        file.save(basedir+'/uploads/'+ filename)
        client.connect(HOST, username=USERNAME, password=PASSWORD)
        ftp_client = client.open_sftp()
        ftp_client.put(basedir+'/uploads/'+filename, '/xx/xx/xxx/'+filename)
        ftp_client.close()

    return render_template('subir_archivo.html',form=form)



@login_required
@core.route('/parar',methods=['POST','GET'])
def parar():
    client.close()

    return render_template('home.html')
