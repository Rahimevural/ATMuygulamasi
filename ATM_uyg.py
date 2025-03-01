class Musteri:
    def __init__(self,ad,soyad,kartsifre,hesapbakiye,kredikartborc,sonodeme):
        self.ad = ad
        self.soyad = soyad
        self.kartsifre = kartsifre
        self.hesapbakiye = hesapbakiye
        self.kredikartborc = kredikartborc
        self.sonodeme = sonodeme

Ahmethesap = Musteri("Ahmet","Candan","1357",5000,4200,"20/11/2025")   
Mehmethesap = Musteri("Mehmet","Duyar","2468",6000,3800,"28/11/2025")      
Takilankart = Ahmethesap


class ATM:
    def __init__(self,atmad):
        self.atmad = atmad
        self.giriskontrol()
        self.dongu = True

    def giriskontrol(self):
        Hak =2
        for i in range(0,3):
            sifre = input("Lütfen 4 Haneli Sifrenizi Giriniz:")
            if sifre == Takilankart.kartsifre:
                self.program()
            elif sifre != Takilankart.kartsifre and Hak!=0:
                 print("Hatalı şifre girdiniz.Kalan Hakkınız{}".format(Hak))  
                 Hak-=1
            elif sifre != Takilankart.kartsifre and Hak==0:
                print("Şifrenizi 3 defa hatalı girdiğiniz için kartınız bloke olmuştur.Lütfen en yakın şubemize başvurunuz !") 
                exit()     

    def program(self):
        secim = self.menu()
        if secim ==1:
            self.bakiye()
        if secim==2:
            self.kkborc()
        if secim ==3:
            self.paracek()
        if secim ==4:
            self.parayatir()
        if secim ==5:
            self.cıkıs()



    def menu(self):
        secim = int(input("*** Merhabalar ,{} 'a hoşgerldiniz .Sayın{}{}.\n\nLütfen yapmak istediğiniz işlemi seçiniz...\n\n[1] Bakiye Sorgulama\n[2] Kredi Kartı Borç Sorgulama\n[3]Para Çekme\n[4]Para Yatırma\n[5] Kart İade\n\n Seçim : ".format(self.atmad,Takilankart.ad,Takilankart.soyad)))   
        while secim<1 or secim>5:
            print("\n\nLütfen 1 ve 5 arasında geçerli bir değer giriniz...\nAna Menüye Dönülüyor...")
            self.program()
        return secim     



    def bakiye(self):
        print("Hesap Bakiyeniz : {} TL'dir.".format(Takilankart.hesapbakiye))
        self.dongu = False
        self.menudon()

    def kkborc(self):
        print("kredi kartı borcunuz {} son ödeme tarihli {} TL 'dir.".format(Takilankart.sonodeme,Takilankart.kredikartborc))
        self.dongu = False
        self.menudon()

    def paracek(self):
        miktar = int(input("lütfen çekeceğiniz tutarı giriniz:..."))
        Yenimiktar=Takilankart.hesapbakiye-miktar
        if miktar>Takilankart.hesapbakiye:
            print("yetersiz bakiye")
            self.menudon()
        else:
            print("lütfen paranızı sayarak alınız.Hesabınızda kalan tutar {} TL'dir.".format(Yenimiktar))
            self.menudon()    

    def parayatir(self):
        miktar2 = int(input("lütfen yatırılacak tutarı giriniz:..."))
        Yenimiktar2=Takilankart.hesapbakiye+miktar2
        print("Para yatırma işlemi başarıyla gerçekleşmiştir. Hesabınızın yeni bakiyesi {} TL'dir.".format(Yenimiktar2))
        self.menudon()

    def cıkıs(self):
        print("Bankamızı tercih ettiğiniz için tesekkür eder,iyi günler dileriz...")
        self.dongu=False
        exit()

    def menudon(self):
        x=int(input("Ana Menüye Dönmek İçin Lütfen 7 Tuşuna Basınız.Kart İade İçin 5'e Basınız..."))
        if x==7:
            self.program()
        elif x==5:
            self.cıkıs()    

Banka = ATM("XBank")
while Banka.dongu:
    Banka.program()    

