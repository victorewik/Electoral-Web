from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

# Ruta del archivo donde se guardan las preguntas
LOG_FILE = "/app/data/preguntas_campana.txt"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sugerencia', methods=['POST'])
def sugerencia():
    email = request.form.get('email').lower().strip()
    pregunta = request.form.get('pregunta').strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardar en el archivo de texto
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"FECHA: {timestamp}\n")
        f.write(f"EMAIL: {email}\n")
        f.write(f"PREGUNTA: {pregunta}\n")
        f.write("-" * 40 + "\n")

    return redirect(url_for('index', enviado='true'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
