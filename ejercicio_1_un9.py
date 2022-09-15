"""Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben 
almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola 
la lista de países ordenados alfabéticamente y separados por comas."""
from calendar import c
from multiprocessing import cpu_count
import pprint
def countries_list(countries):
    countries = countries.replace(' ', '')
    countries = list(sorted(set(countries.split(","))))
    pprint.pprint(countries)

if __name__ == "__main__":
    #countries=input("ingrese los países separados por comas\n")
    countries = "Portugal, Suiza, Alemania, Francia, Belgica, Chile, Colombia, Suiza"
    countries_list(countries)