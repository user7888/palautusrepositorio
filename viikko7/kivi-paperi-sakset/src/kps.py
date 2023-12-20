from tuomari import Tuomari

class KiviPaperiSakset:
    def __init__(self):
        self.tuomari = Tuomari()
        self.ekan_siirto = None
        self.tokan_siirto = None

    def pelaa(self):
        self._lue_siirrot()

        while self._onko_ok_siirto(self.ekan_siirto) and self._onko_ok_siirto(self.tokan_siirto):
            self.tuomari.kirjaa_siirto(self.ekan_siirto, self.tokan_siirto)
            self._pelin_tilanne()
            self._lue_siirrot()
        
        self._lopeta_peli()

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
    
    def _pelin_tilanne(self):
        print(self.tuomari)
    
    def _lue_siirrot(self):
        self.ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self.tokan_siirto = self._toisen_siirto()
    
    def _lopeta_peli(self):
        print("Kiitos!")
        self._pelin_tilanne()