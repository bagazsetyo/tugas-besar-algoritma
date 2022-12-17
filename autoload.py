from db import Database
from view_dokter import Dokter
from view_pasien import Pasien

def init():
    print ("=====================================")
    print ("Selamat Datang di Apotek Lekas Sembuh")
    print ("=====================================")
    print ()
    print ()
    
    tipe_masuk = input("Masuk sebagai (dokter/pasien): ")
    
    
    if(tipe_masuk == "dokter"):
        dokter = Dokter()
    else:
        pasien = Pasien()