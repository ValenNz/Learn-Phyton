# ## LIST

# print("++++++++++++++++++++++ LIST +++++++++++++++++++++++++++++")
data = [1,4,9,16,25,36,49,64]
#   # Data = [0,1,2,3,4,5,6,7,8]

# MENGAKSES LIST
print("\n==== ACCES ====")
subdata_1 = data [3] # mengambil dari depan (1 = 0, 4 = 1)
print(subdata_1)
subdata_2 = data [-3] # mengmabil dari belakang
print(subdata_2)

# # MEMOTONG LIST
# print("\n==== CUT ====")
# subdata_3 = data [0:4] # mengmabil dari (0,1,2,3) mengambil 0 sampai sebelum 4
# print(subdata_3)
# subdata_4 = data [2:4] # mengmabil dari (0,1,2,3) mengambil 0 sampai sebelum 4
# print(subdata_4)
# subdata_5 = data [4:] # mengmabil dari belakang (8,7,6,5)
# print(subdata_5)
# subdata_7 = data [-4:] # mengmabil dari belakang (8,7,6,5)
# print(subdata_7)
# subdata_6 = data [:4] # mengmabil dari depan (0,1,2,3)
# print(subdata_6)

# # MENAMBAH LIST
# print("\n==== ADD ====")
# data2 =[100,200,300,400,500,600,700,800,]
# data3 = data + data2
# print(data3)

# # MERUBAH CONTENT DARI LIST
# print("\n==== CHANGE CONTENT ====")
# data[4] = 45
# print(data)

# # MENGCOPY LIST KE VARIABLE BARU
# print("\n==== COPY TO VARIABLE ====")
# a = data[:]
# a[7] = 45

# # METODE SLICING 
#     # merubah content list 
# print("\n==== SLICING ====")
# data[3:5] = [11,12]
# print(data)

# # LIST DIDALAM LIST
# print("\n==== LIST IN LIST ====")
# x = [data,data2]
# print(x)

# # MENGAKSES LIST DALAM MULTIDIMENSIONAL LIST
# print("\n==== ACC LIST MULTIDIMENSIONAL ====")
# y = x[1][4]
# print(x)
# print(y)

# # METHODS UNTUK LIST
# print("\n==== METHODS ====")
# data.append(30) # append menambah list(member)
# print(data)

# # FUNCTION LIST 
# print("\n==== FUNCTION ====")
# panjang_list = len(data) # menghitung jumlah (member) data
# print(data)
# print(panjang_list)


Barang = ['kunci','ember','jaket','ban','mobil']
print(Barang)

# method untuk menambah data kedalam list
print("===== APPEND =====") # menambah di belakang
Barang.append('sepeda')
print(Barang)

print("===== extend =====") # mengeja data
Barang.extend('dompet')
print(Barang)

print("===== INSERT =====")
Barang.insert(3,'sepeda') # menambahkan ditengah
print(Barang)

# method untuk menghitung anggota
print("===== REMOVE =====")
jumlahSepeda = Barang.count('sepeda') 
print("Jumlah sepeda adalah: ",jumlahSepeda)

# meremove data
print("===== REMOVE =====")
Barang.remove('sepeda') # membuang data yang pertama kali ditemukan
print(Barang)

# membalikan data
print("===== REVERSE =====")
Barang.reverse()
print(Barang)

Stuff = Barang.copy() # copy() = menjadikan barang menjadi list baru
Stuff.append('gelas')
print(Stuff)
print(Barang)

