class Planet(object):
    def __init__(self,jari = 696342):
        self.r = jari
    
    def luas(self):
        return 4 * 3.14 * (self.r ** 2)

    def volume(self):
        return 3 * 3.14 * (self.r**3)