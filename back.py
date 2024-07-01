from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Abrir el archivo CSV y verificar las credenciales
    with open('BasedeDatos.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Comparación de cadenas eliminando espacios en blanco adicionales
            if row['ID_ALUM'].strip() == username and row['CONTRASEÑA'].strip() == password:
                # Autenticación exitosa, redirigir a una página de éxito o dashboard
                return redirect(url_for('success'))

    # Si las credenciales son incorrectas, redirigir a la página de login nuevamente con un mensaje de error
    return render_template('index.html', message='Credenciales incorrectas. Inténtalo nuevamente.')

@app.route('/pagina_p')
def success():
    return render_template('pagina_p.html')  # Renderiza la plantilla pagina_p.html

@app.route('/h_dispo')
def h_dispo():
    return render_template('h_dispo.html')  # Renderiza la plantilla h_dispo.html

@app.route('/h_p')
def h_p():
    return render_template('h_p.html')  # Renderiza la plantilla h_p.html

if __name__ == '__main__':
    app.run(debug=True)
    
