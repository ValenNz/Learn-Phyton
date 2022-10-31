## List
Ganjil = [1,3,5,7,9]
 #data bisa dirubah

## Tuple
 # data tdk dapat dirubah,ditambah.dikurang dll
 # fungsi nya supaya data tdk dapat dirubah cth data penduduk, dll
Genap = (2,4,6,6,8,10)

print(type(Ganjil))
print(type(Genap))

Ganjil  [2] = 99 
# Genap (2) = 99 # akan error

print(Genap)
print(Ganjil)

print("===== ACT =====")
# untuk mengetahui apa saja yang bisa dilakukan tipe data dibawah ini
Genap = (2,4,6,6,8,10)

print(type(Ganjil))
print(type(Genap))

Ganjil  [2] = 99 
# Genap (2) = 99 # akan error

print(dir(Genap))
print(dir(Ganjil))

## Mengetahui besaran data yang digunakan lebih besar mana....(memori)
print("===== MEMORY =====")
import sys

data_list = [1,2,3,4,5,6,7,8,9,10,"pisang goreng","syahrini","via vallen", False, 3.14]
data_tuple = (1,2,3,4,5,6,7,8,9,10,"pisang goreng","syahrini","via vallen", False, 3.14)

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)

print("besar data list:", besar_datalist)
print("besar data tuple:", besar_datatuple)


## Mengetahui waktu untuk mengeneret lebih cepat mana... (waktu)
print("===== WAKTU =====")
import timeit

data_list = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000)

print("waktu untuk memproses list:",data_list)
print("waktu untuk memproses tuple:",data_tuple)




