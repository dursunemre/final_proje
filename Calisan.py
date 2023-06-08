#Insan modülünde Insan classını import ediyoruz
from Insan import Insan
#Insan classını inherit eden Calisan classını oluşturuyoruz
class Calisan(Insan):
    # istenilen değerleri içerecek init metodunu yazıyoruz
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas=None):
        # Insan classından inherit ettiğimiz değerlerin kullanılabilmesi için super metodunu kullanıyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        sektor_liste = ["teknoloji", "muhasebe", "insaat", "diger"]
        #nesneye girilen sektör değerinin geçerli değerleden biri olması için while döngüsüyle kontrol ediyoruz ve hatalıysa tekrar girmesini istiyoruz
        while self.__sektor not in sektor_liste:
            self.__sektor = input("lütfen sektör değerini inşaat, muhasebe, teknoloji veya diğer olarak girin:")
        self.__tecrube = tecrube
        self.__maas = maas
        if yeni_maas is None:
            self.__yeni_maas = yeni_maas
# private değerlere ulaşıp değiştirebilmek için get-set metodlarını yazıyoruz
    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor_deger):
        sektor_liste = ["teknoloji", "muhasebe", "insaat", "diger"]
        while sektor_deger not in sektor_liste:
            sektor_deger = input("lütfen sektör değerini inşaat, muhasebe, teknoloji veya diğer olarak girin:")
        self.__sektor = sektor_deger

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, yeni_tecrube):
        self.__tecrube = yeni_tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, yeni_maas):
        self.__maas = yeni_maas

    def get_yeni_maas(self):
        return self.__yeni_maas

    def set_yeni_maas(self, yeni_yeni_maas):
        self.__yeni_maas = yeni_yeni_maas
# private değerlere ulaşıp değiştirebilmek için get-set metodlarını yazıyoruz
    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor_deger):
        sektor_liste = ["teknoloji", "muhasebe", "insaat", "diger"]
        while sektor_deger not in sektor_liste:
            sektor_deger = input("lütfen sektör değerini inşaat, muhasebe, teknoloji veya diğer olarak girin:")
        self.__sektor = sektor_deger

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, yeni_tecrube):
        self.__tecrube = yeni_tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, yeni_maas):
        self.__maas = yeni_maas

    def get_yeni_maas(self):
        return self.__yeni_maas

    def set_yeni_maas(self, yeni_yeni_maas):
        self.__yeni_maas = yeni_yeni_maas
# istenilen değerleri string halinde döndürecek str metodunu yazıyoruz
    def __str__(self):
        self.zam_hakki()
        return f"AD: {self.get_ad()}, SOYAD: {self.get_soyad()}, TECRUBE: {self.get_tecrube()} AY, YENI MAAS: {self.get_yeni_maas()}"