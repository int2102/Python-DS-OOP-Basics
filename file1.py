class TraseuMontan:
    def __init__(self, nume, distanta, durata):
        self.nume = nume
        self.distanta = distanta
        self.durata = durata

    def __str__(self):
        return f"Traseul {self.nume} are o distanta de {self.distanta} si o durata de {self.durata}"


class Munte:
    def __init__(self):
        self.lista_trasee = []

    def adaugare_traseu(self, traseu):
        self.lista_trasee.append(traseu)

    def distanta_totala(self):
        nrkm = 0
        for traseu in self.lista_trasee:
            nrkm += traseu.distanta
        return nrkm

    def durata_totala(self):
        nrore = 0
        for traseu in self.lista_trasee:
            nrore += traseu.durata
        return nrore

    def __str__(self):
        X = len(self.lista_trasee)
        return f"avem un total de {X} trasee"


Traseu1 = TraseuMontan("Rasnov-Cabana Malaiesti", 6, 2.5)
Traseu2 = TraseuMontan("Cabana Malaiesti-Vf Omu", 4, 3)
Traseu3 = TraseuMontan("Vf Omu-Valea Cerbului-Busteni", 10, 3.5)
Bucegi = Munte()
Bucegi.adaugare_traseu(Traseu1)
Bucegi.adaugare_traseu(Traseu2)
Bucegi.adaugare_traseu(Traseu3)
print(Bucegi)
print(Bucegi.distanta_totala())
print(Bucegi.durata_totala())
