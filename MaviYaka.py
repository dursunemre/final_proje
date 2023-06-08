#Calisan modülünde Calisan classını import ediyoruz
from Calisan import Calisan
#Calisan classını inherit eden MaviYaka classını oluşturuyoruz
class MaviYaka(Calisan):
    # istenilen değerleri içerecek init metodunu yazıyoruz
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas, yipranma_payi):
        # Insan classından inherit ettiğimiz değerlerin kullanılabilmesi için super metodunu kullanıyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas)
        self.__yipranma_payi = yipranma_payi
        #istediğimiz aralıkta yıpranma payı değeri girilmesi için while döngüsüyle kontrol edip hatalı değerde tekrar girilmesini sağlıyoruz
        while self.__yipranma_payi <= 0 or self.__yipranma_payi >= 1:
            self.__yipranma_payi = float(input("Lütfen 0 ile 1 arasında bir yıpranma payı değeri girin: "))
# private değerlere ulaşıp değiştirebilmek için get-set metodlarını yazıyoruz
    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yeni_yipranma_payi):
        if yeni_yipranma_payi <= 0 or yeni_yipranma_payi >= 1:
            yeni_yipranma_payi = float(input("Lütfen 0 ile 1 arasında bir yıpranma payı değeri girin: "))
        self.__yipranma_payi = yeni_yipranma_payi
# yeni maaş değerini hesaplamak için zam hakki metodunu yazıyoruz
    def zam_hakki(self):
        # tecrube ve maas değerlerini bizden istenilen şekilde karşılaştırıp yıpranma payı değerini de kullanarak yeni maaş değeri buluyoruz
        if self.get_tecrube() / 12 < 2:
            zam_orani = self.__yipranma_payi * 10
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (zam_orani / 100))

        elif self.get_tecrube() / 12 >= 2 and self.get_tecrube() < 4 and self.get_maas() < 15000:
            zam_orani = (self.get_maas() % self.get_tecrube()) / 2 + (self.__yipranma_payi * 10)
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (zam_orani / 100))

        elif self.get_tecrube() / 12 >= 4 and self.get_maas() < 25000:
            zam_orani = (self.get_maas() % self.get_tecrube()) / 3 + (self.__yipranma_payi * 10)
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (zam_orani / 100))

        else:
            self.set_yeni_maas(self.get_maas())

# istenilen değerleri string halinde döndürecek str metodunu yazıyoruz
    def __str__(self):
        self.zam_hakki()
        return f"AD: {self.get_ad()}, SOYAD: {self.get_soyad()}, TECRUBE(AY): {self.get_tecrube()} AY, YENI MAAS: {self.get_yeni_maas()}"