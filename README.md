# ⏳ TimeCapsule API – Mensajes al futuro

Una API donde los usuarios pueden crear **cápsulas del tiempo digitales**: mensajes, fotos o audios que solo podrán abrirse en una fecha futura especificada.

---

## 🎯 Idea clave

- Cualquiera puede crear una cápsula con contenido.
- Solo el autor decide **cuándo se puede abrir**.
- Otros usuarios pueden **suscribirse** para recibir una notificación cuando se desbloquee.
- El contenido se **encripta** y permanece inaccesible hasta la fecha señalada.

---

## 🗂 Entidades principales

- **Users** → Registro y autenticación.  
- **Capsules** → Contienen título, descripción, fecha de apertura y archivos opcionales.  
- **Subscriptions** → Usuarios que se anotan para recibir la cápsula.  
- **Open Logs** → Historial de aperturas para estadísticas.  

---

## 🔌 Endpoints principales

### 🔑 Autenticación
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/auth/register/` | Registro de usuario |
| `POST` | `/api/auth/login/` | Login y obtención de token |

---

### 📦 Cápsulas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/capsules/` | Lista de cápsulas públicas disponibles |
| `POST` | `/api/capsules/` | Crear cápsula |
| `GET` | `/api/capsules/{id}/` | Detalles (sin contenido si aún no está disponible) |
| `DELETE` | `/api/capsules/{id}/` | Eliminar (solo autor) |

---

### 📬 Apertura
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/capsules/{id}/open/` | Acceder al contenido (solo si está desbloqueada) |
| `POST` | `/api/capsules/{id}/subscribe/` | Suscribirse a una cápsula |
| `GET` | `/api/capsules/{id}/subscribers/` | Lista de suscriptores |

---

### 📊 Estadísticas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/stats/popular/` | Cápsulas con más suscriptores |
| `GET` | `/api/stats/opened-today/` | Cápsulas abiertas hoy |

---

## ⚙️ Instalación y uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/timecapsule-api.git
   cd timecapsule-api
   ```

2. Crea un entorno virtual e instala dependencias:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # en Linux/Mac
   .venv\Scripts\activate      # en Windows

   pip install -r requirements.txt
   ```

3. Ejecuta migraciones:
   ```bash
   python manage.py migrate
   ```

4. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

5. Prueba la API en [http://localhost:8000](http://localhost:8000)

---

## 📌 Ejemplo rápido con HTTPie

```bash
# Registro
http POST http://localhost:8000/api/auth/register/ username="alice" password="1234"

# Login
http POST http://localhost:8000/api/auth/login/ username="alice" password="1234"

# Crear cápsula
http POST http://localhost:8000/api/capsules/   "Authorization: Token <tu_token>"   title="Mi mensaje al futuro"   message="Nos vemos en 2030"   release_date="2030-01-01T00:00:00Z"
```

---

## 🚀 Tecnologías

- Django + Django REST Framework
- SQLite (por defecto, fácilmente migrable a PostgreSQL/MySQL)
- Autenticación por Token

---

## 📜 Licencia
MIT – libre para usar y modificar.
