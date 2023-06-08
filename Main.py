#kullanacağımız modüller import ediyoruz
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd
#dataframe'i tam haliyle görebilmek için görüntülenen maksimum sütün saysını arttırıyoruz
pd.set_option("display.max_columns", 15)
#class örneklerimizi girip ekrana yazdırıyoruz
ornek_1 = Insan(tc_no=36256,ad="ali",soyad="kara",yas=34,cinsiyet="erkek",uyruk="türk")
ornek_2 = Insan(tc_no=36356,ad="veli",soyad="ak",yas=24,cinsiyet="erkek",uyruk="arap")

print(ornek_1.__str__(),"\n",ornek_2.__str__(),"\n")

ornek_3 = Issiz(tc_no=46256,ad="servet",soyad="şahin",yas=32,cinsiyet="erkek",uyruk="türk",mavi_yaka=5,beyaz_yaka=8,yonetici=10)
ornek_4 = Issiz(tc_no=47256,ad="melih",soyad="kaya",yas=45,cinsiyet="erkek",uyruk="türk",mavi_yaka=0,beyaz_yaka=4,yonetici=3)
ornek_5 = Issiz(tc_no=48956,ad="melike",soyad="şahin",yas=38,cinsiyet="kadın",uyruk="türk",mavi_yaka=9,beyaz_yaka=3,yonetici=0)

print(ornek_3.__str__(),"\n",ornek_4.__str__(),"\n",ornek_5.__str__(),"\n")

ornek_6 = Calisan(tc_no=57856,ad="aslı",soyad="gündoğdu",yas=44,cinsiyet="kadın",uyruk="türk",sektor="teknoloji",tecrube=78,maas=40000,yeni_maas=0)
ornek_7 = Calisan(tc_no=57906,ad="murat",soyad="yeşil",yas=54,cinsiyet="erkek",uyruk="rus",sektor="insaat",tecrube=98,maas=10000,yeni_maas=0)
ornek_8 = Calisan(tc_no=54556,ad="soner",soyad="deli",yas=24,cinsiyet="kadın",uyruk="türk",sektor="muhasebe",tecrube=36,maas=16000,yeni_maas=0)

print(ornek_6.__str__(),"\n",ornek_7.__str__(),"\n",ornek_8.__str__(),"\n")

ornek_9 = MaviYaka(tc_no=65856,ad="kerim",soyad="yılduz",yas=64,cinsiyet="erkek",uyruk="türk",sektor="teknoloji",tecrube=120,maas=23000,yeni_maas=0,yipranma_payi=0.6)
ornek_10 = MaviYaka(tc_no=32106,ad="ayşe",soyad="yıldız",yas=58,cinsiyet="kadın",uyruk="türk",sektor="teknoloji",tecrube=98,maas=16000,yeni_maas=0,yipranma_payi=0.3)
ornek_11 = MaviYaka(tc_no=12556,ad="mahmut",soyad="kesik",yas=44,cinsiyet="erkek",uyruk="çerkez",sektor="diger",tecrube=126,maas=13000,yeni_maas=0,yipranma_payi=0.8)

print(ornek_9.__str__(),"\n",ornek_10.__str__(),"\n",ornek_11.__str__(),"\n")

ornek_12 = BeyazYaka(tc_no=57906,ad="merve",soyad="bıyık",yas=33,cinsiyet="kadın",uyruk="türk",sektor="teknoloji",tecrube=28,maas=43000,yeni_maas=0,tesvik_primi=500)
ornek_13 = BeyazYaka(tc_no=47906,ad="kazım",soyad="çapa",yas=59,cinsiyet="erkek",uyruk="ermeni",sektor="insaat",tecrube=158,maas=13000,yeni_maas=0,tesvik_primi=600)
ornek_14 = BeyazYaka(tc_no=54896,ad="soner",soyad="kabadayı",yas=64,cinsiyet="erkek",uyruk="türk",sektor="muhasebe",tecrube=178,maas=22000,yeni_maas=0,tesvik_primi=250)

print(ornek_12.__str__(),"\n",ornek_13.__str__(),"\n",ornek_14.__str__(),"\n")
#dataframe'de kullanacağımız nesneleri listeye atıyoruz
nesneler = [ornek_6,ornek_7,ornek_8,ornek_9,ornek_10,ornek_11,ornek_12,ornek_13,ornek_14,]
#dataframe oluşturmak için kullanacağımız dictionary'i oluşturuyoruz
sözlük = {"tc_no": [], "ad": [], "soyad": [], "yas": [], "cinsiyet": [], "uyruk": [], "sektor": [], "tecrube(ay)": [], "maas": [],"yeni maas": [] ,"yıpranma_payi": [], "tesvik_primi": [],"çalışan_tipi": []}
#nesneler listesindeki her bir nesne için dönecek for döngüsünü açıyoruz
for nesne in nesneler:
    #nesnenin yeni maaş değerinin hesaplanması için zam hakki metodu çağırıyoruz
    nesne.zam_hakki()
    #her bir nesnenin gerekli değerleini sözlüğe kaydediyoruz
    sözlük["tc_no"].append(nesne.get_tc_no())
    sözlük["ad"].append(nesne.get_ad())
    sözlük["soyad"].append(nesne.get_soyad())
    sözlük["yas"].append(nesne.get_yas())
    sözlük["cinsiyet"].append(nesne.get_cinsiyet())
    sözlük["uyruk"].append(nesne.get_uyruk())
    sözlük["sektor"].append(nesne.get_sektor())
    sözlük["tecrube(ay)"].append(nesne.get_tecrube())
    sözlük["maas"].append(nesne.get_maas())
    sözlük["yeni maas"].append(nesne.get_yeni_maas())
    sözlük["çalışan_tipi"].append(type(nesne).__name__)
    #istenilen değerin nesnede bulnmaması haline try-except kullanarak sözlükte o değerlerin None değerini almasını sağlıyoruz
    try:
        sözlük["yıpranma_payi"].append(nesne.get_yipranma_payi())
    except AttributeError:
        sözlük["yıpranma_payi"].append(None)
    try:
        sözlük["tesvik_primi"].append(nesne.get_tesvik_primi())
    except AttributeError:
        sözlük["tesvik_primi"].append(None)
#pandas modülünü kullanarak dictionary'den dataframe oluşturuyoruz ve ekrana yazdırıyoruz
df = pd.DataFrame(sözlük).fillna(0)
print(df)

#shape metodu kullanarak maaşı 15000'den fazla olanları yazdırıyoruz
maas__15000__uzeri = df[df["maas"] > 15000].shape[0]
print("\nMaaşı 15000 TL üzerinde olanların toplam sayısı:", maas__15000__uzeri)

#dataframedeki değerleri çalışan tipine göre gruplandırıp her grubun ortalama maşş ve tecrübesini ekrana yazdırıyoruz
gruplanmis_df = df.groupby("çalışan_tipi").agg({"yeni maas": "mean", "tecrube(ay)": "mean"})
print("\nÇalışan Tiplerine Göre Ortalama Maaş ve Tecrübe:")
print(gruplanmis_df)

#yeni maaş değerine df sıralıyoruz
sıralı_df = df.sort_values("yeni maas")
print("\nyeni maaş değerine göre sıralanmış dataframe:")
print(sıralı_df)

#ay halindeki tecrube değerini yıl ahline getirip 3 seneden fazla olan beyaz yakalıları yazdırıyoruz
print("\nTecrübesi 3 seneden fazla olan Beyaz yakalılar:")
filtre = (df["çalışan_tipi"] == "BeyazYaka") & ((df["tecrube(ay)"]/12) >= 3)
print(df.loc[filtre])