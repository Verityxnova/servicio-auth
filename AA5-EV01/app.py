from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import bcrypt

# Inicialización de la aplicación Flask
app = Flask(__name__)
# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de datos para usuarios
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID único
    usuario = db.Column(db.String(80), unique=True, nullable=False)  # Nombre de usuario único
    contrasena = db.Column(db.String(120), nullable=False)  # Contraseña hasheada

# Endpoint para registro de usuarios
@app.route('/registro', methods=['POST'])
def registro():
    """Registra un nuevo usuario en el sistema"""
    datos = request.get_json()  # Obtener datos JSON del request
    
    # Extraer usuario y contraseña
    usuario = datos.get('usuario')
    contrasena = datos.get('contrasena')

    # Validación: campos obligatorios
    if not usuario or not contrasena:
        return jsonify({"error": "Usuario y contraseña requeridos"}), 400
    
    # Validación: longitud mínima de contraseña
    if len(contrasena) < 8:
        return jsonify({"error": "La contraseña debe tener mínimo 8 caracteres"}), 400

    # Validación: usuario único
    if Usuario.query.filter_by(usuario=usuario).first():
        return jsonify({"error": "El usuario ya existe"}), 409

    # Hash de contraseña con bcrypt
    hashed = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Crear y guardar nuevo usuario
    nuevo_usuario = Usuario(usuario=usuario, contrasena=hashed)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

# Endpoint para inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    """Autentica un usuario existente"""
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contrasena')

    # Validación: campos obligatorios
    if not usuario or not contrasena:
        return jsonify({"error": "Usuario y contraseña requeridos"}), 400

    # Buscar usuario en base de datos
    user = Usuario.query.filter_by(usuario=usuario).first()
    
    # Verificar credenciales con bcrypt
    if user and bcrypt.checkpw(contrasena.encode('utf-8'), user.contrasena.encode('utf-8')):
        return jsonify({"mensaje": "Autenticación satisfactoria"}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

# Punto de entrada principal
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas si no existen
    app.run(debug=True, port=5000)  # Ejecutar servidor en modo desarrollo