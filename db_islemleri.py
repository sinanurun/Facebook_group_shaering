import os
import sqlite3 as sql

vt = sql.connect('fb_db.sqlite')
imlec = vt.cursor()

def uye_kaydi(k_bilgileri):
    try:
        print(k_bilgileri)
        imlec.execute("SELECT * FROM kullanici where kullanici_eposta=='{}'".format(k_bilgileri[0]))
        kayitlar = imlec.fetchall()
        if len(kayitlar)>0:
            k_idsi = kayitlar[0][0]
            return k_idsi
            print(kayitlar[0][0],"a")
        else:
            y_kullanici = """INSERT INTO kullanici (kullanici_eposta,kullanici_sifre) VALUES ("{}","{}")""".format(k_bilgileri[0].replace('"', "'"), k_bilgileri[1])
            imlec.execute(y_kullanici)
            vt.commit()
            imlec.execute("SELECT * FROM kullanici where kullanici_eposta=='{}'".format(k_bilgileri[0]))
            kayitlar = imlec.fetchall()
            k_idsi = kayitlar[0][0]
            return k_idsi
        # vt.close()
    except:
        print("hatalı işlem")

def kullanici_bilgileri(k_id):
    imlec.execute("SELECT * FROM kullanici where kullanici_id='{}'".format(k_id))
    kayitlar = imlec.fetchall()
    return kayitlar
    # vt.close()

def grup_listele(k_id=1):
    try:
        imlec.execute("SELECT * FROM gruplar where k_id=={}".format(k_id))
        kayitlar = imlec.fetchall()
        return kayitlar
    except:
        return [0]
    vt.commit()
    # vt.close()

def paylasim_grubu_olustur(p_grup_listesi):
    # print(p_grup_listesi)
    grup_adi = p_grup_listesi[0]
    p_grup_listesi.pop(0)
    k_id = p_grup_listesi[-1]
    p_grup_listesi.pop(-1)
    gruplar=str(p_grup_listesi[0])
    for x in p_grup_listesi[1:]:
        gruplar = gruplar +"+"+ str(x)
    grup_kaydi = """INSERT INTO paylasim_gruplari (p_grup_adi,grup_id_havuzu,k_id) VALUES ("{}","{}","{}")""".format(grup_adi,gruplar,k_id)
    imlec.execute(grup_kaydi)
    vt.commit()

def p_grup_listele(k_id=1):
    try:
        imlec.execute("SELECT * FROM paylasim_gruplari where k_id=={}".format(k_id))
        kayitlar = imlec.fetchall()
        return kayitlar
    except:
        return [0]
    vt.commit()

def grup_guncelle(ggruplar,k_id):

    # try:
    #     imlec.execute("SELECT * FROM gruplar where k_id=={}".format(k_id))
    #     kayitlar = imlec.fetchall()
    #     print(kayitlar)
    # except:
    #     print("kayıt yok")
    #     kayitlar=[]
    # # print(ggruplar)
    for grup in ggruplar:
        # print(grup,k_id)
        # print(grup)
        gp = (grup[0].replace('"',"")).replace("'","")
        gpl = (grup[2].replace('"', "")).replace("'", "")
        imlec.execute("SELECT * FROM gruplar where k_id=={} and fb_grup_linki=='{}'".format(k_id,gpl))
        kayitlar2 = imlec.fetchall()
        print(len(kayitlar2))
        if len(kayitlar2)==0:
            grup_kaydi = 'INSERT INTO gruplar (grup_adi,fb_grup_id,fb_grup_linki,k_id) VALUES ("{}",{},"{}",{})'.format(gp,grup[1],gpl,k_id)
            print(grup_kaydi)
            imlec.execute(grup_kaydi)
            print("a")
            vt.commit()
        # else:
        #     pass
        #     print("hata")
    # vt.close()

def paylasim_grubu_guncelle(p_grup_listesi):
    # print(p_grup_listesi)
    grup_id = p_grup_listesi[0]
    p_grup_listesi.pop(0)
    k_id = p_grup_listesi[-1]
    p_grup_listesi.pop(-1)
    gruplar = str(p_grup_listesi[0])
    for x in p_grup_listesi[1:]:
        gruplar = gruplar + "+" + str(x)
    grup_kaydi = "UPDATE paylasim_gruplari SET grup_id_havuzu = '{}' WHERE p_grup_id = '{}'".format(
        gruplar, grup_id)
    imlec.execute(grup_kaydi)
    vt.commit()

def yeni_ileti_kaydet(bilgiler):
    imlec.execute("insert into iletiler (ileti_baslik, ileti_icerik, ileti_durum, kullanici_id, payslasim_gruplari, gruplar) values ('{}','{}','{}','{}','{}','{}')".format(*bilgiler))
    vt.commit()

def taslak_ileti_listesi(k_id=1):
    try:
        imlec.execute("""select * from iletiler where ileti_durum=='0' and kullanici_id=={}""".format(k_id))
        taslak_iletiler = imlec.fetchall()
        return taslak_iletiler
    except:
        pass
def ileti_guncelle(bilgiler):
    try:
        imlec.execute("update iletiler set ileti_baslik= '{}',ileti_icerik= '{}', ileti_durum= '{}',kullanici_id= '{}', payslasim_gruplari= '{}', gruplar= '{}' where ileti_id=='{}'".format(*bilgiler[1:],bilgiler[0]))
        vt.commit()
    except:
        print("güncelleme hatası")

def paylasilanlar(k_id=1):
    try:
        imlec.execute("""select * from iletiler where ileti_durum=='1' and kullanici_id=={}""".format(k_id))
        paylasilan_iletiler = imlec.fetchall()
        return paylasilan_iletiler
    except:
        pass


def db_kapat():
    vt.close()

