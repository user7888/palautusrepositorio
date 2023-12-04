class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, listan_koko=5, kasvatuskoko=5):
        if not isinstance(listan_koko, int) or not isinstance(kasvatuskoko, int):
            raise TypeError("Kapasiteetin ja kasvatuskoon on oltava kokonaislukuja")
        elif not listan_koko > 0 or not kasvatuskoko > 0:
            raise ValueError("Kapasiteetin ja kasvatuskoon on oltava positiivisia")
        
        self.kapasiteetti = listan_koko
        self.kasvatuskoko = kasvatuskoko
        self.lista = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, etsittava):
        loydettyjen_lkm = 0

        for i in range(0, self.alkioiden_lkm):
            if etsittava == self.lista[i]:
                loydettyjen_lkm = loydettyjen_lkm + 1

        if loydettyjen_lkm > 0:
            return True
        else:
            return False

    def lisaa(self, lisattava):
        if self.alkioiden_lkm == 0:
            self.lista[0] = lisattava
            self.alkioiden_lkm = self.alkioiden_lkm + 1

        if not self.kuuluu(lisattava):
            self.lista[self.alkioiden_lkm] = lisattava
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.lista) == 0:
                self.kasvata_listaa(self.lista)
    
    def kasvata_listaa(self, vanha_lista):
        self.lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(vanha_lista, self.lista)

    def poista(self, poistettava):
        poistetun_indeksi = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if poistettava == self.lista[i]:
                poistetun_indeksi = i  # siis luku löytyy tuosta kohdasta :D
                self.lista[poistetun_indeksi] = 0
                break

        if poistetun_indeksi != -1:
            self.poista_nolla(poistetun_indeksi)

    def poista_nolla(self, poistetun_indeksi):
        for j in range(poistetun_indeksi, self.alkioiden_lkm - 1):
            apu = self.lista[j]
            self.lista[j] = self.lista[j + 1]
            self.lista[j + 1] = apu

        self.alkioiden_lkm = self.alkioiden_lkm - 1

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.lista[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lista[0]) + "}"
        else:
            merkkijono = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                merkkijono = merkkijono + str(self.lista[i])
                merkkijono = merkkijono + ", "
            merkkijono = merkkijono + str(self.lista[self.alkioiden_lkm - 1])
            merkkijono = merkkijono + "}"
            return merkkijono
