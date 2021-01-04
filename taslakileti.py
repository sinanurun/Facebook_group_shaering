from PyQt5.QtWidgets import *
from PyQt5.uic import *
import db_islemleri
import sys
import selenium_ileti_paylasma


class Taslak_ileti(QWidget):

    def __init__(self,k_id):

        super(Taslak_ileti,self).__init__()

        self.k_id = k_id
        self.ekran = loadUi("taslakileti.ui", self)

        self.ilk()

    def ilk(self):
        self.ileti_list = db_islemleri.taslak_ileti_listesi(self.k_id)

        self.il()

    def il(self):
        self.ekran.ileti_basliklari.clear()
        for x in self.ileti_list:
            self.ekran.ileti_basliklari.addItem(x[1],userData=x[0])
        self.secilen = self.ekran.ileti_basliklari.currentIndex()
        self.secilen_id =self.ekran.ileti_basliklari.itemData(self.secilen)
        self.secilen_baslik = self.ekran.ileti_basliklari.itemText(self.secilen)
        self.listele()
        self.ekran.ileti_basliklari.currentIndexChanged.connect(self.selectionchange)


    def selectionchange(self):
        self.secilen = self.ekran.ileti_basliklari.currentIndex()
        self.secilen_id = self.ekran.ileti_basliklari.itemData(self.secilen)
        self.secilen_baslik = self.ekran.ileti_basliklari.itemText(self.secilen)
        return self.listele()

    def listele(self):
        ileti_icerik = self.ileti_list[self.secilen][2]
        self.ekran.ileti_icerigi.setPlainText(ileti_icerik)

        self.paylasim_gruplari_listesi()
        self.tum_gruplari_listele()

    def paylasim_gruplari_listesi(self):
        self.fpg = []
        self.db_g_listesi = db_islemleri.p_grup_listele(self.k_id)
        self.satir_sayisi1 = len(self.db_g_listesi)
        self.p_grup_listesi = []
        self.tablo1 = self.ekran.paylasim_gruplari
        self.tablo1.setRowCount(self.satir_sayisi1)
        self.tablo1.setColumnCount(2)
        self.tablo1.setColumnWidth(0, 30)
        self.tablo1.setColumnWidth(1, 450)
        self.ck={}
        self.a=0
        for k in self.db_g_listesi:
            self.kutu = QCheckBox(self)
            if str(k[0]) in self.ileti_list[self.secilen][5]:
                self.kutu.setChecked(1)
                self.fpg.append(k[0])
            self.ck[self.a] = [k,self.kutu]
            self.tablo1.setCellWidget(self.a, 0, self.kutu)
            self.tablo1.setItem(self.a, 1, QTableWidgetItem(str(k[1])))
            self.kutu.stateChanged.connect(self.ap)
            self.a += 1

    def ap(self):
        self.pgruplari = []
        self.fpg=[]
        for k in self.ck:
            if self.ck[k][1].isChecked():
                self.fpg.append(self.ck[k][0][0])
                elemanlar = self.ck[k][0][2].split("+")
                for z in elemanlar:
                    if not z in self.pgruplari:
                        self.pgruplari.append(z)

        for k in self.ck2:
            if str(self.ck2[k][0][0]) in self.pgruplari:
                self.ck2[k][1].setChecked(1)


    def tum_gruplari_listele(self):
        self.db_g_listesi2 = db_islemleri.grup_listele(self.k_id)
        # print(db_g_listesi)
        self.satir_sayisi2 = len(self.db_g_listesi2)

        self.tablo2 = self.ekran.gruplar
        self.tablo2.setRowCount(self.satir_sayisi2)
        self.tablo2.setColumnCount(2)
        self.tablo2.setColumnWidth(0, 30)
        self.tablo2.setColumnWidth(1, 450)
        self.ck2={}
        self.b=0
        for k in self.db_g_listesi2:
            self.kutu2=QCheckBox(self)
            if str(k[0]) in self.ileti_list[self.secilen][6]:
                self.kutu2.setChecked(1)
            self.ck2[self.b] = [k, self.kutu2]
            self.tablo2.setCellWidget(self.b, 0, self.kutu2)
            self.tablo2.setItem(self.b, 1, QTableWidgetItem(str(k[1])))
            self.b+=1

    def ileti_onay(self):
        self.ileti_iceri = self.ekran.ileti_icerigi.toPlainText()
        self.gonderilecek_gruplar = []
        for k in self.ck2:
            if self.ck2[k][1].isChecked():
                self.gonderilecek_gruplar.append(self.ck2[k][0][0])
        self.durum = self.ekran.paylasim_durumu.currentIndex()

        ileti = (self.secilen_id,self.secilen_baslik,self.ileti_iceri,self.durum,self.k_id,self.fpg,self.gonderilecek_gruplar)

        # if self.durum == 0:
        db_islemleri.ileti_guncelle(ileti)
        if self.durum ==1:
            loadUi("ileti_paylasma.ui", self)
            self.close()
            self.yp = Ileti_paylasma(ileti)
            self.yp.show()
        else:
            return self.ilk()


class Ileti_paylasma(QWidget):
    def __init__(self,ileti):
        super(Ileti_paylasma,self).__init__()
        self.uyari = loadUi("ileti_paylasma.ui", self)
        self.sonuc = selenium_ileti_paylasma.ileti_paylas(ileti)
        # if self.sonuc[0] == 0:
        #     self.close()



if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    arayuz = Taslak_ileti(1)
    arayuz.show()
    sys.exit(uygulama.exec_())

