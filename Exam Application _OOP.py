import random as rd


class sınav:
    def __init__(self,sınavAdı,sınavıÇözenKişi):
        self.sınavAdı = sınavAdı
        self.sınavıÇözenKişi = sınavıÇözenKişi
        self.status = True
        self.puan = 0
        self.dogrular = []
        
    def run(self):
        self.soru1()
        self.sınavSonuc()
    
    def soru1(self):
        sıklar = [64,45,78,15,56]
        
        while True:
            rd.shuffle(sıklar)
            sorustr = "1-ahmet kaç yaşınadır ?\nA-{}\nB-{}\nC-{}\nD-{}\nE-{} \ncevap :".format(sıklar[0],sıklar[1],sıklar[2],sıklar[3],sıklar[4])
            seçim = input(sorustr)
            seçim = seçim.lower()
            
            if seçim=="a" or  seçim=="b" or seçim=="c" or seçim=="d" or seçim=="e":
                break
            print("lüften a-e arasında bir değer giriniz")
            continue
        
        
        dogruSık = sıklar.index(56)
        cevap = ""
        
        
        if dogruSık == 0:
            cevap = "a"
        if dogruSık == 1:
            cevap = "b"
        if dogruSık == 2:
            cevap = "c"
        if dogruSık == 3:
            cevap = "d"
        if dogruSık == 4:
            cevap = "e"
            
        if seçim == cevap:
            self.dogrular.append(1)
            self.puan+=10
            
    def sınavSonuc(self):
        print("puan : {} \n doğrular {}".format(self.puan,self.dogrular))
    





s1 = sınav("ÖSYM","Ahmet")
while s1.status:
   s1.run()
   s1.status = False


        