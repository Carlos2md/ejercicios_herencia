class Usuario():
    def __init__(self, nombre, edad, direccion, numero_Cuenta, saldo_Actual):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.numero_Cuenta = numero_Cuenta
        self.saldo_Actual = saldo_Actual

    def depositan(self):
        print(f"Velocidad maxima alcanzada {self.vel_max} km/h")
       
    def debitan(self):
        print(f"velocidad actual: 0")
    
    def cumpleanos(Self):
        edad=+edad
       

class Cliente(Usuario):
    def __init__(self, nombre, edad, direccion, numero_Cuenta, saldo_Actual, id_Cliente, profesion, prestamoEnCurso):
        super().__init__(nombre, edad, direccion, numero_Cuenta, saldo_Actual)
        self.id_Cliente = id_Cliente
        self.profesion = profesion
        self.prestamoEnCurso = prestamoEnCurso
   
    def solicitar_informacion(self):
        print(f"Este carro cuenta con numero de matricula {self._Vehiculo__nro_matricula} y fue fabricado en {self.modelo} y su placa es {self.__placa}")
       
class Empleado(Usuario):
    def __init__(self, nombre, edad, direccion, numero_Cuenta, saldo_Actual, id_Empleado, cargo, sueldo, adelandoDeSueldo):
        super().__init__(nombre, edad, direccion, numero_Cuenta, saldo_Actual)
        self.id_Empleado = id_Empleado
        self.cargo = cargo
        self.sueldo = sueldo
        self.adelandoDeSueldo = adelandoDeSueldo
   
    def solicitar_informacion(self):
        print(f"Esta moto tiene placa {self.__placa} y es de marca {self.marca}")

cliente1 = Usuario("chevrolet", "terrestre", 2010, 140, "car12345", "AVK001", 4)

cliente1.solicitar_informacion()
cliente1.acelerar()
print(cliente1.pasajeros)

print("---------------------------------")

empleado1 = Empleado("Yamaha", "terrestre", 2020, 180, "mot59986", "CB586")
empleado1.solicitar_informacion()
empleado1.acelerar()
print(empleado1.marca)