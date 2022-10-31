## LIST SEBAGAI ITERABLE
print("==== LIST =====")

gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']

for g in gorengan: # (g) untuk print gorengan
    print(g)
    print(len(g)) # menghitung jumlah huruf (len)


##  STRING SEBAGAI ITERABLE
print("\n===== STRING ====")

bakwan = 'bakwan'

for i in bakwan: # (i) mengeja 
    print(i)


## FOR DIDALAM FOR
print("\n==== for in for ====")

gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']
buah     = ['semangka','jeruk','apel','anggur']
sayur    = ['kangkung','wortel','tomat','kentang']
Daftar_belanja = [gorengan,buah,sayur]

for subDaftarBelanja in Daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)


## RANGE SEBAGAI ITERABLE
print("\n==== RANGE =====")

for i in range(0,6):
    print(i)

print("==== RANGE KELIPATAN ====")

for i in range(10,40,5): # (,5) merupakan kelipatan
    print(i)


## ELSE 
print("\n==== ELSE ====")
number = 3

for i in range(0,6):
    print(i)

    if i is number: 
         print("Angka ditemukan",i)
else:
    print("Angka tidak ditemukan ")

print("\n==== ELSE BREAK ====")
number = 3

for i in range(0,6):
    print(i)

    if i is number: 
         print("Angka ditemukan",i)
         break 
else:
    print("Angka tidak ditemukan")


## CONTINUE 
print("\n===== CONTINUE ====")

for i in range(1,6):

    if i is 4:
        print("nilai i adalah",4)
        continue 
        # break : fungsinya untuk mengakhiri for (terminasi)
        # continue : fungsinya untuk melanjutnya ke step berikutnya


## PASS    
print("\n==== PASS ====")
for i in range(1,6):

    if i is 4:
        print("nilai i adalah",4)
        pass # dilewati 
        print("cek bro 1")
    print('nilai saat ini adalah',i)
else:
    print('akhir dari loop')

print('print diluar loop')


























