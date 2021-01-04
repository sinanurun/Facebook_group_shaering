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

# ileti = [self.ileti_baslik,self.ileti_icerik,self.durum,self.k_id,self.fpg,self.gonderilecek_gruplar]
def ileti_paylas(ileti):
    try:
        p_gruplar = ileti[-1]

        tum_gruplar = db_islemleri.grup_listele(ileti[3])
        adresler = []
        kullanici = db_islemleri.kullanici_bilgileri(ileti[3])
        print(kullanici[0][1])
        driver = webdriver.Firefox()
        driver.get("http://facebook.com")
        # //*[@id="u_0_2"]
        time.sleep(5)
        giris_yap = driver.find_element_by_xpath('//*[@id="loginbutton"]')
        ad = driver.find_element_by_xpath('//*[@id="email"]')
        ad.send_keys(kullanici[0][1])
        # giris_yap.click()
        sifre = driver.find_element_by_xpath('//*[@id="pass"]')
        sifre.send_keys(kullanici[0][2])
        giris_yap.click()
        time.sleep(5)
        gruplar = driver.find_element_by_xpath('//textarea[@name="xhpc_message"]')
        time.sleep(5)

        for k in tum_gruplar:
            if k[0] in p_gruplar:
                adresler.append(k[3])
                try:

                    # gruplar.send_keys("merhaba")
                    # time.sleep(5)
                    # paylas = driver.find_element_by_xpath('//button[contains(@data-testid,"react-composer-post-button")]')
                    # time.sleep(5)
                    # paylas.click()
                    # gruplar.click()
                    # time.sleep(5)
                    driver.get(k[3])
                    time.sleep(5)
                    ilk = driver.find_element_by_xpath('//textarea[@name="xhpc_message_text"]')
                    ilk.send_keys(ileti[1])
                    time.sleep(5)
                    paylas = driver.find_element_by_xpath('//button[@data-testid="react-composer-post-button"]')
                    time.sleep(5)
                    paylas.click()
                    time.sleep(5)

                except:
                    pass


        driver.close()

    except:
        print("hata var")