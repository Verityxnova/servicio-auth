# Servicio Web de Autenticación
**Evidencia**: GA7-220501096-AA5-EV01  
**Aprendiz**: Michelle Rojas  
**Repositorio**: [https://github.com/Verityxnova/servicio-auth](https://github.com/Verityxnova/servicio-auth) 

## 🔧 Instalación
Sigue estos pasos para configurar el proyecto:

1. clonar el repositorio: 
  ```bash
git clone https://github.com/Verityxnova/servicio-auth
cd servicio-auth
   
2. Crear entorno virtual:
python -m venv env

3. Activar entorno virtual:
# Windows:
.\env\Scripts\activate

# Linux/Mac:
source env/bin/activate

4. Instalar dependencias:
pip install -r requirements.txt

## 🚀 Ejecución
inicia el servicio web con:
python app.py
El servicio estará disponible en:
http://localhost:5000

## 🌐 Endpoints
1. Registro de Usuario
POST /registro
Content-Type: application/json

{
  "usuario": "nombre_usuario",
  "contrasena": "contraseña_segura"
}

Respuestas:
Éxito (201 Created):
{"mensaje": "Usuario registrado exitosamente"}

Error (400 Bad Request):
{"error": "La contraseña debe tener mínimo 8 caracteres"}

Error (409 Conflict):
{"error": "El usuario ya existe"}

2. Inicio de Sesión
POST /login
Content-Type: application/json

{
  "usuario": "nombre_usuario",
  "contrasena": "tu_contraseña"
}

Respuestas:

Éxito (200 OK):
{"mensaje": "Autenticación satisfactoria"}

Error (400 Bad Request):
{"error": "Usuario y contraseña requeridos"}

Error (401 Unauthorized):
{"error": "Credenciales inválidas"}

## ⚙️ Tecnologías Utilizadas
Lenguaje: Python 3.13

Framework: Flask 3.1.1

Base de datos: SQLite

Seguridad: Bcrypt (hashing de contraseñas)

Control de versiones: Git + GitHub

ORM: SQLAlchemy 2.0

## ✅ Validaciones Implementadas
Contraseña segura: Mínimo 8 caracteres

Usuario único: No se permiten duplicados

Campos obligatorios: Usuario y contraseña requeridos

Autenticación segura: Comparación con bcrypt

Manejo de errores: Respuestas HTTP claras

## 📁 Estructura del Proyecto
servicio-auth/
├── app.py                 # Código principal del servicio
├── requirements.txt       # Lista de dependencias
└── README.md              # Este archivo de documentación

## 🧪 Pruebas
Puedes probar el servicio usando:

PowerShell (Windows):
# Registro
$body = @{usuario="test"; contrasena="password123"} | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:5000/registro -Method Post -ContentType "application/json" -Body $body

# Login exitoso
Invoke-RestMethod -Uri http://localhost:5000/login -Method Post -ContentType "application/json" -Body $body

# Login fallido
$badBody = @{usuario="test"; contrasena="incorrecta"} | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:5000/login -Method Post -ContentType "application/json" -Body $badBody

## cURL (Linux/Mac):
# Registro
curl -X POST http://localhost:5000/registro \
  -H "Content-Type: application/json" \
  -d '{"usuario":"test", "contrasena":"password123"}'

# Login
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"usuario":"test", "contrasena":"password123"}'

##  📝 Notas Adicionales
La base de datos database.db se crea automáticamente en la primera ejecución

Las contraseñas se almacenan con hash bcrypt (nunca en texto plano)

El servicio está diseñado para desarrollo, no para producción