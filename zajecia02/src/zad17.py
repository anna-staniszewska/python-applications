def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    pass
    calkowity_koszt = cena*ilosc
    podsumowanie = f"Nazwa produktu: {nazwa_produktu}, całkowity koszt: {calkowity_koszt}, ilość: {ilosc}"
    return [podsumowanie, calkowity_koszt]