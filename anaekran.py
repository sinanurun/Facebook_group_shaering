from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import db_islemleri
import gglist
import fb_grup_listele
import fb_grubu_olustur
import fb_grubu_lg
import yeni_ileti_olustur
import taslakileti
import paylasilan_iletiler



class Ana_pencere(QMainWindow):
    def __init__(self,k_adi,sifre):
        super(Ana_pencere,self).__init__()
        self.anapencere = loadUi("anaEkran.ui",self)
        self.show()
        self.k_adi, self.k_sifre = k_adi, sifre
        self.kid= db_islemleri.uye_kaydi([self.k_adi, self.k_sifre])


    #pencere kapanınca veri tabanını kapatmak için db de ki kapat fonk çalışır
    def closeEvent(self, a0: QCloseEvent):
        db_islemleri.db_kapat()

    # güncelleme işlemini yapıyor ve eğer güncelleme işlemi başarılı olursa ekrana bu konuda bir dialog ekranı gösteriyor
    def fb_grup_guncelle(self):
        gglist.k_fb_guncelle(self.kid)

    # ana ekranda üye olunan facebook gruplarını listeliyor
    def fb_grup_listele(self):
        try:
            self.yeni = fb_grup_listele.Fb_liste(self.kid)
            self.anapencere.setCentralWidget(self.yeni)
        except:
            print("sıkıntı")

    def fb_paylasim_grubu_listele(self):
        try:
            self.pgl = fb_grubu_lg.Fb_grubu_listele(self.kid)
            self.anapencere.setCentralWidget(self.pgl)
        except:
            print("sıkıntı")

    def fb_paylasim_grubu_olustur(self):
        self.pgo = fb_grubu_olustur.Fb_grubu_olustur(self.kid)
        self.anapencere.setCentralWidget(self.pgo)

    def yeni_ileti(self):
        self.yis = yeni_ileti_olustur.Yeni_ileti(self.kid)
        self.anapencere.setCentralWidget(self.yis)

    def taslak_ileti(self):
        self.yis = taslakileti.Taslak_ileti(self.kid)
        self.anapencere.setCentralWidget(self.yis)

    def paylasilan_ileti(self):
        self.tis = paylasilan_iletiler.Pi_liste(self.kid)
        self.anapencere.setCentralWidget(self.tis)

#ana pencerenin açılmasını sağlıyor
def ana_pencere_ac():
    # uygulama = QApplication(sys.argv)
    arayuz = Ana_pencere()
    arayuz.show()
    # sys.exit(uygulama.exec_())


# bu bölüm her zaman en altta kalacak olan kısım çünkü program bu satırları gördüğü an çalışmaya başlar
# eğer sadece anaekran.py ile çalışacaksanız bunu unutmayın
if  __name__=="__main__":
    uygulama = QApplication(sys.argv)
    arayuz = Ana_pencere()
    # arayuz.show()
    sys.exit(uygulama.exec_())




