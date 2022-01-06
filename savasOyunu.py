from abc import ABC, abstractmethod
class Karakter:
    
    def __init__(self):
        self.name = ""
        self.job = ""
        self.level = 1
        self.gerekliExp = 0
        self.suankiExp = 0
        self.exp = 0
        self.healt = 0
        self.energy = 0
        self.power = 0
        self.deffense = 0
    def gerekliTecrube(self):
        if self.level==1:
            gerekliExp = 100 - self.suankiExp
        elif self.level==2:
            gerekliExp = 300 - self.suankiExp
        elif self.level==3:
            gerekliExp = 540 - self.suankiExp
        elif self.level==4:
            gerekliExp = 720 - self.suankiExp
        elif self.level==5:
            gerekliExp = 1000 - self.suankiExp
        else:
            print("Son levelsiniz.")
    def yetenekVer(self):
        yetenek_menu = True
        if yetenek_menu:
            print("""
                  Tebrikler level atladınız.
                  Şuanki Leveliniz : {} ve Tecrübeniz: {}
                  Geliştirmek istediğiniz özelliği seçiniz.
                  1) Healt (50 HP)
                  2) Energy (1 Energy)
                  3) Power (1 Power)
                  4) Deffense (1 Deffense)
                  """.format(self.level,self.exp))
            yetenek_menu = False
            seçim = input("Seçiminiz hangisi? : ")
            if seçim =="1":
                self.healt += 50
            elif seçim =="2":
                self.energy += 1
            elif seçim =="3":
                self.power += 1
            elif seçim =="4":
                self.deffense +=1
            else:
                print("Yanlış tuşladınız. Lütfen tekrar deneyin.")
                yetenek_menu = True
        
    def expVer(self,gelen_tecrube):
        if self.suankiExp + gelen_tecrube >= self.gerekliExp:
            artan_tecrube = (self.suankiExp + gelen_tecrube) % self.gerekliExp
            self.level+=1
            self.suankiExp = artan_tecrube
            self.yetenekVer()
        elif self.suankiExp + gelen_tecrube < self.gerekliExp:
            self.suankiExp = self.suankiExp + gelen_tecrube
            print("Tecrübeniz yükseldi. Şuanki tecrübeniz: {}".format(self.suankiExp))
    def expDusur(self,giden_tecrube):
        if self.suankiExp > 0:
            self.suankiExp = self.suankiExp - giden_tecrube
            if self.suankiExp < 0:
                self.suankiExp = 0
            print("Tecrübe kaybettiniz. Şuanki tecrübeniz: {}".format(self.suankiExp))
    def bilgiVer(self):
        print("""
              ***********************************************************************
              ************************Karakter Bilgilerin****************************
              Karakter İsmi: {}
              Karakter Sınıfı: {}
              Karakter Leveli: {}
              Karakter Tecrübesi: {}
              Level Atlamak İçin Gerekli Tecrübe: {}
              Healt: {} , Energy: {} , Power: {} , Deffense: {}
              ***********************************************************************
              """.format(self.name,self.job,self.level,self.suankiExp,self.gerekliExp,self.healt,self.energy,self.power,self.deffense))
              
    @abstractmethod
    def atakYap(self):
        pass
    @abstractmethod
    def karakterYarat(self):
        pass
class Savasci(Karakter):

    def __init__(self):
        super().__init__()
        
    def atakYap(self):
        print("Savaşçı Atak Yaptı.")
        
    def karakterYarat(self):
        self.job = "Savaşçı"
        self.healt = 200
        self.energy = 10
        self.power = 14
        self.deffense = 12

class Ninja(Karakter):
    def __init__(self):
        super().__init__()
    def atakYap(self):
        print("Ninja Atak Yaptı.")
    def karakterYarat(self):
        self.job = "Ninja"
        self.healt = 180
        self.energy = 14
        self.power = 13
        self.deffense = 10
        
