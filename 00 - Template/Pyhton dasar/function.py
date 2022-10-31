print("\n===== DEFINISI ====")
# MENDEFINISIKAN FUNGSI

def fungsi():
    print("ini adalah fungsi")

# MEMANGGIL FUNGSI
fungsi()


print("\n===== FUNGSI SEDERHANA =====")
# membuat fungsi sederhana
def suaraayam(): # def (meemanggil ber ulang ulang)
    print('kukuruyuk!!!!')

def hargaayam():
    #suaraayam() # bisa dipangil berulang ulang
    print('harga ayam per 1 kg adalah Rp. 20.000')
    

print("\n===== INPUT ARGUMEN ====")
# membuat fungsi dengan input argumen
def hargatotalayam(kg):
    hargaayam()
    harga = 20000
    hargaTotal = kg*harga
    print('harga',kg,'kg ayam adalah',hargaTotal)

hargaayam()
hargatotalayam(2)
hargatotalayam(0.5)
hargatotalayam(1)
hargatotalayam(9)


print("\n===== ARGUMEN SEDERHANA =====")
# fungsi dengan menggunakan argumen sederhana

def siswa(nama): # () merupakan argumen
    print('siswa ini bernama:',nama)

siswa('mario')


print("\n===== KEYWORDS ARGUMEN =====")
# fungsi dengan menggunakan keywords arguments

def guru(nama,pelajaran):
    print('guru ini bernama:',nama)
    print('mengajar:',pelajaran)

guru(nama='popong',pelajaran='seni rupa')
guru(pelajaran='olah raga',nama='endang')
guru('olah raga','raihan') # ini contoh yang salah


print("\n===== DEFAULTS ARGUMEN =====")
# fungsi dengan menggunakan default arguments
def penjagaSekolah(nama,shift='siang',galak='tidak'):
    print('penjaga sekolah ini bernama:', nama)
    print('shiftnya:', shift)
    print('galak?:', galak)

penjagaSekolah('Entis')
penjagaSekolah('Maman',shift='malam')
penjagaSekolah('Asep',galak='Sangat')
penjagaSekolah(shift='malam',galak='iya') # menghasilkan error


print("\n===== RETURN VALUE =====")
# fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari',argumen,'adalah:',total)
    return total

a = kuadrat(4)
print(a)


print("\n===== RETURN VALUE AND MULTIPLE ARGUMEN =====")
# fungsi dengan return value dan multiple argumen
def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1,'+',argumen2,'=',total)
    return total

def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1,'x',argumen2,'=',total)
    return total

b = kali(3,tambah(3,4))

print(b)


print("\n===== LAMBDA FUNCTION =====")
#lambda functiom

def jumlah(a,b):
    c = a+b
    return c

hasil = jumlah(4,5)


print("\n===== LAMBDA =====") # tidak perlu mengunakan def
# membuat anonymous function dengan lambda

kali = lambda x,y: x*y
hasil = kali(3,4)
print(hasil)

# tanpa def
(lambda x,y: x**2 + y**2)(4,6)
hasil = (lambda x,y: x**2 + y**2)(4,6)
print(hasil)