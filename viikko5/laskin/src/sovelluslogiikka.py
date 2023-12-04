class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_arvo = 0
        self._edellinen_komento = None

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def aseta_edellinen_komento(self, komento):
        self._edellinen_komento = komento

    def edellinen_komento(self):
        return self._edellinen_komento