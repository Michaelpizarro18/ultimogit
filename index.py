from flask import Flask, render_template
from flask_frozen import Freezer

# Crea la aplicación Flask
app = Flask(__name__, template_folder='App')

# Crea un objeto Freezer
freezer = Freezer(app)

# Definición de rutas
@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/cuerpo')
def cuerpo():
    return render_template('cuerpo.html')

# Ejecuta la aplicación en modo de desarrollo
if __name__ == '__main__':
    app.run(debug=True)