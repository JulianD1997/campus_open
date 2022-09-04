num = int(input("Ingrese un numero: "))
if num == 0:
    print("El numero es igual a cero")
elif num > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")
num = 0
while num < 3 :
    print(num,"while")
    num += 1
for i in range(4):
    print(i,"for")
