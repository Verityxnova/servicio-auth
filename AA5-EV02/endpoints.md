## Endpoints
### POST /registro 
- **Descripción:** Registra un nuevo usuario
{ "usuario": "texto", "contrasena": "texto" }
- **Body (JSON):**
  ```json
  {
    "usuario": "texto",
    "contrasena": "texto"
  }

- **Respuestas:**
  - 201: Registro exitoso
  - 400: Error en validaciones
  - 409: Usuario ya existe

### POST /login
- **Descripción:** Autentica un usuario
{ "usuario": "texto", "contrasena": "texto" }
- **Body (JSON):**
  ```json
{
  "usuario": "texto",
  "contrasena": "texto"
}

- **Respuestas:**
  - 200: Login exitoso
  - 400: Campos faltantes
  - 401: Credenciales inválidas