## IMPORT DASAR
  # untuk multifile / untuk mengakses beberapa file

# cara memanggil dari file lain 
print("===== MODUL =====")
import modul

# cara memanggil sebuah variable
print("===== VARIABLE =====")
print(modul.data)

# cara memanggil sebuah fungsi 
print("===== FUNGSI =====")
modul.cek_modul()



## CARA MENGAKSES IMPORT MENGGUNAKAN FUNGSI
print("+++++++++++++++++++++++++ ACCES FUNGSI ++++++++++++++++++++++++++++++++")

#  Mengimport file matematika
print("===== IMPORT FILE MATH =====") # 1
import matematika

matematika.tambah(3,4)
matematika.kurang(4,5)

print("===== IMPORT FILE MATH =====") # 2
import matematika as math

math.tambah(3,4)
math.kurang(5,4)

# Mengimport hanya spesifikasinya
print("===== IMPORT FILE MATH =====") # 3

from matematika import tambah, kurang # bisa mengambil fungsi kurang
from matematika import * # untuk mengambil semuanya

tambah(4,5)
kurang(5,4)

print("===== IMPORT FILE MATH =====") # 3
from matematika import tambah as t

t(3,4)



## PACKAGES
  # Kumpulan dari beberapa modul
print("++++++++++++++++++++++++++++++++++++++ PACKAGES ++++++++++++++++++")

#import fisika
#import matematika

#kecepatan = fisika.kecepatan(50,10)
#print(kecepatan)

# mengakses dari file
from sains import fisika,matematika

fisika.kecepatan(3,4)
matematika.tambah(4,5)