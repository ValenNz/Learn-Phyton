# OPERASI ARITMATIKA
print("+++++++++++++++++++++ ARITMATIKA +++++++++++++++++")

a = 10
b = 4
c = 5

# PENJUMLAHAN (+)
hasil = a + b
print(a,"+",b,"=",hasil)

# PENGURANGAN (-)
hasil = a - b
print(a,"-",b,"=",hasil)

# PERKALIAN (*)
hasil = a * b
print(a,"*",b,"=",hasil)

# PEMBAGIAN (/)
hasil = a / b
print(a,"/",b,"=",hasil)

# EKSPONEN / PANGKAT (**)
hasil = a ** b
print(a,"**",b,"=",hasil)

# MODULUS / SISA PEMBAGIAN (%)
hasil = a % b
print(a,"%",b,"=",hasil)

# FLOOR DIVISION / DIBULATKAN KEBAWAH (//)
hasil = a // b
print(a,"//",b,"=",hasil)

# TANDA KURUNG
hasil = (a + b) * c
print("(",a,"+",b,") *",c,"=",hasil)

# PRIORITAS OPERASI (operational precedence)
x = 10
y = 4
z = 5
Hasil = x + y * z / y
print(x, "+",y,"*",z,"/",y,"=",Hasil) 
# CATATAN (Prioritas = () - Pangkat - Perkalian/Pembagian - Penjumlahan/Pengurangan)





## COMPARISON OPERATION
print("\n+++++++++++++++++++++ KOMPARASI ++++++++++++++++++")
     # setiap hasil dari komprasi pasti boolean
a = 10
b = 2

print("--[Lebih Dari]--")
hasil = a > 3 
print(a,">",3,"=",hasil)
hasil = b > 3 
print(b,">",3,"=",hasil)
hasil = a > 10 
print(a,">",10,"=",hasil)

print("\n--[Kurang Dari]--")
hasil = a < 3 
print(a,"<",3,"=",hasil)
hasil = b < 3 
print(b,"<",3,"=",hasil)
hasil = a < 10 
print(a,"<",10,"=",hasil)

print("\n--[Lebih Dari Sama Dengan]--")
hasil = a >= 3 
print(a,">=",3,"=",hasil)
hasil = b > 3 
print(b,">=",3,"=",hasil)
hasil = a >= 10 
print(a,">=",10,"=",hasil)

print("\n--[Kurang Dari Sama Dengan]--")
hasil = a <= 3 
print(a,"<=",3,"=",hasil)
hasil = b <= 3 
print(b,"<=",3,"=",hasil)
hasil = a <= 10 
print(a,"<=",10,"=",hasil)

print("\n--[Sama Dengan]--")
hasil = a == 3 
print(a,"==",3,"=",hasil)
hasil = b == 3 
print(b,"==",3,"=",hasil)
hasil = a == 10 
print(a,"==",10,"=",hasil)

print("\n--[Tidak Sama Dengan]--")
hasil = a != 3 
print(a,"!=",3,"=",hasil)
hasil = b != 3 
print(b,"!=",3,"=",hasil)
hasil = a != 10 
print(a,"!=",10,"=",hasil)

print("\n--[Objek Identity is]--")
x = 5 # assigment untuk membuat objek 
y = 5
print("nilai x =,",x,",id = ",hex(id(x)))
print("nilai x =,",y,",id = ",hex(id(y)))
hasil = x is y
print("x is y =",hasil) # is sebagai komperasi objek identity

x = 5  
y = 6
print("nilai x =,",x,",id = ",hex(id(x)))
print("nilai x =,",y,",id = ",hex(id(y)))
hasil = x is y
print("x is y =",hasil) 

print("\n--[Objek Identity is not]--")
x = 5  
y = 5
print("nilai x =,",x,",id = ",hex(id(x)))
print("nilai x =,",y,",id = ",hex(id(y)))
hasil = x is not y
print("x is y =",hasil) 

x = 5  
y = 6
print("nilai x =,",x,",id = ",hex(id(x)))
print("nilai x =,",y,",id = ",hex(id(y)))
hasil = x is not y
print("x is y =",hasil) 





