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
import math

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
    print(area_circulo(23))

