from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL



app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'vinedo'
#app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)

@app.route('/')
def Index():
    
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['pass']
        #coneccion db
        con = mysql.connection.cursor()
        con.execute('SELECT * FROM usuario () ')
    
        return redirect(url_for('Index'))



@app.route('/register')
def register():
    return render_template('registro.html')


@app.route('/formregister', methods =['POST'])
def formregister():
    if request.method == 'POST':
        nombre = request.form['nombreR']
        apellido = request.form['apellidoR']
        email = request.form['emailR']
        telefono = request.form['telefonoR']
        ciudad = request.form['ciudadR']
        departamento = request.form['departamentoR']
        contrasena = request.form['passR']
        contrasenaC = request.form['passconfR']

        if(contrasena == contrasenaC):
            contrasenaa = contrasena

            #coneccion db
            con = mysql.connection.cursor()
            con.execute('INSERT INTO usuario (nombreUsuario, apellidoUsuario, email, contrasena, telefono, idciudad, iddepartamento) VALUES ( %s, %s, %s, %s, %s, %s, %s)',
            (nombre, apellido, email, contrasenaa, telefono, ciudad, departamento ))
            mysql.connection.commit()
        else:
            return redirect(url_for('register'))
        
        return redirect(url_for('register'))

        



if __name__=='__main__':
    app.run(port=3000, debug=True)
