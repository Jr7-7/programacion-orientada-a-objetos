import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas Pendientes")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5)
        self.task_entry.bind("<Return>", self.add_task)

        self.add_button = tk.Button(self.frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.root.bind("<Escape>", lambda event: root.destroy())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<d>", lambda event: self.delete_task())

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = f"{task} - Completada"
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, f"{task} - Completada")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
