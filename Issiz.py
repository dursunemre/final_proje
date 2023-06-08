#Insan modülünde Insan classını import ediyoruz
from Insan import Insan
#Insan classını inherit eden Issiz classını oluşturuyoruz
class Issiz(Insan):
    #istenilen değerleri içerecek init metodunu yazıyoruz
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,mavi_yaka,beyaz_yaka,yonetici, tecrube= None,statu=None):
        #Insan classından inherit ettiğimiz değerlerin kullanılabilmesi için super metodunu kullanıyoruz
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk)
        self.__mavi_yaka = mavi_yaka
        self.__beyaz_yaka = beyaz_yaka
        self.__yonetici = yonetici
        #tecrube dictionarymizin içi boşsa içine giridğimiz beyaz yaka,mavi yaka ve yönetici tecrubesi değerlerini atıyoruz
        if tecrube is None:
            tecrube = {"mavi yaka": mavi_yaka, "beyaz yaka": beyaz_yaka, "yonetici": yonetici}
        self.__tecrube = tecrube
        #statü değerini statü bul metodu kullanarak bulduruyoruz
        if statu is None:
            self.__statu = self.statu_bul()

    # private değerlere ulaşıp değiştirebilmek için get-set metodlarını yazıyoruz
    def get_mavi_yaka_tecrube(self):
        return self.__tecrube["mavi yaka"]

       def set_mavi_yaka_tecrube(self, yeni_mavi_yaka_tecrube):
        self.__mavi_yaka = yeni_mavi_yaka_tecrube

    def get_beyaz_yaka_tecrube(self):
        return self.__tecrube["beyaz yaka"]

    def set_beyaz_yaka_tecrube(self, yeni_beyaz_yaka_tecrube):
        self.__beyaz_yaka = yeni_beyaz_yaka_tecrube

    def get_yonetici_tecrube(self):
        return self.__tecrube["yonetici"]

    def set_yonetici_tecrube(self, yeni_yonetici_tecrube):
        self.__mavi_yaka = yeni_yonetici_tecrube

    def get_statu(self):
        return self.__statu