import sqlite3
from typing import List, Tuple, Optional


class Database:
    """Clase para gestionar la base de datos SQLite"""
    
    def __init__(self, db_name: str = "usuarios.db"):
        """Inicializar conexión a la base de datos"""
        self.db_name = db_name
        self.crear_tabla()
    
    def conectar(self) -> sqlite3.Connection:
        """Crear conexión a la base de datos"""
        return sqlite3.connect(self.db_name)
    
    def crear_tabla(self):
        """Crear tabla de usuarios si no existe"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL,
                telefono TEXT,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def cerrar_conexion(self, conn: sqlite3.Connection):
        """Cerrar conexión a la base de datos"""
        if conn:
            conn.close()
    
    def crear_usuario(self, id: str, nombre: str, email: str, telefono: str = "") -> bool:
        """
        Crear un nuevo usuario en la base de datos
        
        Args:
            id: ID único del usuario
            nombre: Nombre completo
            email: Correo electrónico
            telefono: Número de teléfono (opcional)
        
        Returns:
            bool: True si se creó correctamente, False si hubo error
        """
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO usuarios (id, nombre, email, telefono)
                VALUES (?, ?, ?, ?)
            ''', (id, nombre, email, telefono))
            
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            # El ID ya existe
            return False
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False
    
    def obtener_todos_usuarios(self) -> List[Tuple]:
        """
        Obtener todos los usuarios de la base de datos
        
        Returns:
            List[Tuple]: Lista de tuplas con datos de usuarios
        """
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, nombre, email, telefono, fecha_creacion FROM usuarios ORDER BY fecha_creacion DESC')
        usuarios = cursor.fetchall()
        
        conn.close()
        return usuarios
    
    def buscar_usuario_por_id(self, id: str) -> Optional[Tuple]:
        """
        Buscar un usuario específico por ID
        
        Args:
            id: ID del usuario a buscar
        
        Returns:
            Optional[Tuple]: Tupla con datos del usuario o None si no existe
        """
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, nombre, email, telefono, fecha_creacion FROM usuarios WHERE id = ?', (id,))
        usuario = cursor.fetchone()
        
        conn.close()
        return usuario
    
    def actualizar_usuario(self, id: str, nombre: str, email: str, telefono: str = "") -> bool:
        """
        Actualizar información de un usuario existente
        
        Args:
            id: ID del usuario a actualizar
            nombre: Nuevo nombre
            email: Nuevo email
            telefono: Nuevo teléfono
        
        Returns:
            bool: True si se actualizó correctamente, False si no existe
        """
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE usuarios
                SET nombre = ?, email = ?, telefono = ?
                WHERE id = ?
            ''', (nombre, email, telefono, id))
            
            filas_afectadas = cursor.rowcount
            conn.commit()
            conn.close()
            
            return filas_afectadas > 0
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False

    def eliminar_usuario(self, id: str) -> bool:
        """
        Eliminar un usuario de la base de datos
        
        Args:
            id: ID del usuario a eliminar
        
        Returns:
            bool: True si se eliminó correctamente, False si no existe
        """
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
            
            filas_afectadas = cursor.rowcount
            conn.commit()
            conn.close()
            
            return filas_afectadas > 0
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False