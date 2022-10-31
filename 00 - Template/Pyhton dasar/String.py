## BENTUK STRING
data = "Its String"
print(data)
print(type(data))





## OPERASI DAN MANIPULASI STRING
print("\n++++++++++++++ OPERASI DAN MANIPULASI STRING +++++++++++++++++")

# 1.  Menyambung String (CONCATENATE)
Nama_pertama = "Nuevalen"
Nama_kedua   = "Refitra"
Nama_ketiga  = "Alswando"
Nama_lengkap = Nama_pertama + " " + Nama_kedua +" " + Nama_ketiga
print(Nama_lengkap)

# 2. Menghitung panjang string
panjang = len(Nama_lengkap)
print("panjang dari " + Nama_lengkap + " = " + str(panjang))

# 3. Operator Untuk String
     # Mengecek apakah ada komponen char atau string di STRING

d = "d"
status = d in Nama_lengkap
print("string "+ d + " ada di " + Nama_lengkap + " = " + str(status))
D = "D"
status = D in Nama_lengkap
print("string "+ D + " ada di " + Nama_lengkap + " = " + str(status))
D = "D"
status = D not in Nama_lengkap
print("string "+ D + " ada di " + Nama_lengkap + " = " + str(status))

# 4. Mengulang String
print("Wk"*10)
print(10*"Wk")

# 5. INDEXING
print("index ke -0 : " + Nama_lengkap[0])
print("index ke -(-1) : " + Nama_lengkap[-1]) # Mengambil dari belakang
print("index ke -[0:3] : " + Nama_lengkap[0:4]) # (:) sampai, yang diambil 0 sampai 4 (dihitung dari 0)
print("index ke -[3:6] : " + Nama_lengkap[3:7])
print("index ke -[0,2,4,6,8] : " + Nama_lengkap[0:8:2]) # (:2) merupakan diloncati 2 

# 6. Item 
print("Paling kecil : " + min(Nama_lengkap))
print("Paling Besar : " + max(Nama_lengkap))

# 7. Ascii code
ascii_code = ord(" ")
print("ASCII CODE untuk spasi adalah " + str(ascii_code))
data = 110
print("Char untuk ASCII CODE 110 adalah " + chr(data))

# 8. Operator dalam bentuk Method
data = "Nuevalen Refitra Alswando"
jumlah = data.count("a")
print("Jumlah a pada " + data + " = " + str(jumlah))





## FORMAT STRING
print("\n+++++++++++++++++ FORMAT STRING ++++++++++++++++++++")

# STRING
nama = " Valen"
format_str = f"hello {nama}"
print(format_str)

# BOOLEAN
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# ANGKA
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# BILANGAN BULAT
angka = 10
format_str = f"bilangan bulat = {angka:d}" # (:d) menampilkan bahwa si d merupakan bilangan bulat
print(format_str)

# BILANGAN RIBUAN
angka = 2000
format_str = f"Ribuan = {angka:,}" # (:,) meletakan koma setelah angka 2
print(format_str)

# BILANGAN DESIMAL
angka = 2005.54321
format_str = f"desimal = {angka:.2f}" # (:.2f) mengambil 2 dibelakang koma
print(format_str)

# MENAMPILKAN LEADING ZERO
angka = 2005.54321
format_str = f"desimal = {angka:9.3f}" # (:.2f) mengambil 2 dibelakang koma
print(format_str)
angka = 2005.54321
format_str = f"desimal = {angka:09.3f}" # (:.2f) mengambil 2 dibelakang koma
print(format_str)

# MENAMPILKAN TANDA +/-
angka_minus = -10
angka_plus   =  10
format_minus = f"minus = {angka_minus}"
format_plus  = f"plus = {angka_plus:+d}" # (:+d) menampilkan tanda (+) pada angka
print(format_minus)
print(format_plus)

# MEMFORMAT PERSEN
persentase = 0.045
format_persen = f"persen = {persentase:%}"
print(format_persen)

# MELAKUKAN OPERASI ARITMATIKA DIDALAM PLACE HOLDER
harga = 10000
jumlah = 5
format_string = f"Total harga = Rp. {harga*jumlah:,}"
print(format_string)

# FORMAT ANGKA LAIN 
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)



