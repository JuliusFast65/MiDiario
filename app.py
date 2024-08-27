from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diario.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Entrada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    contenido = db.Column(db.Text, nullable=False)
    eventos = db.relationship('Evento', backref='entrada', lazy=True)

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    detalles = db.Column(db.Text)
    entrada_id = db.Column(db.Integer, db.ForeignKey('entrada.id'), nullable=False)

@app.route('/')
def index():
    entradas = Entrada.query.order_by(Entrada.fecha.desc()).all()
    return render_template('index.html', entradas=entradas)

@app.route('/nueva_entrada', methods=['GET', 'POST'])
def nueva_entrada():
    if request.method == 'POST':
        contenido = request.form['contenido']
        nueva_entrada = Entrada(contenido=contenido)
        db.session.add(nueva_entrada)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('nueva_entrada.html')

@app.route('/entrada/<int:id>')
def ver_entrada(id):
    entrada = Entrada.query.get_or_404(id)
    return render_template('ver_entrada.html', entrada=entrada)

@app.route('/agregar_evento/<int:entrada_id>', methods=['POST'])
def agregar_evento(entrada_id):
    entrada = Entrada.query.get_or_404(entrada_id)
    nombre_evento = request.form['nombre_evento']
    detalles_evento = request.form['detalles_evento']
    nuevo_evento = Evento(nombre=nombre_evento, detalles=detalles_evento, entrada=entrada)
    db.session.add(nuevo_evento)
    db.session.commit()
    return redirect(url_for('ver_entrada', id=entrada_id))

# Inicialización automática de la base de datos
with app.app_context():
    db.create_all()
    print("Base de datos inicializada.")

if __name__ == '__main__':
    app.run(debug=True)