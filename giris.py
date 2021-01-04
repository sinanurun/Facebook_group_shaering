import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from selenium import webdriver

import anaekran


class G_penceresi(QWidget):
    def __init__(self):
        super(G_penceresi,self).__init__()
        self.pencere = loadUi("giris_ekrani.ui",self)

    def giris_kontrol(self):
        self.k_ad = self.pencere.k_adi.text()
        self.k_sifre = self.pencere.sifre.text()

        try:
            driver = webdriver.Firefox()
            driver.get("http://facebook.com")
            # //*[@id="u_0_2"]
            time.sleep(5)
            giris_yap = driver.find_element_by_xpath('//*[@id="loginbutton"]')
            ad = driver.find_element_by_xpath('//*[@id="email"]')
            ad.send_keys(self.k_ad)
            # giris_yap.click()
            sifre = driver.find_element_by_xpath('//*[@id="pass"]')
            sifre.send_keys(self.k_sifre)
            giris_yap.click()
            time.sleep(5)
            gruplar = driver.find_element_by_xpath('//textarea[@name="xhpc_message"]')
            time.sleep(5)
            driver.close()
            # yeni pencere açıp var olan pencereyi saklamak için kullanılıyor aşağıdaki kodlar
            self.hide()
            self.ype = anaekran.Ana_pencere(self.k_ad,self.k_sifre)
            # self.ype.show()


        except:
            driver.close()
            self.pencere.hatali_giris.setText("Hatalı Giriş Yaptınız"+self.k_ad)
            self.pencere.k_adi.setText("")


if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    arayuz = G_penceresi()
    arayuz.show()
    sys.exit(uygulama.exec_())