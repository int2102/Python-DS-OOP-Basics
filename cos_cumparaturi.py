class Produs:
    def __init__(self, nume, pret):
        self.nume = nume
        self.pret = pret

    def __str__(self):
        return f"{self.nume} ({self.pret} lei)"


class CosCumparaturi:  # Aici am corectat arhitectura, nu mai mosteneste Produs
    def __init__(self):
        self.continut = []

    def adauga_produs(self, produs_nou):
        self.continut.append(produs_nou)

    def calculeaza_total(self):
        total = 0
        for element in self.continut:
            total += element.pret
        return total

    def __str__(self):
        X = len(self.continut)
        return f"Cosul contine {X} produse."


telefon = Produs("iPhone 15", 4500)
husa = Produs("Husa Silicon", 100)
incarcator = Produs("Incarcator Fast", 150)

cosul_meu = CosCumparaturi()
cosul_meu.adauga_produs(telefon)
cosul_meu.adauga_produs(husa)
cosul_meu.adauga_produs(incarcator)

print(cosul_meu)
de_plata = cosul_meu.calculeaza_total()
print(f"Total de plata la casa: {de_plata} lei.")
