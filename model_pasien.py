import os 
import random
from db import Database

class PasienApotek: 
    
    def keluhan():
        os.system('cls')
        print ("=====================================")
        print ("Keluhan")
        print ("=====================================")
        print ()
        
        arr_keluhan = []
        while True:
            keluhan = input("Masukkan keluhan: ")
            arr_keluhan.append(keluhan)
            
            if(input("Apakah sudah selesai? (y/n): ") == 'y'):
                os.system('cls')
                break
        
        db = Database.read('obat')
        id_obat = []
        for i in db:
            for j in arr_keluhan:
                try:
                    if (i['penyakit'] == j):
                        print ("Kode Obat: " + str(i['id']))
                        print ("Penyakit: " + i['penyakit'])
                        print ("Obat: " + i['nama'])
                        print ("Stok: " + str(i['stok']))
                        print ("Harga: " + str(i['harga']))
                        print ("=====================================")
                        
                        id_obat.append(i['id'])
                except: 
                    print ()
            
        beli = input('Beli Obat? (y/n): ')
        if (beli == 'y'):
            PasienApotek().beli_obat(id_obat)
                    
    def beli_obat(self, idobat = []):
        print ("=====================================")
        print ("Beli Obat")
        print ("=====================================")
        print ()
        
        print ()
        if(len(idobat) > 1):
            print ('Kode obat penyakit anda: ')
            print (', '.join(str(x) for x in idobat))
            
        print ("masukkan kode obat: ")
        list_kode_obat = []
        db = Database.read('obat')
        while True:
            kode_obat = input("Kode Obat: ")
            for i in db:
                if (str(i['id']) == kode_obat):
                    qty = int(input("Masukkan jumlah obat: "))
                    list_kode_obat.append({
                        'kode_obat': kode_obat,
                        'qty': qty,
                        'nama': i['nama'],
                        'harga': i['harga']
                    })
                    
            if(input("Apakah anda ingin membeli lagi? (y/n): ") == 'n'):
                os.system('cls')
                break
            
        PasienApotek().bayar(list_kode_obat)
            
    def bayar(self, barang):
        print ("=====================================")
        print ("Bayar")
        print ("=====================================")
        print ()
        
        total_bayar = 0
        
        for i in barang:
            total_bayar += i['harga'] * i['qty']
        
        # make number format 
        formatHarga = "{:,}".format(total_bayar) 
        print ("Total Bayar: " + formatHarga)
        print ()
        
        harga_bayar = int(input("Masukkan harga bayar: "))
        print ()
        
        print ("=====================================")
        hasil_akhir = harga_bayar - total_bayar
        while hasil_akhir < 0:
            hasil_akhir_format = "{:,}".format(hasil_akhir)
            print ("Uang tidak cukup", hasil_akhir_format)
            harga_bayar = int(input("Masukkan harga bayar: "))
            hasil_akhir = harga_bayar - total_bayar
            print ()
            
        for j in barang:
            db = Database.read('obat')
            for i in db:
                if (i['id'] == int(j['kode_obat'])):
                    i['stok'] -= j['qty']
                    db = Database.save('obat', db)
                    
            
        # create invoice on database transaksi 
        db = Database.read('transaksi')
        id = random.randint(1, 100000)
        db.append({
            'id': id,
            'barang': barang,
            'harga_bayar': harga_bayar,
        })
        Database.save('transaksi', db)
        
        os.system('cls')
        
        print ("=====================================")
        print ("Invoice")
        print ("=====================================")
        
        for i in barang:
            print ("Nama Obat: " + i['nama'])
            print ("Harga: " + str(i['harga']))
            print ("Jumlah: " + str(i['qty']))
            print ("=====================================")

        print ()
        print ("Total " + formatHarga)
        print ("Bayar: " + str(harga_bayar))
        print ("=====================================")
        formatKembalian = "{:,}".format(hasil_akhir)
        print ("Kembalian: " + str(formatKembalian))
        
        print ("Terima kasih telah berbelanja di apotek kami")
        print ("Semoga lekas sembuh")
        