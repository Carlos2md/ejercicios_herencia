class Vehiculo():
    def __init__(self, marca, tipo, modelo, vel_max, matricula):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo
        self.vel_max = vel_max
        self.matricula = matricula

    def acelerar(self):
        print(f"Velocidad maxima alcanzada {self.vel_max} km/h")
       
    def frenar(self):
        print(f"velocidad actual: 0")
       

class Carro(Vehiculo):
    def __init__(self, marca, tipo, modelo, vel_max, matricula, placa, pasajeros):
        super().__init__(marca, tipo, modelo, vel_max, matricula)
        self.__placa = placa
        self.pasajeros = pasajeros
        self.ruedas = 4
   
    def solicitar_informacion(self):
        print(f"Este carro cuenta con numero de matricula {self._Vehiculo__nro_matricula} y fue fabricado en {self.modelo} y su placa es {self.__placa}")
       
class Moto(Vehiculo):
    def __init__(self, marca, tipo, modelo, vel_max, matricula, placa):
        super().__init__(marca, tipo, modelo, vel_max, matricula)
        self.__placa = placa
        self.pasajeros = 2
        self.ruedas = 2
   
    def solicitar_informacion(self):
        print(f"Esta moto tiene placa {self.__placa} y es de marca {self.marca}")

carro1 = Carro("chevrolet", "terrestre", 2010, 140, "car12345", "AVK001", 4)

carro1.solicitar_informacion()
carro1.acelerar()
print(carro1.pasajeros)

print("---------------------------------")

moto1 = Moto("Yamaha", "terrestre", 2020, 180, "mot59986", "CB586")
moto1.solicitar_informacion()
moto1.acelerar()
print(moto1.marca)