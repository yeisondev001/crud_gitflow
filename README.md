# crud_gitflow

# Sistema de Gestión de Usuarios - CRUD con SQLite

Sistema completo de gestión de usuarios desarrollado en Python con SQLite, implementando las operaciones CRUD (Create, Read, Update, Delete).

## 📋 Descripción

Aplicación de línea de comandos que permite administrar una base de datos de usuarios de forma sencilla e interactiva. Incluye una arquitectura modular con separación de responsabilidades entre la lógica de base de datos y la interfaz de usuario.

## 🚀 Características

- ✅ **Crear** nuevos usuarios con ID único
- 📖 **Leer** y visualizar todos los usuarios registrados
- 🔍 **Buscar** usuarios específicos por ID
- ✏️ **Actualizar** información de usuarios existentes
- 🗑️ **Eliminar** usuarios de la base de datos
- 💾 Persistencia de datos con SQLite
- 🎨 Interfaz de usuario amigable con menú interactivo
- ⚡ Validación automática de IDs duplicados

## 📁 Estructura del Proyecto

```
proyecto/
│
├── database.py       # Módulo de gestión de base de datos (CRUD)
├── main.py          # Programa principal con interfaz de menú
├── usuarios.db      # Base de datos SQLite (se crea automáticamente)
└── README.md        # Documentación del proyecto
```

## 🛠️ Requisitos

- Python 3.6 o superior
- sqlite3 (incluido en Python por defecto)

## 📦 Instalación

1. Clona o descarga este repositorio
2. Navega a la carpeta del proyecto:
   ```bash
   cd tu-proyecto
   ```
3. No requiere instalación de dependencias adicionales

## 💻 Uso

### Ejecutar el programa

```bash
python main.py
```

### Menú Principal

Al ejecutar el programa, verás el siguiente menú:

```
==================================================
SISTEMA DE GESTIÓN DE USUARIOS
==================================================
1. Agregar nuevo usuario
2. Ver todos los usuarios
3. Buscar usuario por ID
4. Actualizar usuario
5. Eliminar usuario
6. Salir
==================================================
```

### Ejemplos de Uso

#### 1. Agregar un usuario
```
Seleccione una opción: 1
ID del usuario: 001
Nombre completo: Juan Pérez
Email: juan@email.com
Teléfono: 809-555-1234
```

#### 2. Ver todos los usuarios
```
Seleccione una opción: 2
Total de usuarios: 3

--------------------------------------------------
ID:       001
Nombre:   Juan Pérez
Email:    juan@email.com
Teléfono: 809-555-1234
Creado:   2024-11-24 10:30:45
--------------------------------------------------
```

#### 3. Buscar usuario
```
Seleccione una opción: 3
Ingrese el ID del usuario: 001
```

#### 4. Actualizar usuario
```
Seleccione una opción: 4
ID del usuario a actualizar: 001
Nuevo nombre [Juan Pérez]: Juan Pérez Rodríguez
Nuevo email [juan@email.com]: 
Nuevo teléfono [809-555-1234]: 809-555-9999
```

#### 5. Eliminar usuario
```
Seleccione una opción: 5
ID del usuario a eliminar: 001
⚠️  Está a punto de eliminar a: Juan Pérez
¿Está seguro? (s/n): s
```

## 📊 Estructura de la Base de Datos

### Tabla: usuarios

| Campo          | Tipo      | Descripción                          |
|----------------|-----------|--------------------------------------|
| id             | TEXT      | ID único del usuario (PRIMARY KEY)   |
| nombre         | TEXT      | Nombre completo (NOT NULL)           |
| email          | TEXT      | Correo electrónico (NOT NULL)        |
| telefono       | TEXT      | Número de teléfono (opcional)        |
| fecha_creacion | TIMESTAMP | Fecha y hora de creación (automático)|

## 🔧 Componentes del Sistema

### database.py
Contiene la clase `Database` con los siguientes métodos:

- `__init__(db_name)` - Inicializa la conexión
- `conectar()` - Crea conexión a SQLite
- `crear_tabla()` - Crea la tabla de usuarios
- `crear_usuario(id, nombre, email, telefono)` - Inserta nuevo usuario
- `obtener_todos_usuarios()` - Retorna lista de todos los usuarios
- `buscar_usuario_por_id(id)` - Busca un usuario específico
- `actualizar_usuario(id, nombre, email, telefono)` - Modifica usuario
- `eliminar_usuario(id)` - Elimina usuario por ID

### main.py
Programa principal que proporciona:
- Menú interactivo
- Funciones de interfaz para cada operación CRUD
- Validaciones de entrada
- Mensajes de confirmación para operaciones críticas

## ⚠️ Consideraciones

- Los IDs de usuario deben ser únicos
- No se pueden crear dos usuarios con el mismo ID
- La eliminación de usuarios requiere confirmación
- Los campos de teléfono son opcionales
- Los datos persisten incluso después de cerrar el programa

## 🔒 Manejo de Errores

El sistema incluye manejo de errores para:
- IDs duplicados
- Usuarios no encontrados
- Errores de conexión a la base de datos
- Entradas inválidas del usuario



## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.

## 👤 Autor

Desarrollado como proyecto educativo para aprender operaciones CRUD con Python y SQLite.


---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub
