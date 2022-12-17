import os 
from model_obat import Obat
import autoload

class Dokter: 
    
    def __init__(self):
        Dokter.menu(self)
        
    def menu(self):
        os.system('cls')
        print ("=====================================")
        print ("Menu Dokter")
        print ("=====================================")
        print ("0. Keluar")
        print ("1. Lihat Stok Obat")
        print ("2. Tambah Obat")
        print ("3. Hapus Obat")
        print ("=====================================")
        Dokter.pilihan(self)
            
    def pilihan(self):
        while True:
            pilihan = input("Masukkan Pilihan Menu: ")
        
            if pilihan == "1":
                self.list_data_obat()
            elif pilihan == "2":
                self.tambah_obat()
            elif pilihan == "3":
                self.hapus_obat()
            elif pilihan == "0":
                os.system('cls')
                autoload.init()
            else :
                print ("menu tidak ditemukan")
                print ("0. Keluar")
                print ("1. Lihat Stok Obat")
                print ("2. Tambah Obat")
                print ("3. Hapus Obat")

    def list_data_obat(self):
        os.system('cls')
        print ("=====================================")
        print ("Stok Obat")
        print ("=====================================")
        
        Obat.listAll()
        
    def tambah_obat(self):
        os.system('cls')
        print ("=====================================")
        print ("Tambah Obat")
        print ("=====================================")
        
        Obat.add()
        
    def hapus_obat(self):
        os.system('cls')
        print ("=====================================")
        print ("Hapus Obat")
        print ("=====================================")
        
        Obat.deletes()