## OPERASI LOGIKA DAN KOMPERASI
print("\n+++++++++++++++++ LOGIKA DAN KOMPERASI +++++++++++")

print("====IRISAN====")
# ------2++++++6------8++++++12------

inputuser = float(input("Masukan angka ;"))
Angka = 2 < inputuser < 6 or 8 < inputuser < 12
print("Angka yang anda masukan :",Angka)

print("====Gabungan====")
#++++++2------6++++++8------12++++++

inputuser = float(input("Masukan angka ;"))
Angka = 2 > inputuser or 6 < inputuser < 8 or inputuser > 12
print("Angka yang anda masukan :",Angka)





## OPERASI LOGIKA DAN BOOLEAN
print("\n+++++++++++++++++ LOGIKA DAN BOLEAN ++++++++++++++")

print("====NOT====")
a =  True # jika a = false makan hasilnya true
b = not a
print("data a =", a)
print("----------------NOT")
print("data b =", b)

print("====OR====")
a = False
b = False
c = a or b
print(a,"OR",b,"=",c)
a = False
b = True
c = a or b
print(a,"OR",b,"=",c)
a = True
b = False
c = a or b
print(a,"OR",b,"=",c)
a = True
b = True
c = a or b
print(a,"OR",b,"=",c)
# Jika salah satu True maka hasilnya akan (True)

print("====AND====")
a = False
b = False
c = a and b
print(a,"AND",b,"=",c)
a = False
b = True
c = a and b
print(a,"AND",b,"=",c)
a = True
b = False
c = a and b
print(a,"AND",b,"=",c)
a = True
b = True
c = a and b
print(a,"AND",b,"=",c)
# jika 2 buah (True) maka hasilnya akan (True)

print("====XOR====")
a = False
b = False
c = a ^ b
print(a,"XOR",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"XOR",b,"=",c)
a = True
b = False
c = a ^ b
print(a,"XOR",b,"=",c)
a = True
b = True
c = a ^ b
print(a,"XOR",b,"=",c)
 # hasilnya akan (True) jika salah satu true, sisanya (false)




## OPERATOR BITWISE (OPERASI BINER)
print("\n+++++++++++++++++++++ BITWISE ++++++++++++++++++")
a = 9
b = 5

print("\n===============OR===============")
c = a | b
print("nilai :",a,",binary :",format(a,"08b"))
print("nilai :",b,",binary :",format(b,"08b"))
print("----------------------------(|)")
print("nilai :",c,",binary :",format(c,"08b"))

print("\n===============AND===============")
c = a & b
print("nilai :",a,",binary :",format(a,"08b"))
print("nilai :",b,",binary :",format(b,"08b"))
print("----------------------------(&)")
print("nilai :",c,",binary :",format(c,"08b"))

print("\n===============XOR===============")
c = a ^ b
print("nilai :",a,",binary :",format(a,"08b"))
print("nilai :",b,",binary :",format(b,"08b"))
print("----------------------------(^)")
print("nilai :",c,",binary :",format(c,"08b"))

print("\n===============NOT===============")
c = ~a 
print("nilai :",a,",binary :",format(a,"08b"))
print("----------------------------(~)")
print("nilai :",c,",binary :",format(c,"08b"))

print("\n===========NOT KE XOR============")
c = ~a 
print("nilai :",a,",binary :",format(a,"08b"))
print("----------------------------(~)")
print("nilai :",c,",binary :",format(c,"08b"))
print("----------------------------(^)")
d = 0b0000001001
e = 0b1111111111 # XOR
print("nilai :",e ^ d,",binary :",format(e ^ d,"08b"))

# SHIFTING

print("====RIGHT====")
c = a >> 2
print("nilai :",a,",binary :",format(a,"08b"))
print("----------------------------(>>)")
print("nilai :",c,",binary :",format(c,"08b"))

print("====LEFT====")
c = a << 2
print("nilai :",a,",binary :",format(a,"08b"))
print("----------------------------(<<)")
print("nilai :",c,",binary :",format(c,"08b"))







