def licznikA():
    l_a = 0
    
    def zwieksz():
        nonlocal l_a
        l_a += 1
        return l_a
    
    return zwieksz