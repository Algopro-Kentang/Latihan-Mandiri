class Tabung(object):

    def __init__(self, jari, tinggi):
        """Property yang tidak mempunyai nilai default"""
        self.r = jari
        self.t = tinggi
    def volume(self):
        """volume tabung"""
        phi = 3.14
        V = phi * self.r * self.r * self.t
        return V
    def luas(self):
        """luas permukaan tabung"""
        phi = 3.14
        L = 2 * phi * self.r * (self.r + self.t)
        return L

tabung_abc = Tabung(1, 18)
print(tabung_abc.luas())

def tambah(angka_1,angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,10)