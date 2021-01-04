from PyQt5.QtWidgets import *
from PyQt5.uic import *
import db_islemleri
import sys

class Pi_liste(QWidget):
    def __init__(self,k_id):
        super(Pi_liste,self).__init__()

        self.ekran = loadUi("paylasilan_iletiler.ui",self)

        db_g_listesi = db_islemleri.paylasilanlar(k_id)
        # print(db_g_listesi)
        self.satir_sayisi = len(db_g_listesi)
        g_listeleri = db_islemleri.grup_listele(k_id)
        p_listeleri =db_islemleri.p_grup_listele(k_id)
        self.tablo = self.ekran.grup_tablosu
        self.tablo.setRowCount(self.satir_sayisi)
        self.tablo.setColumnCount(4)
        self.tablo.setColumnWidth(0, 150)
        self.tablo.setColumnWidth(1, 300)
        self.tablo.setColumnWidth(2, 150)
        self.tablo.setColumnWidth(3, 250)
        a=0
        for k in db_g_listesi:
            # print(k)
            self.tablo.setItem(a, 0, QTableWidgetItem(str(k[1])))
            self.tablo.setItem(a, 1, QTableWidgetItem(str(k[2])))
            pgrup_idleri =((k[5][1:])[:-1]).split(", ")
            self.combo = QComboBox(self)
            # print(grup_idleri)

            for x in p_listeleri:
                if str(x[0]) in pgrup_idleri:
                    # print(x[1])
                    self.combo.addItem(x[1])
            self.tablo.setCellWidget(a, 2, self.combo)

            grup_idleri = ((k[6][1:])[:-1]).split(", ")
            self.combo2 = QComboBox(self)
            for x in g_listeleri:
                if str(x[0]) in grup_idleri:
                    # print(x[1])
                    self.combo2.addItem(x[1])

                    self.tablo.setCellWidget(a, 3, self.combo2)
            a+=1
if  __name__=="__main__":
    uygulama = QApplication(sys.argv)
    arayuz = Pi_liste(1)
    arayuz.show()
    sys.exit(uygulama.exec_())