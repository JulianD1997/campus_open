print("""Hola, soy Julian Casallas
estoy iniciando el curso
espero aprender mucho...""")
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
print(f"tu indice de imc es {round(imc(peso,altura),2)}")
