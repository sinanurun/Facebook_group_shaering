from PyQt5.QtWidgets import *
from PyQt5.uic import *
import db_islemleri
import sys


class Fb_grubu_listele(QWidget):

    def __init__(self,k_id):

        super(Fb_grubu_listele,self).__init__()

        self.k_id = k_id
        self.ekran = loadUi("fb_paylasim_grubu_lg.ui", self)

        self.gl()

    def listele(self):
        self.a = 0
        self.ck = {}
        # print(self.secilen)
        icerik = self.db_g_listesi[self.secilen][2].split("+")
        # print(icerik)
        self.grupid = self.db_g_listesi[0]
        self.db_g_liste = db_islemleri.grup_listele(self.k_id)

        self.satir_sayisi = len(self.db_g_liste)
        self.p_grup_listesi = []
        self.tablo = self.ekran.grup_tablosu
        self.tablo.setRowCount(self.satir_sayisi)
        self.tablo.setColumnCount(2)
        self.tablo.setColumnWidth(0, 30)
        self.tablo.setColumnWidth(1, 550)

        for k in self.db_g_liste:
            self.kutu = QCheckBox(self)
            self.ck[self.a] = [k[0],self.kutu]
            self.tablo.setCellWidget(self.a, 0, self.kutu)
            if str(k[0]) in icerik:
                self.kutu.setChecked(1)
            self.tablo.setItem(self.a, 1, QTableWidgetItem(str(k[1])))

            self.a += 1

    def gl(self):
        self.db_g_listesi = db_islemleri.p_grup_listele(self.k_id)
        self.pgruplari = []
        self.ekran.fb_pg_list.clear()
        for z in self.db_g_listesi:
            self.pgruplari.append([z[1], z[0]])
        self.ekran.fb_pg_list.addItems(x[0] for x in self.pgruplari)
        self.secilen = self.ekran.fb_pg_list.currentIndex()

        self.listele()
        self.ekran.fb_pg_list.currentIndexChanged.connect(self.selectionchange)


    def selectionchange(self):
        self.secilen = self.ekran.fb_pg_list.currentIndex()
        return self.listele()


    def ck_kontrol(self):
        self.grup_adi = self.ekran.fb_pg_list.currentText()
        self.p_grup_listesi.append(self.grup_adi)
        for k in range(self.satir_sayisi):
            if self.ck[k][1].isChecked():
                self.p_grup_listesi.append(self.ck[k][0])
                # print("+", self.ck[k][0])
        self.p_grup_listesi.append(self.k_id)
        self.p_grup_listesi[0]=self.pgruplari[self.secilen][1]
        db_islemleri.paylasim_grubu_guncelle(self.p_grup_listesi)
        self.gl()
        # self.ekran.fb_pg_list.setCurrentIndex(0)
        # self.listele()


if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    arayuz = Fb_grubu_listele(1)
    arayuz.show()
    sys.exit(uygulama.exec_())