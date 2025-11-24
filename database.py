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