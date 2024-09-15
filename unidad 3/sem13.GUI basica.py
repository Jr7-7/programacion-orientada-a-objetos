import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entry.get()
    if dato:
        listbox.insert(tk.END, dato)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista
def limpiar_lista():
    listbox.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Datos")

# Crear y colocar los componentes
label = tk.Label(root, text="Ingrese Información:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

btn_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
