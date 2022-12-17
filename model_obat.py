import os 
import random
from db import Database

class Obat: 
    
    def listAll():
        # bersihkan terminal agar tidak terlalu panjang
        os.system('cls')
        try:
            # ambil semua data obat dan tampilkan
            tabel = Database.read('obat')
            for i in tabel:
                print("---------" + i['nama'] + "---------")
                print("Kode Obat: " + str(i['id']))
                print("Stok: " + str(i['stok']))
                print("Harga: " + str(i['harga']))
                print("Jenis Penyakit: " + i['penyakit'])
                print("---------------------------")
                
        except Exception as e:
            print (e)
            print("Terjadi kesalahan pada sistem")
    
    def add():
        while True:
            os.system('cls')
            try:
                # input data obat
                nama = input("Nama Obat: ")
                stok = int(input("Stok: "))
                harga = int(input("Harga: "))
                penyakit = input("Jenis Penyakit: ")

                tabel = Database.read('obat')
                rand = random.randint(1, 10000)
                
                tabel.append({
                    'id': rand,
                    'penyakit': penyakit,
                    'nama': nama,
                    'stok': stok,
                    'harga': harga,
                })
                
                print ()
                print ("=====================================")
                print ("Nama Obat: " + nama)
                print ("Stok: " + str(stok))
                print ("Harga: " + str(harga))
                print ("Jenis Penyakit: " + penyakit)
                print ("=====================================")
                print ()
                
                if(input("Apakah data sudah benar? (y/n): ") != 'y'):
                    break
                
                Database.save('obat', tabel)
                print("Berhasil menambahkan obat")
                
                if(input("Tambah lagi? (y/n): ") != 'y'):
                    break
                
            except Exception as e:
                os.system('cls')
                print("Terjadi kesalahan pada sistem")
                if(input("Ulangi input? (y/n): ") != 'y'):
                    break 
            
    def deletes():
        # bersihkan terminal agar tidak terlalu panjang
        os.system('cls')
        try:
            tabel = Database.read('obat')
            Obat.listAll()
            kode = int(input("Masukkan kode obat yang ingin dihapus: "))
            tabel.pop(kode-1)
            Database.save('obat', tabel)
            print("Berhasil menghapus obat")
        except Exception as e:
            print("Obat tidak terhapus")
            