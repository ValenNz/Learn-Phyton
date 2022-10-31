## dictionary
 # sifat asosiatif adalah sifat dari beberapa operasi biner, yang berarti bahwa mengatur ulang tanda kurung dalam ekspresi yang tidak mengubah hasilnya.
 # dict = {key:value,key:value}
member1 = {"ID":101,
           "Nama":"Faqihza Mukhlish",
           "Pekerjaan":"Mahasiswa",
           "Status member":"Gold"
           }
# print(member1["ID"]) # mengambil salah satu (harus menggunakan key) cara mengakses data
#  #print(member1[101]) # jika value yang dimasukan maka akan error
# print(member1.keys()) # mengakses keys nya saja
# print(member1.value()) # mengakses value nya saja
# print(member1.items()) # mengakses semua item pada member1

member2 = {"ID":102,
           "Nama":"Ujang Pintu",
           "Pekerjaan":"reparasi pintu",
           "Status member":"Berlian"}

memberlist = {101:member1,102:member2} #  bisa memasukan dict kedalam list

print(memberlist[101])