def licznikD():
    l_d = getattr(licznikD, 'l', 0)
    licznikD.l = l_d + 1
    return licznikD.l