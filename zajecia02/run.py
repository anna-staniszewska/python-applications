from src.zad15 import *
from src.zad16 import *
from src.zad17 import *
from src.zad18 import *
from src.zad19 import *
from src.liczniki_stanu import *
from src.zad23 import *

def run():
    #6
    print("Zad. 6")
    dane = (2024, 'Python', 3.8)
    rok, jezyk, wersja = dane
    print(rok, jezyk, wersja)

    #7
    print("\nZad. 7")
    oceny = [4, 3, 5, 2, 5, 4]
    pierwsza, *srodek, ostatnia = oceny 
    print(pierwsza, srodek, ostatnia)

    #8
    print("\nZad. 8")
    info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
    imie, nazwisko, _, _, zawod = info
    print(imie, nazwisko, zawod)

    #9
    print("\nZad. 9")
    dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
    rok, [jezyk, wersja, opis] = dane
    print(rok, jezyk, wersja, opis)

    #10
    print("\nZad. 10")
    a = b = [1, 2, 3]
    b[0] = 'zmieniono'
    print(a, b)

    #11
    print("\nZad. 11")
    c = a[:]
    c[0] = 'nowa wartosc'
    print(a, b, c)

    #12
    print("\nZad. 12")
    x = y = 10
    y = y + 1
    print(x, y)

    #13
    print("\nZad. 13")
    K = [1, 2]
    L = K
    K = K + [3, 4]
    M = [1, 2]
    N = M
    M += [3, 4]
    print(K, L, M, N)

    #14
    print("\nZad. 14")
    imiona = ['Anna', 'Jan', 'Ewa']
    oceny = [5, 4, 3]
    for i in zip(imiona, oceny):
        print(i)

    #15
    print("\nZad. 15")
    liczby = [1, 2, 3, 4, 5]    
    map_wynik = map(kwadrat, liczby)
    for i in map_wynik:
        print(i)

    #16
    print("\nZad. 16")
    a = [3,5,1]
    b = 5335
    print(f'Przed zmianą - a: {a}, b: {b}')
    zmien_wartosc(a)
    zmien_wartosc(b)
    print(f'Po zmianie - a: {a}, b: {b}')

    #17
    print("\nZad. 17")
    #a
    order_list = [zamowienie_produktu("Zszywacz", cena=11, ilosc=25),
                zamowienie_produktu("Drukarka", cena=254),
                zamowienie_produktu("Kreda", cena=25, ilosc=50)]
    #b,d
    sum = 0
    for order in order_list:
        print(order[0])
        sum += order[1]
    print(f"Całkowity koszt z wszystkich zamówień: {sum}.")

    #18
    print("\nZad. 18")
    print(stworz_raport(101, 102, p_101_nazwa="Kubek termiczny", p_101_cena="45.99 zł", p_102_nazwa="Długopis", p_102_cena="4.99 zł"))

    #19
    print("Zad. 19")
    potega_2 = stworz_funkcje_potegujaca(2)
    print(potega_2(4))

    print("\nZad. 20")
    #20a
    licznik_a = licznikA()
    print("Zmienna nonlocal w zagnieżdżonej funkcji:")
    print(licznik_a()) 
    print(licznik_a())  

    print()

    #20b
    print("Zmienna global:")
    print(licznikB())
    print(licznikB())

    print()

    #20c
    licznik_c = LicznikC()
    print("Klasa z atrybutem instancji:")
    print(licznik_c())  
    print(licznik_c())  

    print()

    #20d
    print("Atrybut funkcji:")
    print(licznikD()) 
    print(licznikD())  

    #21 wykonano dla funkcji z zad. 19
    print("\nZad. 21 - wykonano dla funkcji z zad. 19")

    #22
    print("\nZad. 22")
    ksiazka1 = {"tytul": "Ten obcy", "autor": "Irena Jurgielewiczowa", "rok_wydania": 1961}
    ksiazka2 = {"tytul": "Kobieta, którą jestem", "autor": "Britney Spears", "rok_wydania": 2023}
    ksiazka3 = {"tytul": "Normalni ludzie", "autor": "Rooney Sally", "rok_wydania": 2022}
    lista_slownikow = [ksiazka1, ksiazka2, ksiazka3]
    #a
    posortowane_ksiazki = sorted(lista_slownikow, key=lambda x: x['rok_wydania'])
    print("Posortowane książki według roku wydania:")
    print(posortowane_ksiazki)
    #b
    ksiazki_po_2000 = filter(lambda x: x['rok_wydania'] > 2000, lista_slownikow)
    print("\nKsiążki wydane po 2000 roku:")
    for ksiazka in ksiazki_po_2000:
        print(ksiazka)
    #c
    tytuly_ksiazek = map(lambda x: x['tytul'], lista_slownikow)
    print("\nTytuły książek:")
    for tytul in tytuly_ksiazek:
        print(tytul)

    #23
    print("\nZad. 23")
    print("Dni tygodnia:")
    for dzien in gen():
        print(dzien)
        
    print("\nPierwsze 3 dni tygodnia:")
    dni_tyg_3 = list(gen())[:3]
    print(dni_tyg_3)

if __name__ == "__main__":
    run()