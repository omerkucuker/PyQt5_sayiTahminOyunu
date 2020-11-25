from PyQt5.QtWidgets import*
from design import Ui_MainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import random

class sayiTahmin    (QMainWindow):
    pc_sayi = random.randint(1, 100)
    flag = False
    kalan_hak = 2
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(":\num.ico"))
        self.ui.txt_kalanhak.setText(str(self.kalan_hak + 1))
        self.ui.txt_tahmin.returnPressed.connect(self.tahminet)
        self.ui.btn_yenioyun.clicked.connect(self.yeniOyun)
        self.ui.btn_cikis.clicked.connect(self.cikma)
        
        
    def cikma(self):
        app.exit()

    def yeniOyun(self):
        
        self.kalan_hak=5
        self.flag=False
        self.ui.txt_sonuc.setText("Yeni Oyun Başladı")
        self.ui.txt_tahmin.setText("")
        self.ui.txt_kalanhak.setText(str(self.kalan_hak + 1))
        self.pc_sayi = random.randint(1, 100)

    def tahminet(self):
        

        try:
            girilenSayi = int(self.ui.txt_tahmin.text())
            if self.pc_sayi == int(girilenSayi):
                self.ui.txt_sonuc.setText("Tebrikler doğru bildiniz.. " + str(self.pc_sayi))
                self.flag = True
                self.ui.txt_tahmin.setText("")

                #self.yeniOyun()

            elif self.kalan_hak == 0:
                self.ui.txt_sonuc.setText(
                    "Son hakkında da bilemedin ve hakkın bitti.. Başka bir oyunda tekrar deneyin. \n Doğru sayi: " + str(
                        self.pc_sayi))
                self.ui.txt_tahmin.setText("")
                self.ui.txt_kalanhak.setText(str(self.kalan_hak))


            elif int(girilenSayi) > self.pc_sayi:
                self.ui.txt_sonuc.setText(
                    "Tekrar Deneyin.. İpucu: Daha küçük sayi girin.. ")
                # Kalan hakkınız: " + str(self.kalan_hak))
                self.kalan_hak -= 1
                self.ui.txt_kalanhak.setText(str(self.kalan_hak + 1))
                self.ui.txt_tahmin.setText("")

            else:
                self.ui.txt_sonuc.setText(
                    "Tekrar Deneyin.. İpucu: Daha büyük bir sayi girin..")
                # Kalan hakkınız: " + str(self.kalan_hak))
                self.kalan_hak -= 1
                self.ui.txt_kalanhak.setText(str(self.kalan_hak + 1))
                self.ui.txt_tahmin.setText("")
        except ValueError:
            self.ui.txt_sonuc.setText("Sayi giriniz..")




app=QApplication([])
window=sayiTahmin()
window.show()
app.exec_()
