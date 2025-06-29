# Servicio Web de Autenticación 
**Evidencia**: GA7-220501096-AA5-EV01  
**Aprendiz**: Michelle Rojas  
**Repositorio**: https://github.com/Verityxnova/servicio-auth

## 📂 Evidencias
- [AA5-EV01: Desarrollo del Servicio Web](./AA5-EV01)
- [AA5-EV02: Testing con Postman](./AA5-EV02)

## 🎬 Video Demostrativo EV02
[Ver en YouTube](https://youtu.be/jS4c5To6cgk)

---

## 🔧 Instalación

 1. Clonar el repositorio:
git clone https://github.com/Verityxnova/servicio-auth cd servicio-auth
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt

## 🚀 Ejecución

1. Clonar el repositorio:
- Inicia el servicio web con:

python app.py
El servicio estará disponible en:
http://localhost:5000


## 🌐 Endpoints 
1. Registro de Usuario
POST /registro
Body: json

{
  "usuario": "nombre_usuario",
  "contrasena": "contraseña_segura"
}

Respuestas:
201 Created: {"mensaje": "Usuario registrado exitosamente"}
400 Bad Request: {"error": "La contraseña debe tener mínimo 8 caracteres"}
409 Conflict: {"error": "El usuario ya existe"}

1. Inicio de Sesión
POST /login
Body:json

{
  "usuario": "nombre_usuario",
  "contrasena": "tu_contraseña"
}

Respuestas:
200 OK: {"mensaje": "Autenticación satisfactoria"}
400 Bad Request: {"error": "Usuario y contraseña requeridos"}
401 Unauthorized: {"error": "Credenciales inválidas"}

## ⚙️ Tecnologías Utilizadas
Python 3.13
Flask 3.1.1
SQLite
Bcrypt
SQLAlchemy 2.0
Git + GitHub

## ✅ Validaciones Implementadas
Contraseña segura (mínimo 8 caracteres)
Usuario único (no duplicados)
Campos obligatorios
Hash con Bcrypt
Manejo de errores HTTP

## 🧪 Pruebas con PowerShell

# Registro
$body = @{usuario="test"; contrasena="password123"} | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:5000/registro -Method Post -ContentType "application/json" -Body $body

# Login exitoso
Invoke-RestMethod -Uri http://localhost:5000/login -Method Post -ContentType "application/json" -Body $body

# Login fallido
$badBody = @{usuario="test"; contrasena="incorrecta"} | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:5000/login -Method Post -ContentType "application/json" -Body $badBody

## 🧪 Pruebas con cURL

# Registro
curl -X POST http://localhost:5000/registro \
  -H "Content-Type: application/json" \
  -d '{"usuario":"test", "contrasena":"password123"}'

# Login
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"usuario":"test", "contrasena":"password123"}'


## 📝 Notas Adicionales
La base de datos database.db se crea automáticamente.
Las contraseñas se almacenan con hash bcrypt.
Este servicio está diseñado para uso en entornos de desarrollo.


