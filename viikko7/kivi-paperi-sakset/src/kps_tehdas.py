from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KiviPaperiSaksetTehdas:
    @staticmethod
    def luo_kaksinpeli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_yksinpeli():
        return KPSTekoaly()

    @staticmethod
    def luo_vaikea_yksinpeli():
        return KPSParempiTekoaly()