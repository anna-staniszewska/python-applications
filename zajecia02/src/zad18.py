def stworz_raport(*args, **kwargs):
    description = ""
    for produkt_id in args:
        description = description + f'Informacje o produkcie o ID {produkt_id} - '
        for key, value in kwargs.items():
            if key.endswith(str(produkt_id) + '_nazwa') or key.endswith(str(produkt_id) + '_cena'):
                description = description + f"{key.split('_', 2)[2]}: {value} "
        description = description + f'\n'
    return description