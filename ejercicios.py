"""print(""""""Hola, soy Julian Casallas
estoy iniciando el curso
espero aprender mucho..."""""")
var = "Hola Mundo"
print(var)
print(type(var))
var = 30
print(var)
print(type(var))
nombre = "Julian"
apellidos = "Casallas"
edad = 25
email = "julian.casallasb@gmail.com"
telefono =  1129735694
casado = False
hijos = False
amigos = [1,2,3,4,5,6,7]
peliculas = {"pelicula 1" : "Son como niños",
            "pelicula 2" : "El señor de los anillos",
            "pelucula 3" : "Elysium"}
print(f"{nombre} {apellidos} {edad} años {email} {telefono} casado : {casado}\
    \nhijos : {hijos} {amigos} peliculas {peliculas}")

def imc(peso,altura):
    imc = peso/(altura**2)
    return imc
peso = int(input("Ingrese su peso en kilogramos : "))
altura = float(input("Ingrese su altura en metros : "))
print(f"tu indice de imc es {round(imc(peso,altura),2)}")"""

"""Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no."""

"""edad = int(input("Ingrese su edad : "))
if edad <18 :
    print("Usted no es mayor de edad")
else :
    print("Usted es mayor de edad")
"""
"""Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]"""
"""
num_1 = int(input("Ingrese el numero de inicio : "))
num_2 = int(input("Ingrese el numero de final : "))

impares = list(i for i in range(num_1,num_2+1) if i%2 == 1)
print(impares)"""
"""Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso."""
"""
for i in range(100,0,-1):
    print(i)"""

"""Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo."""
"""import math

def area_triangulo(base,altura):
    return f"Area del triangulo = {(base*altura)/2}"


def area_circulo(radio):
    return f"Area del circulo = {round((math.pi*math.sqrt(radio)),2)}"

if __name__ == "__main__":
    print(area_triangulo(4,8))
    print(area_triangulo(7,18))
    print(area_triangulo(2,6))
    print(area_triangulo(3,10))
    print(area_circulo(5))
    print(area_circulo(10))
    print(area_circulo(2))
    print(area_circulo(23))"""

"""Escribe una función que pueda decirte si un número (número entero) es primo o no."""

"""def numero_primo(numero):

    for i in range(2,numero):
        if numero % i == 0:
            return f"{numero} No es primo"
    return f"{numero} Es primo"

if __name__ == "__main__":
    print(numero_primo(3))
    print(numero_primo(4))
    print(numero_primo(13))
    print(numero_primo(20))
    print(numero_primo(41))
    print(numero_primo(45))
    print(numero_primo(67))
    print(numero_primo(72))
    print(numero_primo(89))"""
"""Escribe una función que pueda decirte si un año (número entero) es bisiesto o no."""

"""def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"El {year} es año bisiesto"
            else :
                return f"El {year} no es año bisiesto"
        else:
            return f"El {year} es año bisiesto"
    else :
        return f"El {year} no es año bisiesto"
if __name__ == "__main__":
    print(leap_year(1992))
    print(leap_year(2000))
    print(leap_year(1900))
    print(leap_year(2012))
    print(leap_year(2024))
    print(leap_year(2020))
    print(leap_year(2100))
    print(leap_year(1988))
    print(leap_year(1997))"""
"""
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

Color

Ruedas

Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

Velocidad

Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
"""
"""class Vehículo:
    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
class Coche(Vehículo):
    def __init__(self,color,ruedas,puertas,velocidad,cilindrada):
        super().__init__(color,ruedas,puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        #return f#\"""
        #Color : {self.color}
        #ruedas : {self.ruedas}
        #puertas : {self.puertas}
        #velocidad : {self.velocidad}
        #cilindrada : {self.cilindrada}\"""

if __name__ == "__main__":
    mi_coche = Coche("Negro",4,4,120,6.2)
    print(mi_coche)
    mi_coche_1 = Coche("Rojo",4,2,160,8.5)
    print(mi_coche_1)
    mi_coche_2 = Coche("Gris",4,2,180,3.8)
    print(mi_coche_2)
    mi_coche_3 = Coche("Blanco",4,4,200,9.9)
    print(mi_coche_3)"""

"""En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como 
atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y 
mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""
class Alumno:
    def __init__(self, nombre,nota):
        self.__nombre = nombre
        self.__nota = nota
    def __esta_aprobado(self):
        if self.__nota >= 7 :
            return "Aprobo"
        else:
            return "Desaprobo"
    def __str__(self):
        return f"{self.__nombre} con nota {self.__nota}\n{self.__esta_aprobado()}"
if __name__ == "__main__":
    alumno_1 = Alumno("Juan",6.8)
    print(alumno_1)
    alumno_2 = Alumno("Julian",9)
    print(alumno_2)
    alumno_3 = Alumno("Sara",7.0)
    print(alumno_3)
    alumno_3 = Alumno("Luisa",5.6)
    print(alumno_3)
    alumno_4 = Alumno("Lorena",10)
    print(alumno_4)
