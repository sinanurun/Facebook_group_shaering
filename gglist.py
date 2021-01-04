#güncel grup liste işlemleri yapılacak bölüm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PyQt5.QtWidgets import *
from PyQt5.uic import *
import sys
import re
import db_islemleri



def k_fb_guncelle(k_id):

    try:
        kullanici_bilgileri = db_islemleri.kullanici_bilgileri(k_id)

        driver = webdriver.Firefox()
        driver.get("http://facebook.com")
        # //*[@id="u_0_2"]
        time.sleep(5)
        giris_yap = driver.find_element_by_xpath('//*[@id="loginbutton"]')
        ad = driver.find_element_by_xpath('//*[@id="email"]')
        ad.send_keys(kullanici_bilgileri[0][1])
        # giris_yap.click()
        sifre = driver.find_element_by_xpath('//*[@id="pass"]')
        sifre.send_keys(kullanici_bilgileri[0][2])
        giris_yap.click()
        time.sleep(5)
        driver.get("https://www.facebook.com/groups/?ref=bookmarks")
        time.sleep(5)
        for a in range(60):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        # print(driver.page_source)
        a = driver.page_source
        f = open("deneme.txt", "w", encoding="utf-8")
        f.write(a)

        p = 0
        f = open("deneme.txt", "r", encoding="utf-8")
        k = f.read()
        gruplar = []
        bolmeler = k.split('<div class="_266w">')
        for a in bolmeler[1:-1]:
            p = p + 1
            k = a.split('</a></div>')
            # print(k[0])
            link = k[0][9:].split('" data')
            glinki = "http://facebook.com" + link[0][:-21]
            g_adi = a.split('>')
            g_g_adi = g_adi[1][:-3]
            # print(k[1][:50])
            # # print(z[1][:20])
            # print([g_g_adi, p, glinki])
            gruplar.append([g_g_adi, p, glinki])
        # print(gruplar)
        db_islemleri.grup_guncelle(gruplar,k_id)
        guncelleme = FbGuncellendi()
    except:
        return print("8")
class FbGuncellendi(QDialog):
    def __init__(self):
        super(FbGuncellendi,self).__init__()
        self.dp = loadUi("fb_guncellendi.ui",self)
        self.show()
        self.exec_()



if __name__ == "__main__":
    uyari = QApplication(sys.argv)
    k_fb_guncelle(1)
    sys.exit(uyari.exec_())


# """<div class="_266w"><a href="/groups/1875587072556848/?ref=group_browse_new" data-hovercard="/ajax/hovercard/group.php?id=1875587072556848&amp;ref=group_browse_new" data-hovercard-prefer-more-content-show="1">Microbit Türkiye</a></div>"""