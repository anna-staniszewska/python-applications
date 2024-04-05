def stworz_funkcje_potegujaca(wykladnik: int) -> callable:
    def poteguj(podstawa: int) -> int:
        return podstawa ** wykladnik
    return poteguj