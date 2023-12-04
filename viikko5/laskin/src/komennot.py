class Summa:
    def __init__(self, sovelluslogiikka, lue):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue = lue
        self.edellinen_arvo = 0
    
    def suorita(self):
        operandi = int(self.lue())
        self.edellinen_arvo = self.sovelluslogiikka.arvo()

        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.arvo() + operandi)
    
    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, lue):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue = lue
    
    def suorita(self):
        operandi = int(self.lue())

        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.arvo() - operandi)

class Nollaus:
    def __init__(self, sovelluslogiikka, lue):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue = lue

    def suorita(self):
        self.sovelluslogiikka.aseta_arvo(0)

class Kumoa:
    def __init__(self, sovelluslogiikka, lue):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue = lue

    def suorita(self):
        pass