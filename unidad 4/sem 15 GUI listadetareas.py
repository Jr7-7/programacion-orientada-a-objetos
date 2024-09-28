import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar una tarea.")

def mark_completed():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        listbox.delete(index)
        listbox.insert(tk.END, f"{task} - Completada")
    except IndexError:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

def on_enter_key(event):
    add_task()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Campo de entrada para nuevas tareas
entry = tk.Entry(root, width=50)
entry.pack(pady=10)
entry.bind("<Return>", on_enter_key)

# Botones para añadir, marcar como completada y eliminar tareas
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Marcar como Completada", command=mark_completed)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=5)

# Listbox para mostrar las tareas
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()
