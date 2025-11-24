import tkinter as tk
from tkinter import ttk, messagebox 
from tkinter import ttk
from database import Database 


class CRUDApp:
    """Aplicación CRUD con interfaz gráfica"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD de Usuarios - SQLite")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
         
         # Inicializar base de datos
        self.db = Database()
        
        # Crear interfaz
        self.crear_interfaz()
        self.cargar_usuarios() 
    
    def crear_interfaz(self):
        """Crear elementos de la interfaz"""
        
        # ========== FRAME SUPERIOR - TÍTULO ==========
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        tk.Label(
            title_frame, 
            text="📋 SISTEMA DE GESTIÓN DE USUARIOS", 
            font=('Arial', 18, 'bold'),
            bg='#2c3e50',
            fg='white'
        ).pack(pady=15)
        
        # ========== FRAME FORMULARIO ==========
        form_frame = tk.Frame(self.root, bg='#ecf0f1', padx=30, pady=20)
        form_frame.pack(fill=tk.X, padx=20, pady=20)
        
        # Fila 1: ID y Nombre
        tk.Label(
            form_frame, 
            text="ID Usuario:", 
            font=('Arial', 10, 'bold'),
            bg='#ecf0f1'
        ).grid(row=0, column=0, sticky='e', padx=10, pady=10)
        
        self.id_entry = tk.Entry(form_frame, font=('Arial', 11), width=15)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(
            form_frame, 
            text="Nombre Completo:", 
            font=('Arial', 10, 'bold'),
            bg='#ecf0f1'
        ).grid(row=0, column=2, sticky='e', padx=10, pady=10)
        
        self.nombre_entry = tk.Entry(form_frame, font=('Arial', 11), width=25)
        self.nombre_entry.grid(row=0, column=3, padx=10, pady=10)
        
        # Fila 2: Email y Teléfono
        tk.Label(
            form_frame, 
            text="Email:", 
            font=('Arial', 10, 'bold'),
            bg='#ecf0f1'
        ).grid(row=1, column=0, sticky='e', padx=10, pady=10)
        
        self.email_entry = tk.Entry(form_frame, font=('Arial', 11), width=30)
        self.email_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky='w')
        
        tk.Label(
            form_frame, 
            text="Teléfono:", 
            font=('Arial', 10, 'bold'),
            bg='#ecf0f1'
        ).grid(row=1, column=2, sticky='e', padx=10, pady=10)
        
        self.telefono_entry = tk.Entry(form_frame, font=('Arial', 11), width=15)
        self.telefono_entry.grid(row=1, column=3, padx=10, pady=10)
        
        # ========== FRAME BOTONES ==========
        btn_frame = tk.Frame(self.root, bg='white', pady=15)
        btn_frame.pack(fill=tk.X, padx=20)
        
        button_config = {
            'font': ('Arial', 10, 'bold'),
            'width': 12,
            'height': 2,
            'cursor': 'hand2'
        }
        
        tk.Button(
            btn_frame, 
            text="➕ CREAR",
            bg='#27ae60',
            fg='white',
            command=self.crear_usuario,
            **button_config
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            btn_frame, 
            text="🔍 BUSCAR",
            bg='#3498db',
            fg='white',
            **button_config
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            btn_frame, 
            text="✏️ ACTUALIZAR",
            bg='#f39c12',
            fg='white',
            **button_config
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            btn_frame, 
            text="🗑️ ELIMINAR",
            bg='#e74c3c',
            fg='white',
            **button_config
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            btn_frame, 
            text="🔄 LIMPIAR",
            bg='#95a5a6',
            fg='white',
            **button_config,
            command=self.limpiar_campos
        ).pack(side=tk.LEFT, padx=10)
        
        # ========== FRAME TABLA ==========
        table_frame = tk.Frame(self.root, bg='white')
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        # Scrollbar
        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Tabla
        self.tabla = ttk.Treeview(
            table_frame,
            columns=("ID", "Nombre", "Email", "Teléfono", "Fecha"),
            show='headings',
            yscrollcommand=scrollbar.set,
            height=12
        )
        scrollbar.config(command=self.tabla.yview)
        
        # Configurar columnas
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre Completo")
        self.tabla.heading("Email", text="Email")
        self.tabla.heading("Teléfono", text="Teléfono")
        self.tabla.heading("Fecha", text="Fecha Creación")
        
        self.tabla.column("ID", width=80, anchor='center')
        self.tabla.column("Nombre", width=200)
        self.tabla.column("Email", width=250)
        self.tabla.column("Teléfono", width=120, anchor='center')
        self.tabla.column("Fecha", width=150, anchor='center')
        
        self.tabla.pack(fill=tk.BOTH, expand=True)
        
        # Estilo de la tabla
        style = ttk.Style()
        style.configure("Treeview", 
                       font=('Arial', 10),
                       rowheight=30)
        style.configure("Treeview.Heading", 
                       font=('Arial', 10, 'bold'),
                       background='#34495e',
                       foreground='white')
    
    def limpiar_campos(self):
        """Limpiar todos los campos del formulario"""
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.id_entry.focus()

def crear_usuario(self):
        """Crear un nuevo usuario en la base de datos"""
        # Obtener valores
        usuario_id = self.id_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        email = self.email_entry.get().strip()
        telefono = self.telefono_entry.get().strip()
        
        # Validaciones
        if not usuario_id:
            messagebox.showwarning("Campo vacío", "El ID es obligatorio")
            self.id_entry.focus()
            return
        
        if not nombre:
            messagebox.showwarning("Campo vacío", "El nombre es obligatorio")
            self.nombre_entry.focus()
            return
        
        if not email:
            messagebox.showwarning("Campo vacío", "El email es obligatorio")
            self.email_entry.focus()
            return
        
        # Validar formato de email básico
        if '@' not in email or '.' not in email:
            messagebox.showwarning("Email inválido", "Por favor ingrese un email válido")
            self.email_entry.focus()
            return
        
        # Intentar crear usuario
        if self.db.crear_usuario(usuario_id, nombre, email, telefono):
            messagebox.showinfo("Éxito", f"Usuario '{nombre}' creado correctamente")
            self.limpiar_campos()
            self.cargar_usuarios()
        else:
            messagebox.showerror("Error", f"El ID '{usuario_id}' ya existe en la base de datos")
            self.id_entry.focus()
    
def cargar_usuarios(self):
        """Cargar todos los usuarios en la tabla"""
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        # Obtener usuarios de la BD
        usuarios = self.db.obtener_todos_usuarios()
        
        # Insertar en la tabla
        for usuario in usuarios:
            # usuario = (id, nombre, email, telefono, fecha_creacion)
            fecha = usuario[4][:19] if usuario[4] else ""  # Formato fecha
            self.tabla.insert('', tk.END, values=(
                usuario[0],  # ID
                usuario[1],  # Nombre
                usuario[2],  # Email
                usuario[3] if usuario[3] else "N/A",  # Teléfono
                fecha  # Fecha
            ))
def crear_usuario(self):
        """Crear un nuevo usuario en la base de datos"""
        # Obtener valores
        usuario_id = self.id_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        email = self.email_entry.get().strip()
        telefono = self.telefono_entry.get().strip()
        
        # Validaciones
        if not usuario_id:
            messagebox.showwarning("Campo vacío", "El ID es obligatorio")
            self.id_entry.focus()
            return
        
        if not nombre:
            messagebox.showwarning("Campo vacío", "El nombre es obligatorio")
            self.nombre_entry.focus()
            return
        
        if not email:
            messagebox.showwarning("Campo vacío", "El email es obligatorio")
            self.email_entry.focus()
            return
        
        # Validar formato de email básico
        if '@' not in email or '.' not in email:
            messagebox.showwarning("Email inválido", "Por favor ingrese un email válido")
            self.email_entry.focus()
            return
        
        # Intentar crear usuario
        if self.db.crear_usuario(usuario_id, nombre, email, telefono):
            messagebox.showinfo("Éxito", f"Usuario '{nombre}' creado correctamente")
            self.limpiar_campos()
            self.cargar_usuarios()
        else:
            messagebox.showerror("Error", f"El ID '{usuario_id}' ya existe en la base de datos")
            self.id_entry.focus()
    
def cargar_usuarios(self):
        """Cargar todos los usuarios en la tabla"""
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        # Obtener usuarios de la BD
        usuarios = self.db.obtener_todos_usuarios()
        
        # Insertar en la tabla
        for usuario in usuarios:
            # usuario = (id, nombre, email, telefono, fecha_creacion)
            fecha = usuario[4][:19] if usuario[4] else ""  # Formato fecha
            self.tabla.insert('', tk.END, values=(
                usuario[0],  # ID
                usuario[1],  # Nombre
                usuario[2],  # Email
                usuario[3] if usuario[3] else "N/A",  # Teléfono
                fecha  # Fecha
            ))
if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()