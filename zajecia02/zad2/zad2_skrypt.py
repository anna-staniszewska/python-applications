import this

#6
dane = (2024, 'Python', 3.8)
rok, jezyk, wersja = dane
print(rok, jezyk, wersja)

#7
oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny 
print(pierwsza, srodek, ostatnia)

#8
info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, _, _, zawod = info
print(imie, nazwisko, zawod)

#9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok, [jezyk, wersja, opis] = dane
print(rok, jezyk, wersja, opis)

#10
a = b = [1, 2, 3]
b[0] = 'zmieniono'
print(a, b)

#11
c = a[:]
c[0] = 'nowa wartosc'
print(a, b, c)

#12
x = y = 10
y = y + 1
print(x, y)

#13
K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]
print(K, L, M, N)

#14
imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3]
for i in zip(imiona, oceny):
    print(i)

#15
liczby = [1, 2, 3, 4, 5]    
def kwadrat(x):
    return x**2
map_wynik = map(kwadrat, liczby)
for i in map_wynik:
    print(i)

#16
def zmien_wartosc(arg):
    if (isinstance(arg, list)):
        arg[0] = 'kalafior'
    elif (isinstance(arg, int)):
        arg = 65482652
a = [3,5,1]
b = 5335
print(f'Przed zmianą - a: {a}, b: {b}')
zmien_wartosc(a)
zmien_wartosc(b)
print(f'Po zmianie - a: {a}, b: {b}')

#17
def zamowienie_produktu(nazwa_produktu, *, cena, ilosc):
    pass

zamowienie_produktu("fdsdfdf", cena=123, ilosc=43)

