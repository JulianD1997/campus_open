"""En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada 
por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce."""

from functools import reduce

lista_numeros = [i for i in range(100)]
impares = filter(lambda x: x%2 == 1,lista_numeros)
reduce_result = reduce(lambda a,b: a + b, impares)
print(reduce_result)