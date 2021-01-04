from PyQt5.QtWidgets import *
from PyQt5.uic import *
import db_islemleri
import sys


class Fb_grubu_olustur(QWidget):

    def __init__(self,k_id):

        super(Fb_grubu_olustur,self).__init__()

        self.k_id = k_id
        self.ekran = loadUi("fb_paylasim_grubu_olustur.ui", self)

        self.p_grup_listesi = []


        db_g_listesi = db_islemleri.grup_listele(k_id)
        self.satir_sayisi = len(db_g_listesi)

        self.tablo = self.ekran.grup_tablosu
        self.tablo.setRowCount(self.satir_sayisi)
        self.tablo.setColumnCount(2)
        self.tablo.setColumnWidth(0, 30)
        self.tablo.setColumnWidth(1, 550)

        self.a = 0
        self.ck = {}

        for k in db_g_listesi:
            self.kutu = QCheckBox(self)
            self.ck[self.a]=[k[0],self.kutu]
            self.tablo.setCellWidget(self.a, 0, self.kutu)
            self.tablo.setItem(self.a, 1, QTableWidgetItem(str(k[1])))
            self.a += 1

    def ck_kontrol(self):
        self.grup_adi = self.ekran.p_grup_adi.text()
        self.p_grup_listesi.append(self.grup_adi)
        for k in range(self.satir_sayisi):
            if self.ck[k][1].isChecked():
                self.p_grup_listesi.append(self.ck[k][0])
                # print("+", self.ck[k][0])
        self.p_grup_listesi.append(self.k_id)
        # print(self.p_grup_listesi)
        db_islemleri.paylasim_grubu_olustur(self.p_grup_listesi)
        self.p_grup_listesi.clear()

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    arayuz = Fb_grubu_olustur(1)
    arayuz.show()
    sys.exit(uygulama.exec_())