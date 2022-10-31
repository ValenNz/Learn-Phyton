# Episode input user

# data yang dimasukan pasti string
data = input("Masukan data: ")

print("data = ",data,",type =",type(data))

# jika kita ingin mengambil int, maka
angka = float(input("masukan angka: "))
angka = int(input("masukan angka: "))

print("data = ",angka,",type =",type(angka))

# bagaimana dengan boolean
biner = bool(int(input("masukan nilai boolean: ")))

print("data = ",biner,",type =",type(biner))





print("====================================")

print("=====STRING=====")
data = input ("Masukan nama :")
print("Nama :", data)
print("Nama ;", data,"type =",type(data))

print("=====INTEGER=====")
data = int(input ("Masukan absen :"))
print("Absen ;", data,"type =",type(data))

print("=====BOOLEAN TRUE=====")
data = bool(input ("Masukan Nilai a :"))
print("Nilai a :", data)
print("Nilai a ;", data,"type =",type(data))

print("=====BOOLEAN FALSE=====")
data = bool(int(input("Masukan nilai b :"))) # casting ke int terlebih dahulu baru akan menghasilkan false
print("Nilai b :", data) # nilai = 0 akan menghasilkan false
print("Nilai b ;", data,"type =",type(data))






