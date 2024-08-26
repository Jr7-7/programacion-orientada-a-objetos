import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id_producto, nombre, cantidad = linea.strip().split(',')
                    self.productos[id_producto] = {'nombre': nombre, 'cantidad': int(cantidad)}
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo al guardar.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for id_producto, datos in self.productos.items():
                    file.write(f"{id_producto},{datos['nombre']},{datos['cantidad']}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"No se tiene permiso para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, id_producto, nombre, cantidad):
        self.productos[id_producto] = {'nombre': nombre, 'cantidad': cantidad}
        self.guardar_inventario()

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None):
        if id_producto in self.productos:
            if nombre:
                self.productos[id_producto]['nombre'] = nombre
            if cantidad is not None:
                self.productos[id_producto]['cantidad'] = cantidad
            self.guardar_inventario()
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
        else:
            print(f"Producto con ID {id_producto} no encontrado.")
