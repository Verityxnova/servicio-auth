# Evidencia AA5-EV02: Testing de API con Postman

## Recursos Incluidos
1. **Video demostrativo**: [https://youtu.be/jS4c5To6cgk](ver en youtube))` (muestra todas las pruebas)
1. **Capturas de prueba**:
   - Registro exitoso
   - Registro con error
   - Login exitoso
   - Login con error
2. **Documentación técnica**: 
   - `endpoints.md` (especificación de endpoints)
   - `repo.txt` (enlace al repositorio)

## Pruebas Realizadas
| Caso de Prueba                   | Endpoint  | Estado Esperado  | Resultado  |
|----------------------------------|-----------|------------------|------------|
| Registro exitoso                 | /registro |   201 Created    |     ✔️    |
| Registro con usuario existente   | /registro |   409 Conflict   |     ✔️    |
| Login exitoso                    | /login    |   200 OK         |     ✔️    |
| Login con credenciales inválidas | /login    | 401 Unauthorized |     ✔️    |

## Repositorio
El código fuente completo está disponible en:  
https://github.com/Verityxnova/servicio-auth