class Büyücü(Karakter):
    def __init__(self):
        super().__init__()
    def atakYap(self):
        print("Büyücü Atak Yaptı.")
    def karakterYarat(self):
        self.job = "Büyücü"
        self.healt = 190
        self.energy = 16
        self.power = 12
        self.deffense = 11
class Canavar:
    def __init__(self,name,level,healt,energy,power,deffense,give_exp):
        self.name = name
        self.level = level
        self.healt = healt
        self.energy = energy
        self.power = power
        self.deffense = deffense
        self.give_exp = give_exp
        canavar1 = None
        canavar2 = None
    def canavarOlustur(self):
        canavarlistesi = []
        self.canavar1 = Canavar("Yabani Köpek",1,100,2,5,3,50)
        self.canavar2 = Canavar("Aç Kurt",2,130,3,6,4,80)
        canavarlistesi.append(self.canavar1)
        canavarlistesi.append(self.canavar2)
    
main_menu = True
karakter_menu = True
canavar_menu = True
while True:
    if main_menu:
        print("""
              Merhaba kudretli topraklara hoşgeldin. 
              Burada esrarengiz olaylar ve büyük savaşlar olmakta.
              Heran herşeye hazırlıklı olmanı dilerim.
              """)
        main_menu = False
        seçim = input("Oyuna başlamak için B, Çıkış yapmak için Q harflerini giriniz. : ")
    if seçim == "B" or seçim == "b":
        print("""
              Seni gözüm tuttu savaştan korkup kaçacak biri değilsin.
              Hadi onlara gününü göster.
              """)
        if karakter_menu:
            print("""
                  ***** Karakter Menüsü
                  1) Savaşçı
                  2) Ninja
                  3) Büyücü
                  Q) Çıkış
                  """)
            karakter_menu = False
            
            seçim = input("Seçimini Yap: ")
            if seçim == "1":
                karakterismi = input("Karakter isminizi giriniz: ")
                karakter = Savasci()
                karakter.name = karakterismi
                print("Karakter isminiz: {}".format(karakter.name))
                karakter.karakterYarat()
                karakter.bilgiVer()
                if canavar_menu:
                    Canavar.self.canavarOlustur()
                    print("""
                          ***************************Savaş Menüsü********************************
                          {} Adet Canavar Bulunmakta.
                          1) """+Canavar.canavar1.name+"""+" "+"""+Canavar.canavar1.level+"""+" "+"""+Canavar.canavar1.healt+"""
                          2) """+Canavar.canavar2.name+"""+" "+"""+Canavar.canavar2.level+"""+" "+"""+Canavar.canavar2.healt+"""
                         """)
                    savas_menusu = False
                    seçim = input("Canavar numarasını giriniz: ")
                    if seçim == "1":
                        if karakter.power > karakter.canavar1.power:
                            karakter.expVer(karakter.canavar1.give_exp)
                        else:
                            karakter.expDusur(100)
                    elif seçim == "2":
                        if karakter.power > karakter.canavar2.power:
                            karakter.expVer(karakter.canavar2.give_exp)
                        else:
                            karakter.expDusur(100)
                    else:
                        print("Yanlış canavar tuşladınız.")
                        savas_menusu = True
                        break
                
            elif seçim == "2":
                karakterismi = input("Karakter isminizi giriniz: ")
                karakter = Ninja()
                karakter.name = karakterismi
                print("Karakter isminiz: {}".format(karakter.name))
                karakter.karakterYarat()
                break
            
            elif seçim == "3":
                karakterismi = input("Karakter isminizi giriniz: ")
                karakter = Büyücü()
                karakter.name = karakterismi
                print("Karakter isminiz: {}".format(karakter.name))
                karakter.karakterYarat()
                break
            
            elif seçim == "Q" or seçim == "q":
                break
            
            else:
                print("Sanırım seçenekleri yanlış anladınız. Tekrar deneyin.")
                karakter_menu = True
    elif seçim == "Q" or seçim == "q":
        break
    else:
        print("Sanırım seçenekleri yanlış anladınız. Tekrar deneyin.")
        main_menu = True
        karakter_menu = False
            
        
        
        