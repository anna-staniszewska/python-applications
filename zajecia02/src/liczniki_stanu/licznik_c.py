class LicznikC:
    def __init__(self):
        self.l_c = 0
    
    def __call__(self):
        self.l_c += 1
        return self.l_c