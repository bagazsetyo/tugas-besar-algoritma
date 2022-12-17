import os 
from model_obat import Obat
from model_pasien import PasienApotek

class Pasien: 
    
    def __init__(self):
        Pasien.menu(self)
        
    def menu(self):
        os.system('cls')
        print ("=====================================")
        print ("Menu Pasien")
        print ("=====================================")
        print ("0. Keluar")
        print ("1. Lihat Stok Obat")
        print ("2. Keluhan")
        print ("3. Beli Obat")
        print ("=====================================")
        Pasien.pilihan(self)
            
    def pilihan(self):
        while True:
            pilihan = input("Masukkan Pilihan Menu: ")
        
            if pilihan == "1":
                self.list_data_obat()
            elif pilihan == "2":
                self.keluhan()
            elif pilihan == "3":
                self.beli_obat()
            elif pilihan == "0":
                break
            else :
                print ("menu tidak ditemukan")
                print ("0. Keluar")
                print ("1. Lihat Stok Obat")
                print ("2. Keluhan")
                print ("3. Beli Obat")

    def list_data_obat(self):
        os.system('cls')
        print ("=====================================")
        print ("Stok Obat")
        print ("=====================================")
        
        Obat.listAll()
        
    def keluhan(self):
        os.system('cls')
        print ("=====================================")
        print ("Keluhan")
        print ("=====================================")
        
        PasienApotek.keluhan()
        
    def beli_obat(self):
        os.system('cls')
        print ("=====================================")
        print ("Beli Obat")
        print ("=====================================")
        
        
        PasienApotek.beli_obat()