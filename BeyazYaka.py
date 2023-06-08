#Calisan modülünde Calisan classını import ediyoruz
from Calisan import Calisan
#Calisan classını inherit eden BeyazYaka classını oluşturuyoruz
class BeyazYaka(Calisan):
    # istenilen değerleri içerecek init metodunu yazıyoruz
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas, tesvik_primi):
        # Insan classından inherit ettiğimiz değerlerin kullanılabilmesi için super metodunu kullanıyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas)
        self.__tesvik_primi = tesvik_primi
        # istediğimiz aralıkta tesvik primi değeri girilmesi için while döngüsüyle kontrol edip hatalı değerde tekrar girilmesini sağlıyoruz
        while self.__tesvik_primi < 100:
            self.__tesvik_primi = int(input("Lütfen 100'den büyük bir teşvik primi değeri girin:"))
# private değerlere ulaşıp değiştirebilmek için get-set metodlarını yazıyoruz
    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, yeni_tesvik_primi):
        while yeni_tesvik_primi < 100:
            yeni_tesvik_primi = int(input("Lütfen 100'den büyük bir teşvik primi değeri girin:"))
        self.__tesvik_primi = yeni_tesvik_primi