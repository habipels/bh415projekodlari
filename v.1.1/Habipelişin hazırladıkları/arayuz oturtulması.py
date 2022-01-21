class Neos_otomasyon(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_neos()
        self.ui.setupUi(self)
        self.giris()
        self.girisler = 0
        self.tablolar = tablo()
        self.tablolar.yonetici_tablosu()
        self.tablolar.ogrenci_tablosu()
        self.tablolar.siniflar()
        self.tablolar.pesin_odemeler()
        self.tablolar.taksitli_odemeler()
        self.tablolar.sertifika()
        self.tablolar.neden_ekle()
        self.ui.giris_buton.clicked.connect(self.goster)
        self.ui.egitim_kaydet.clicked.connect(self.sinif_ekleme)
        self.combobox_edit()
        self.ui.comboBox.activated['QString'].connect(self.combo)
        self.ui.kayit_et.clicked.connect(self.ogrenci_ekle)
        self.liste_goster()
        self.ui.listWidget.itemClicked.connect(self.tiklandi)
        self.ui.kayit_et_sinif.clicked.connect(self.kayit)
        self.ui.bul.clicked.connect(self.ogrenci_liste_goster)
        self.liste()
        self.mkc = self.ui.tableWidget.currentItem()
        print(self.mkc)
        self.ui.kayit_et_2.clicked.connect(self.elaman_ekle)
        self.listeleme()
        self.ui.listWidget_4.itemClicked.connect(self.silme)
        #self.ui.sebep_sil.clicked.connect(self.sil)
        self.taksit_goster()
        self.ui.arama.clicked.connect(self.odeme_ara)
        self.odenen = 0
        self.ui.odeme.clicked.connect(self.ode)
        self.taksit = 0
        self.odeme_al = 0
        self.ui.pushButton.clicked.connect(self.ciro)
        self.toplam = 0
        self.satis = 0
        self.comboboxlar()
        self.ui.excel_cikar.clicked.connect(self.sinif_excel)
        self.ui.kayitli_ogrenci_tablosu.clicked.connect(self.tum_ogrenci_excel)
        self.ui.silme.setText("ARA")
        self.ui.silme.clicked.connect(self.ogrenci_bilgi_goster)
        self.ui.guncelle.clicked.connect(self.guncel)
    def guncel(self):
        self.tablolar.guncelle_ogr(str(self.ui.not_arasi.toPlainText()),str(self.ui.adi_soyadi.text()),str(self.ui.telefon.text()))
        self.liste()
    def ogrenci_bilgi_goster(self):
        s = self.tablolar.tum_ogrenciler()
        m = self.ui.adi_soyadi.text()
        for i in range(len(s)):
            if m == s[i][1]:
                self.ui.kayit_tarihi.date().setDate(int(s[i][7]),int(s[i][6]),int(s[i][5]))
                self.ui.telefon.setText(str(s[i][2]))
                self.ui.mail_adrsi.setText(str(s[i][3]))
                self.ui.not_arasi.setText(str(s[i][4]))

    def tum_ogrenci_excel(self):
        pass   

    def sinif_excel(self):
        pass
    def sertifika_excel(self,u):
        pass  
    def pesin_excel(self):
        
        pass
    def comboboxlar(self):
        self.ui.comboBox_3.clear()
        c = self.tablolar.siniflari_goster()
        for i in c:
            self.ui.comboBox_3.addItem(i[1])
    def taksit_kalan_excel(self):
        pass
    def taksit_kalan_excel(self):
        pass
    def ciro(self):
        pass
    def taksilatlar(self,tarih1,tarih2):
        self.satis = 0
        self.toplam = 0
        odeme = self.tablolar.taksit_goster()
        print(odeme)
        tarih1 = str(tarih1).split(".")
        tarih2 = self.ui.cirobitis.text()
        tarih2 = str(tarih2).split(".")
        for i in range(len(odeme)):
            print(odeme[i][6])
            s = odeme[i][6] 
            s = str(s).split("-")
            print(s)
            if tarih1[0] <= s[0] and tarih1[2] == s[2] :
                if tarih1[1] <= s[1] :
                    if tarih2[0] >= s[0] and tarih2[2] >= s[2]:
                        print("selam")
                        if tarih2[1] >= s[1] and tarih2[2] >= s[2]: 
                            self.toplam = self.toplam + int(odeme[i][4])
                            self.satis = self.satis+int(odeme[i][5])+int(odeme[i][7])+int(odeme[i][9])
                    else:
                        if tarih2[1] >= s[1] and tarih2[2] >= s[2]: 
                            self.toplam = self.toplam + int(odeme[i][4])
                            self.satis = self.satis+int(odeme[i][5])+int(odeme[i][7])+int(odeme[i][9])
                        elif tarih2[2] > s[2]:
                            self.toplam = self.toplam + int(odeme[i][4])
                            self.satis = self.satis+int(odeme[i][5])+int(odeme[i][7])+int(odeme[i][9])
            elif tarih1[0] >= s[0] and tarih1[2] == s[2] :
                if tarih1[1] <= s[1] :
                    if tarih2[0] >= s[0] and tarih2[2] >= s[2]:
                        if tarih2[1] >= s[1]: 
                            self.toplam = self.toplam + int(odeme[i][4])
                            self.satis = self.satis+int(odeme[i][5])+int(odeme[i][7])+int(odeme[i][9])
                    else:
                        if tarih2[1] >= s[1] and tarih2[2] >= s[2]: 
                            self.toplam = self.toplam + int(odeme[i][4])
                            self.satis = self.satis+int(odeme[i][5])+int(odeme[i][7])+int(odeme[i][9])
                        elif tarih2[2] > s[2]:
                            self.toplam = self.toplam + int(odeme[i][4])
                            self.satis = self.satis+int(odeme[i][5])+int(odeme[i][7])+int(odeme[i][9])
            
    def ode (self):
        ogr = self.ui.adi_soyadi_2.text()
        sinif = self.ui.sinif.text()
        tutar = self.ui.odeme_tutari.text()
        try:
            self.odenen = self.odenen + int(tutar)
        except ValueError:
            self.ui.statusbar.showMessage("Taksit Kısmı Boş::))",3000)
            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
        tarih = self.ui.kayit_tarihi_2.text()
        if self.taksit == 1 and self.odeme_al == 1:
            self.tablolar.taksilat_al1(0,self.odenen,ogr,sinif,tarih)
            self.taksit_goster()
            self.odeme_al = 0
            self.ui.statusbar.showMessage("Ödeme Başarılı Hayırlı Olsun ::))",3000)
            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
        elif self.taksit == 2 and self.odeme_al == 1:
            self.tablolar.taksilat_al2(0,self.odenen,ogr,sinif,tarih)
            self.taksit_goster()
            self.odeme_al = 0
            self.ui.statusbar.showMessage("Ödeme Başarılı Hayırlı Olsun ::))",3000)
            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
        elif self.taksit == 3 and self.odeme_al == 1:
            self.tablolar.taksilat_al3(0,self.odenen,ogr,sinif,tarih)
            self.taksit_goster()
            self.odeme_al = 0
            self.ui.statusbar.showMessage("Ödeme Başarılı Hayırlı Olsun ::))",3000)
            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
        else:
            self.ui.statusbar.showMessage("Taksit bulunamadı ::))",3000)
            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
    def odeme_ara(self):
        adi = self.ui.adi_soyadi_2.text()
        ogr = self.tablolar.taksit_goster()
        print("Çalıitı")
        for i in range(len(ogr)):
            
            if adi == ogr[i][1] and ogr[i][2] == self.ui.sinif.text() :
                if ogr[i][5] != 0:
                    self.ui.odeme_tutari.setText(str(ogr[i][5]))
                    s = ogr[i][3] - ogr[i][4]
                    self.ui.label_42.setText(str(s))
                    self.odenen = ogr[i][4]
                    t = ogr[i][6]
                    t = str(t)
                    t = t.split("-")
                    tarih = QDate(int(t[2]),int(t[1]),int(t[0]))
                    self.ui.kayit_tarihi_2.setDate(tarih)
                    self.taksit = 1
                    self.odeme_al = 1
                    
                else:
                    if ogr[i][7] != 0:
                        self.ui.odeme_tutari.setText(str(ogr[i][7]))
                        s = ogr[i][3] - ogr[i][4]
                        self.ui.label_42.setText(str(s))
                        t = ogr[i][8]
                        self.odenen = ogr[i][4]
                        t = str(t)
                        t = t.split("-")
                        tarih = QDate(int(t[2]),int(t[1]),int(t[0]))
                        self.ui.kayit_tarihi_2.setDate(tarih)
                        self.taksit = 2
                        self.odeme_al = 1
                    else:
                        if ogr[i][9] != 0:
                            self.ui.odeme_tutari.setText(str(ogr[i][9]))
                            s = ogr[i][3] - ogr[i][4]
                            self.ui.label_42.setText(str(s))
                            t = ogr[i][10]
                            self.odenen = ogr[i][4]
                            t = str(t)
                            t = t.split("-")
                            tarih = QDate(int(t[2]),int(t[1]),int(t[0]))
                            self.ui.kayit_tarihi_2.setDate(tarih)
                            self.taksit = 3
                            self.odeme_al = 1
                        else:

                            self.odeme_al = 0
        
    def taksit_goster(self):
        ogr = self.tablolar.taksit_goster()
        print(len(ogr))
        self.ui.tableWidget_2.setRowCount(len(ogr))
        #self.ui.tableWidget.insertRow(len(ogr))
        for i in range(len(ogr)):
            for j in range(11):
                
                c = str(ogr[i][j])
                        
                self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(c))
                
    
    def silme(self):
        j =self.ui.listWidget_4.currentItem()
        u = self.tablolar.neden_listele()
        for i in u :
            if j.text() == i[0]:
                self.ui.kayit_olamama_nedeni.setText(j.text())
    def sil(self):
        self.tablolar.neden_sil(self.ui.kayit_olamama_nedeni.text)
        self.listeleme()
    def gel(self):
        print(self.mkc)
        print("Selam")
    def elaman_ekle(self):
        ekle = self.ui.kayit_olamama_nedeni.text()
        if ekle == "":
            pass
        else:
            self.tablolar.neden_ogrenci(ekle)
            self.listeleme()
    def listeleme(self):
        
        self.ui.listWidget_4.clear()
        
        u = self.tablolar.neden_listele()
        for i in u :
            self.ui.listWidget_4.addItem(i[0])
       

    def liste(self):
        ogr = self.tablolar.tum_ogrenciler()
        print(len(ogr))
        self.ui.tableWidget.setRowCount(len(ogr))
        #self.ui.tableWidget.insertRow(len(ogr))
        for i in range(len(ogr)):
            for j in range(6):
                if j == 5 :
                    c = str(ogr[i][5])+ "."+str(ogr[i][6])+"."+str(ogr[i][7])
                        
                    self.ui.tableWidget.setItem(i,j, QTableWidgetItem(c))
                else:
                    c = str(ogr[i][j])
                    self.ui.tableWidget.setItem(i,j, QTableWidgetItem(c))
    def sinif_kayit(self,sinif,id,isim,numara):
        self.tablolar.sinifa_ogrenci_ekle(sinif,id,isim,numara)
        self.ui.statusbar.showMessage("Kayıt Edildi ::))",3000)
        self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
    def pesin(self,id,isim,sinif,alinan,tarih):
        self.tablolar.pesin_ode(id,isim,sinif,alinan,tarih)
    def kayit(self):
        if self.ui.ogrenci_adi.text() != "Öğrenci Soyadı":
            if self.ui.label_19.text() != "Eğitim Seçmelisiniz !!!":
                u = self.ui.comboBox_2.currentIndex()
                y = self.ui.comboBox.currentText()
                print(y)
                print(u)
                if u == 1:
                    if self.ui.pesin.text() == "":
                        self.ui.statusbar.showMessage("Ücreti Doldurunuz ::))",3000)
                        self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")    
                    else:
                        try:
                            y = self.ui.comboBox.currentText()
                            k = int(self.ui.pesin.text())
                            self.sinif_kayit(y,self.id,self.isim,self.numara)
                            tarih = self.ui.dateEdit_3.text()
                            self.pesin(self.id,self.isim,y,k,tarih)
                            self.sertifika(self.id,self.isim,y)
                            
                            self.ui.statusbar.showMessage("Kayıt Başarılı ::))",3000)
                            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")  
                        except:
                            self.ui.statusbar.showMessage("Ücreti Yanlış Doldurunuz ::))",3000)
                            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                elif u == 0:
                    self.ui.statusbar.showMessage("Ödeme Yöntemini Doldurunuz ::))",3000)
                    self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                else:
                    try:
                        b = int(self.ui.onodeme.text())
                        
                        if self.ui.onodeme.text() != "":
                            s = self.ui.taksit_combo.currentIndex()
                            if s == 0 :
                                self.ui.statusbar.showMessage("Taksit Seçiniz ::))",3000)
                                self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                            elif s ==1:
                                try:
                                    b = int(self.ui.ilk_taksit.text())
                                    if self.ui.ilk_taksit.text() != "":
                                        y = self.ui.comboBox.currentText()
                                        ucret = int(self.ui.ucret.text())
                                        on_odeme = int(self.ui.onodeme.text())
                                        ilk_taksit = int(self.ui.ilk_taksit.text())
                                        tarih = self.ui.dateEdit_2.text()
                                        self.tablolar.taksit_ode(self.id,self.isim,y,ucret,on_odeme,ilk_taksit,tarih,0,tarih,0,tarih)
                                        self.sertifika(self.id,self.isim,y)
                                        self.ui.statusbar.showMessage("Kayıt Edildi  ::))",3000)
                                        self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                                    else:
                                        self.ui.statusbar.showMessage("Taksitleri Düzgün Doldurunuz ::))",3000)
                                        self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                                except ValueError:
                                    self.ui.statusbar.showMessage("Taksitleri Düzgün Doldurunuz ::))",3000)
                                    self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                                
                            elif s == 2:
                                try:
                                    b = int(self.ui.ilk_taksitt.text())
                                    a = int(self.ui.ilk_taksitt_2.text())
                                    if a == "" or b == "":
                                        
                                        self.ui.statusbar.showMessage("Taksitleri Düzgün Doldurunuz ::))",3000)
                                        self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                                    else:
                                        y = self.ui.comboBox.currentText()
                                        ucret = int(self.ui.ucret.text())
                                        on_odeme = int(self.ui.onodeme.text())
                                        t1 = self.ui.ilk_taksit_tarih.text()
                                        t2 = self.ui.ikinci_taksit_tarih.text()
                                        self.tablolar.taksit_ode(self.id,self.isim,y,ucret,on_odeme,b,t1,a,t2,0,t2)
                                        self.sertifika(self.id,self.isim,y)
                                        self.ui.statusbar.showMessage("Kayıt Edildi  ::))",3000)
                                        self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                                except ValueError:
                                    self.ui.statusbar.showMessage("Taksitleri Düzgün Doldurunuz ::))",3000)
                                    self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                                
                                
                            else:
                                try:
                                    a = int(self.ui.taksit_3_ilk.text())
                                    b = int(self.ui.taksit_3_ilk_2.text())
                                    c = int(self.ui.taksit_3_ilk_3.text())
                                    if a == "" or b == "" or c == "":
                                        self.ui.statusbar.showMessage("Taksitleri Düzgün Doldurunuz ::))",3000)
                                        self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                                    else:
                                        y = self.ui.comboBox.currentText()
                                        ucret = int(self.ui.ucret.text())
                                        on_odeme = int(self.ui.onodeme.text())
                                        t1 = self.ui.ilk_3_taksit.text()
                                        t2 = self.ui.ilk_3_taksit_2.text()
                                        t3 = self.ui.ilk_3_taksit_3.text()
                                        self.tablolar.taksit_ode(self.id,self.isim,y,ucret,on_odeme,a,t1,b,t2,c,t3)
                                        self.sertifika(self.id,self.isim,y)
                                        self.ui.statusbar.showMessage("Kayıt Edildi  ::))",3000)
                                        self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                                except ValueError:
                                    self.ui.statusbar.showMessage("Taksitleri Düzgün Doldurunuz ::))",3000)
                                    self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                                
                                
                        else:
                            self.ui.statusbar.showMessage("Ön Ödemeyi Doldurunuz ::))",3000)
                            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                    except ValueError:
                        self.ui.statusbar.showMessage("Ön Ödemeyi Doldurunuz ::))",3000)
                        self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
            else:
                self.ui.statusbar.showMessage("Sınıfı  Doldurunuz ::))",3000)
                self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")  
        else:
            self.ui.statusbar.showMessage("Öğrenci Seçin  ::))",3000)
            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
    def sertifika(self,ogrenci_id,ogrenci_adi,sinif):
        iccw = self.ui.checkBox.isChecked()
        katilim = self.ui.checkBox_2.isChecked()
        universite = self.ui.checkBox_3.isChecked()
        i = ""
        k = ""
        u = ""
        if iccw == 1:
            i = "ICCW"
        if katilim == 1:
            k = "KATILIM"
        if universite == 1:
            u = "ÜNİVERSİTE"
        self.tablolar.sertifika_al(ogrenci_id,ogrenci_adi,sinif,i,k,u)
            
    def tiklandi(self):
        j =self.ui.listWidget.currentItem()
        u = self.tablolar.ogrenci_goster()
        for i in u :
            if j.text() == i[0]:
                self.ui.label_16.setText(i[1])
                self.ui.label_18.setText(i[2]) 
                self.ui.ogrenci_adi.setText(j.text())
                self.id = i[3]
                self.isim = i[0]
                self.numara = i[1] 
                
    def liste_goster(self):
        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        u = self.tablolar.ogrenci_goster()
        for i in u :
            self.ui.listWidget.addItem(i[0])
        for i in u :
            self.ui.listWidget_2.addItem(i[1])
    def ogrenci_liste_goster(self):
        u = self.tablolar.ogrenci_goster()
        if self.ui.ogrenci_adi_2.text() != "":
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            for i in u:
                if self.ui.ogrenci_adi_2.text() == i[0]:
                    self.ui.listWidget.addItem(i[0])
                    self.ui.listWidget_2.addItem(i[1])
                
        else:
            self.liste_goster()
    def odeme_tablosu(self):
        if self.girisler == 1:
            self.ui.stackedWidget.setCurrentIndex(10)
    def combo(self):
        d = self.ui.comboBox.currentIndex()
        c = self.tablolar.siniflari_goster()
        m = c[d][2]
        self.ui.ucret.setText(str(m))    
    def giris(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def kayit_sayfasi(self):
        if self.girisler == 1:
            self.ui.stackedWidget.setCurrentIndex(1)
    def ogrenci_bilgileri_sayfasi(self):
        if self.girisler == 1:
            self.ui.stackedWidget.setCurrentIndex(2)
    def sinifa_ogrenci_ekle(self):
        if self.girisler == 1:    
            self.ui.stackedWidget.setCurrentIndex(3)
            
    def sinif_olustur(self):
        if self.girisler == 1:
            self.ui.stackedWidget.setCurrentIndex(4)
    def uye_olusturma(self):
        if self.girisler == 1:
            self.ui.stackedWidget.setCurrentIndex(6) 
    def ciro_tablosu(self):
        if self.girisler == 1:
            self.ui.stackedWidget.setCurrentIndex(8)
    def ogrenciler_tablosu(self):
        if self.girisler == 1:
            self.ui.stackedWidget.setCurrentIndex(9)
    def kayit_olmam_nedeni(self):
        if self.girisler == 1:
            self.ui.stackedWidget.setCurrentIndex(7)
    def tablo(self):
        if self.girisler == 1:
            self.ui.stackedWidget.setCurrentIndex(5)
    def goster(self):
        a = self.ui.kullanici_edit.text()
        b = self.ui.sifre_edit.text()
        liste = self.tablolar.yonetici_kontrol()
        for i in liste:
            if a == i[0] and b == i[1]:
                self.girisler = 1
                self.calistir()
                self.ui.statusbar.showMessage("Giriş Başarılı ::))",3000)
                self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                self.ui.kullanici_edit.setText("")
                self.ui.sifre_edit.setText("")
                self.kayit_sayfasi()

            else:
                self.ui.statusbar.showMessage("Kullanıcı Bulunamadı !!!",3000)
                self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
                self.ui.kullanici_edit.setText("")
                self.ui.sifre_edit.setText("")
    def sinif_ekleme(self):
        a = self.ui.sinif_adi.text()
        
        try:
            b = int(self.ui.egitim_tutari.text())
            c = self.ui.egitim_tarihi.date().day()
            d = self.ui.egitim_tarihi.date().month()
            e = self.ui.egitim_tarihi.date().year()
            f = self.ui.egitim_bitis_tarihi.date().day()
            g = self.ui.egitim_bitis_tarihi.date().month()
            k = self.ui.egitim_bitis_tarihi.date().year()
            id = self.tablolar.int_veri()
            buyuk = 0
            print(id)
            for i in id:
                if i[0] > buyuk:
                    buyuk = i[0]
            buyuk = buyuk + 1
            self.tablolar.sinif_ekle(a,b,c,d,e,f,g,k,buyuk)
            self.combobox_edit()
        except ValueError:
            self.ui.statusbar.showMessage("Düzgün Doldurunuz  !!!",3000)
            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
            self.ui.egitim_tutari.setText("")
    def ogrenci_ekle(self):
        id = self.tablolar.ogrenci_int_veri()
        buyuk = 0
        print(id)
        for i in id:
            if i[0] > buyuk:
                buyuk = i[0]
            buyuk = buyuk + 1
        a = self.ui.lineEdit.text() 
        b = self.ui.dateEdit.date().day()
        c = self.ui.dateEdit.date().month()
        d = self.ui.dateEdit.date().year()
        e = self.ui.lineEdit_3.text()
        f = self.ui.lineEdit_2.text()
        g = self.ui.not_adress_kayit.toPlainText()
        self.tablolar.ogrenci_ekle(buyuk,a,e,f,g,b,c,d)
        self.ui.statusbar.showMessage("Kayıt  Başarılı ::))",3000)
        self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
        self.liste_goster()    
    def combobox_edit(self):
        self.ui.comboBox.clear()
        c = self.tablolar.siniflari_goster()
        for i in c:
            self.ui.comboBox.addItem(i[1])
        

    def cik(self):
        self.girisler = 0
        self.ui.statusbar.showMessage("Çıkış Başarılı ::))",3000)
        self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
        self.giris()
    def calistir(self):
        if self.girisler == 1: 
            self.ui.action_k.triggered.connect(self.cik)
            self.ui.action_renci_Kaydet.triggered.connect(self.kayit_sayfasi)
            self.ui.action_renci_Bilgileri.triggered.connect(self.ogrenci_bilgileri_sayfasi)
            self.ui.actionS_n_fa_renci_Ekle.triggered.connect(self.sinifa_ogrenci_ekle)
            self.ui.actionS_n_f_Olu_tur.triggered.connect(self.sinif_olustur)
            self.ui.actionNeos_Yaz_l_m_ye_olu_tur.triggered.connect(self.uye_olusturma)
            self.ui.actionCiro_Tablosu.triggered.connect(self.ciro_tablosu)
            self.ui.actionDurum_Tablosu.triggered.connect(self.ogrenciler_tablosu)
            self.ui.actionKay_t_Olamama_Nedenleri.triggered.connect(self.kayit_olmam_nedeni)
            self.ui.kayit_ol.clicked.connect(self.uye_kayit)
            self.ui.actionExcel_Tablosu.triggered.connect(self.tablo)
            self.ui.action_deme_Al.triggered.connect(self.odeme_tablosu)
        
    def uye_kayit(self):

        if self.ui.parola.text() == self.ui.parola_2.text():
            self.tablolar.yonetici_ekle(self.ui.parola.text(),self.ui.parola_2.text())
            self.ui.statusbar.showMessage("Kayıt Oldunu ;=}",3000)
            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
            self.ui.parola.setText("")
            self.ui.parola_2.setText("")
            self.ui.kullanici_adi.setText("")
            
            
        else: 
            self.ui.statusbar.showMessage("Şifreler Uyuşmuyor !!!",3000)
            self.ui.statusbar.setStyleSheet("color: rgb(0, 0, 0); font-weight:bold;")
            self.ui.parola.setText("")
            self.ui.parola_2.setText("")
            self.goster()

app = QApplication([])
window =Neos_otomasyon()
window.show()
app.exec_()
