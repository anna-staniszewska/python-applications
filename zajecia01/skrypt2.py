import math
import random

# Działania matematyczne
wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie ** 12
tekst = str(potega)
wartosc_pi = math.pi
lista = [1, 2, 3, 4, 5, 6]
losowa = random.choice(lista)

# Łańcuchy znaków
tekst = f"Wartosc: {tekst}"
print(len(tekst))
print(tekst[1:4])
print(dir(tekst))
tekst = tekst.upper()
print(tekst)
print(tekst.replace("A", "p"))

# Listy
lista = list(tekst)
lista = lista[:8]
lista.append([1,2,3,4,5])
lista.remove(":")
print(lista)
lista2 = [1,2,3,"banan",100]
lista3 = [e**2 for e in lista2 if e != "banan"]
print(lista3)