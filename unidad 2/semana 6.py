class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("el perro hace Guau!")

class Gato(Animal):
    def hablar(self):
        print("el gato hace Miau!")

perro = Perro()
gato = Gato()

perro.hablar()  # Imprime "el perro hace Guau!"
gato.hablar()   # Imprime "el gato hace Miau!"
