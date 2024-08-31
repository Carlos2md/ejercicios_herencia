class Animal():
    def __init__(self, edad, nombre, tipo, color):
        self.edad = edad
        self.nombre = nombre
        self.tipo = tipo
        self.color = color
       
    def andar(self):
        print(f"Andar")
       
    def comer(self):
        print(f"Comer")

    def dormir(self):
        print(f"Dormir")
       

class Perro(Animal):
    def __init__(self, edad, nombre, tipo, color, patas, raza):
        super().__init__(edad, nombre, tipo, color)
        self.patas = patas
        self.raza = raza
   
    def ladrar(self):
        print(f"Este animal llamado {self.nombre} de raza {self.raza} ladra feo")
       
    def olfatear(self):
        print(f"Este animal llamado {self.nombre} de raza {self.raza} olfatea bien")
       

class Gato(Animal):
    def __init__(self, edad, nombre, tipo, color, patas, raza):
        super().__init__(edad, nombre, tipo, color)
        self.patas = patas
        self.raza = raza
   
    def maullar(self):
        print(f"Este animal llamado {self.nombre} de raza {self.raza} maulla feo")

    def trepar(self):
       print(f"Este animal llamado {self.nombre} de raza {self.raza} trepa agilmente")

class Serpiente(Animal):
    def __init__(self, edad, nombre, tipo, color, largo, diametro, raza, venenoza):
         super().__init__(edad, nombre, tipo, color)
         self.largo=largo
         self.diametro=diametro
         self.raza=raza
         self.venenoza=venenoza
        
    def morder(self):
        
        #veneno=float(input("Ingrese si la serpiente es venenosa: "))

        if self.venenoza==True:
            print(f"la Serpiente {self.nombre} de raza {self.raza} es venenoza debe tener cuidado para no ser mordido")
        else:
            print(f"la Serpiente {self.nombre} de raza {self.raza} no representa peligro alguno porque no es venenoza")

    
    def cazar(self):
        print(f"Este animal llamado {self.nombre} de raza {self.raza} caza Gallinas")


perro1 = Perro(5, "Pluto", "Terrestre", "Negro", 4, "Doberman")

perro1.ladrar()
perro1.olfatear()
print(perro1.patas)

print("---------------------------------")

gato1 = Gato(5,"Felix", "Terrestre", "Gris", 4, "Persa Extreme")
gato1.maullar()
gato1.trepar()
print(gato1.raza)

dato_veneno = input("Diga si la serpientes es venenosa (si/no): ")

if dato_veneno == "si":
    dato_veneno = True
elif dato_veneno == "no":
    dato_veneno = False

serpiente1= Serpiente(12, "Pitoniza", "Terrestre", "Negra", 1.5, 0.5, "Piton", dato_veneno)
serpiente1.morder()
