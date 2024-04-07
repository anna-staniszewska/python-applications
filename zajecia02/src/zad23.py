def gen():
    dni_tygodnia = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
    i = 0
    while i<7:
        yield dni_tygodnia[i]
        i += 1