class Personaj:
    def __init__(self, nume, viata):
        self.nume = nume
        self.viata = viata

    def __str__(self):
        return f"Personajul {self.nume} are {self.viata} HP"


class Razboinic(Personaj):
    def __init__(self, nume, viata, armura):
        super().__init__(nume, viata)
        self.armura = armura

    def incaseaza_atac(self, daune):
        self.viata = self.viata - (daune - self.armura)
        self.armura = 0  # Armura se sparge dupa prima lovitura

    def __str__(self):
        return f"Razboinicul {self.nume} are {self.viata} HP si {self.armura} puncte de armura."


class Mag(Personaj):
    def __init__(self, nume, viata, mana):
        super().__init__(nume, viata)
        self.mana = mana

    def vindecare(self):
        if self.mana >= 10:
            self.mana = self.mana - 10
            self.viata += 20
        else:
            print("Mana insuficienta")

    def __str__(self):
        return f"Magul {self.nume} are {self.viata} HP si {self.mana} mana."


conan = Razboinic("Conan", 100, 5)
gandalf = Mag("Gandalf", 80, 50)

conan.incaseaza_atac(20)
gandalf.vindecare()

print(conan)
print(gandalf)
