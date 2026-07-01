class ContBancar:
    def __init__(self, nume, sold):
        self.nume = nume
        self.sold = sold

    def depunere(self, suma_depusa):
        self.sold += suma_depusa

    def retragere(self, suma_retrasa):
        if self.sold - suma_retrasa >= 0:
            self.sold = self.sold - suma_retrasa
        else:
            print("Persoana nu are suficient sold in cont")

    def __str__(self):
        return f"Titular: {self.nume}, Sold Curent: {self.sold} lei"


persoana = ContBancar("Maria", 1800)
persoana.depunere(100)
persoana.retragere(500)
print(persoana)
