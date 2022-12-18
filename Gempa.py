class Gempa:
    #member1 variable
    lokasi = ''
    skala = 0
    #member2 konstruktor
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala
    #member3 method
    def dampak(self):
        if(self.skala < 2): ket = 'Tidak Terasa'
        elif(self.skala >= 2 and self.skala < 4): ket = 'Bangunan Retak-Retak'
        elif(self.skala >= 4 and self.skala < 6): ket = 'Bangunan Roboh'
        else: ket = 'Bangunan Roboh dan berpotensi tsunami'
        print(
            "Lokasi Gempa\t:",self.lokasi
            "\nSkala\t\t:",self.skala,"richer"
            "\nDampak\t\t:",ket,
            "\n------------------------------")
            