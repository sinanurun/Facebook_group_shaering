from PyQt5.QtWidgets import *
from PyQt5.uic import *
import db_islemleri
import sys

class Fb_liste(QWidget):
    def __init__(self,k_id):
        super(Fb_liste,self).__init__()

        self.ekran = loadUi("grup_listeleme.ui",self)

        db_g_listesi = db_islemleri.grup_listele(k_id)
        # print(db_g_listesi)
        self.satir_sayisi = len(db_g_listesi)

        self.tablo = self.ekran.grup_tablosu
        self.tablo.setRowCount(self.satir_sayisi)
        self.tablo.setColumnCount(2)
        self.tablo.setColumnWidth(0, 300)
        self.tablo.setColumnWidth(1, 300)
        a=0
        for k in db_g_listesi:
            # print(k)
            self.tablo.setItem(a, 0, QTableWidgetItem(str(k[1])))
            self.tablo.setItem(a, 1, QTableWidgetItem(str(k[3])))
            a+=1
if  __name__=="__main__":
    uygulama = QApplication(sys.argv)
    arayuz = Fb_liste(1)
    arayuz.show()
    sys.exit(uygulama.exec_())