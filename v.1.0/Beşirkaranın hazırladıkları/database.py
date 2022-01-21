
import mysql.connector





class tablo():
    def __init__(self) :
        self.baglanti  = mysql.connector.connect(
        host="sql11.freemysqlhosting.net",
        db="sql11438034",
        user=" sql11438034",
        password="AqTp9ZelPA"
        )
        self.cursor  = self.baglanti.cursor()
        
    def yonetici_tablosu(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS yonetici (İsim TEXT,sifre TEXT)")
        self.baglanti.commit()
    def yonetici_ekle(self,kullanici_adi,sifre):
        self.cursor.execute("insert into yonetici Values(%s,%s)",(kullanici_adi,sifre))
        self.baglanti.commit()
    def yonetici_kontrol(self):
        self.cursor.execute("select İsim,sifre from yonetici")
        liste = self.cursor.fetchall()
        return liste
    def ogrenci_tablosu(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS ogrenci (ogrenci_id INTEGER PRIMARY KEY ,adi_soyadi TEXT,telefon TEXT ,mail TEXT,detay TEXT ,gun INT,ay INT, yil INT)")
        self.baglanti.commit()
    def ogrenci_int_veri(self):
        self.cursor.execute("select ogrenci_id from ogrenci ")
        liste = self.cursor.fetchall()
        return liste
    def tum_ogrenciler(self):
        self.cursor.execute("select * from ogrenci ")
        liste = self.cursor.fetchall()
        return liste
    def ogrenci_ekle(self,id,a,b,c,d,e,f,g):
        self.cursor.execute("insert into ogrenci Values(%s,%s,%s,%s,%s,%s,%s,%s)",(id,a,b,c,d,e,f,g))
        self.baglanti.commit()
    def ogrenci_goster(self):
        self.cursor.execute("select adi_soyadi,telefon,mail,ogrenci_id from ogrenci ")
        liste = self.cursor.fetchall()
        return liste
    def siniflar(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS siniflar (sinif_id INTEGER PRIMARY KEY ,sinif_adi TEXT, ucreti INT,basgun INT ,basay INT ,basyil INT ,bitgun INT,bitay INT ,bityil INT)")
        self.baglanti.commit()
    def sinif_ekle(self,a,b,c,d,e,f,g,k,id):
        self.isim = a + "_"+str(c)+"_"+str(d)
        self.cursor.execute("insert into siniflar Values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,self.isim,b,c,d,e,f,g,k))
        self.baglanti.commit()
        self.sinif_ekleme(self.isim)
    def guncelle_ogr(self,tutar ,odenen,ogrenci):
        self.cursor.execute("update ogrenci set detay = %s where adi_soyadi = %s AND  telefon = %s  ",(tutar ,odenen,ogrenci))
        self.baglanti.commit()
    def int_veri(self):
        self.cursor.execute("select sinif_id from siniflar ")
        liste = self.cursor.fetchall()
        return liste
    def sinif_ekleme(self,gelen):
        self.sorgu = "CREATE TABLE IF NOT EXISTS "+gelen+" (ogrenci_id INTEGER PRIMARY KEY ,ogrenci_adi TEXT,numara TEXT)"
        self.cursor.execute(self.sorgu)
        self.baglanti.commit()
    def sinif_bilgileri(self,gelen):
        c = "select * from "+gelen
        self.cursor.execute(c)
        liste = self.cursor.fetchall()
        return liste
    def taksitli_odemeler(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS taksitli (ogrenci_id INT,ogrenci TEXT,sinif TEXT,ucret_talebi INT ,odenen INT ,taksit1 INT,tarih1 DATE,taksit2 INT,tarih2 DATE,taksit3 INT,tarih3 DATE)")
        self.baglanti.commit()
    def taksit_ode(self,id,isim,sinif,ucret,odenen,s1,t1,s2,t2,s3,t3):
        self.cursor.execute("insert into taksitli Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,isim,sinif,ucret,odenen,s1,t1,s2,t2,s3,t3))
        self.baglanti.commit()
    def taksit_goster(self):
        self.cursor.execute("select * from taksitli")
        liste = self.cursor.fetchall()
        return liste
    def taksilat_al1(self ,tutar ,odenen,ogrenci,sinif,tarih):
        self.cursor.execute("update taksitli set taksit1 = %s ,odenen = %s where ogrenci = %s AND  (sinif = %s AND tarih1 = %s ) ",(tutar ,odenen,ogrenci,sinif,tarih))
        self.baglanti.commit()
    def taksilat_al2(self ,tutar ,odenen,ogrenci,sinif,tarih):
        self.cursor.execute("update taksitli set taksit2 = %s ,odenen = %s where ogrenci = %s AND  (sinif = %s AND tarih2 = %s ) ",(tutar ,odenen,ogrenci,sinif,tarih))
        self.baglanti.commit()
    def taksilat_al3(self ,tutar ,odenen,ogrenci,sinif,tarih):
        self.cursor.execute("update taksitli set taksit3 = %s ,odenen = %s where ogrenci = %s AND  (sinif = %s AND tarih3 = %s ) ",(tutar ,odenen,ogrenci,sinif,tarih))
        self.baglanti.commit()
    def siniflari_goster(self):
        self.cursor.execute("select sinif_id,sinif_adi,ucreti from siniflar")
        liste = self.cursor.fetchall()
        return liste
    def sinifa_ogrenci_ekle(self,sinif,id,isim,numara):
        self.cursor.execute("insert into "+sinif+ " Values(%s,%s,%s)",(id,isim,numara))
        self.baglanti.commit()
    def pesin_odemeler(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS pesin (ogrenci_id INT,ogrenci_adi TEXT,sinif_adi TEXT,alinan_pesin INT,tarih DATE)")
        self.baglanti.commit()
    def pesin_ode(self,id,isim,sinif,alinan,tarih):
        self.cursor.execute("insert into pesin Values(%s,%s,%s,%s,%s)",(id,isim,sinif,alinan,tarih))
        self.baglanti.commit()
    def pesin_goster(self):
        self.cursor.execute("select * from pesin")
        liste = self.cursor.fetchall()
        return liste
    def sertifika(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS setifikalar (ogrenci_id INT,ogrenci_adi TEXT,sinif TEXT,sertifika1 TEXT,sertifika2 TEXT,sertifika3 TEXT)")
        self.baglanti.commit()
    def sertifika_al(self,id,isim,sinif,s1,s2,s3):
        self.cursor.execute("insert into setifikalar Values(%s,%s,%s,%s,%s,%s)",(id,isim,sinif,s1,s2,s3 ))
        self.baglanti.commit()
    def sertifika_goster(self):
        self.cursor.execute("select * from setifikalar")
        liste = self.cursor.fetchall()
        return liste
    def neden_ekle(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS nedenler (neden TEXT ,ne TEXT)")
        self.baglanti.commit()
    def neden_ogrenci(self,ekle):
        self.cursor.execute("insert into nedenler Values(%s,%s)",(ekle ,"Selam"))
        self.baglanti.commit()
    def neden_listele(self):
        self.cursor.execute("select * from nedenler")
        liste = self.cursor.fetchall()
        return liste
    def neden_sil(self,yazar):
        self.cursor.execute("DELETE FROM nedenler WHERE neden = %s",(yazar,))
        self.baglanti.commit()
