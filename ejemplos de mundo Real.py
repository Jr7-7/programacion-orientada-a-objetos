class Reserva:
    def __init__(self, nombre_cliente, fecha, cantidad_personas):
        self.nombre_cliente = nombre_cliente
        self.fecha = fecha
        self.cantidad_personas = cantidad_personas
        self.confirmada = False

    def confirmar_reserva(self):
        self.confirmada = True
        print(f"Reserva para {self.cantidad_personas} personas el {self.fecha} confirmada.")

    def cancelar_reserva(self):
        self.confirmada = False
        print(f"Reserva para {self.cantidad_personas} personas el {self.fecha} cancelada.")

# Ejemplo de uso
if __name__ == "__main__":
    reserva1 = Reserva("Juan Pérez", "2024-06-20", 4)
    reserva1.confirmar_reserva()

    reserva2 = Reserva("María Gómez", "2024-06-22", 2)
    reserva2.cancelar_reserva()