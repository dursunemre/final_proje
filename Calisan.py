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