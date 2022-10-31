## ATRIBUTE
  # nilai yang nempel pada class  (nama = 'nama')
print("===== ATRIBUTE =====")

class Mahasiswa(): # class mahasiswa adalah kumpulan mahasiswa(nama)
	nama = 'nama' 

otong = Mahasiswa() # otong = intenst/objek # mahasiswa = class
ucup = Mahasiswa()

otong.nama = "otong surotong" 
ucup.nama = "michael ucup"

print(otong.nama)
print(ucup.nama)



## METHOD
  # berlaku jika dipanggil fungsinya
  # fungsi yang nempel di class
print("\n===== METHOD =====")

class Mahasiswa():
	nama = 'nama'

	def belajar(self, kondisi): # self = pemilik method
		print(self.nama,'sedang belajar', kondisi) # kondisi bisa untuk tambahan argumen(40)

	def tidur(self):
		print(self.nama,'tidur di kelas')

# main programnya

otong = Mahasiswa()
ucup = Mahasiswa()

otong.nama = "otong surotong"
ucup.nama = "michael ucup"

otong.belajar('dengan giat')
ucup.tidur()



## INIT
print("\n===== __INIT__ =====")

#class
class Mahasiswa():
	nama = 'nama' # tidak perlu

	def __init__(self, input_nama, input_nim):
		self.nama = input_nama
		self.nim = input_nim

	def belajar(self, kondisi):
		print(self.nama,'sedang belajar', kondisi)

# main programnya

otong = Mahasiswa("otong surotong", 13317001)
print(otong.nama)
print(otong.nim)

otong.belajar('dengan giat')



## PRIVATE ATRIBUTE
 # ada sebuah variable yang hanya bisa dirubah didalam class
print("\n===== PRIVATE ATRIBUTE =====")

# class
class mahasiswa():

    jurusan = "teknik tata boga" # bisa diakses(dirubah)
    __nilai = 0 # private # tdk bisa dia akses  (tdk dirubah)

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim  # public

# acc private

    def uts(self,input_nilai):
        self.__nilai += input_nilai

    def uas(self,input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,'tidak lulus')
        else:
            print(self.nama, 'lulus')

# main programnya

otong = mahasiswa("otong surotong", 13317001)
ucup = mahasiswa("michael ucup", 13317002)

otong.uts(10)
otong.uas(50)
otong.check_status()

ucup.uts(5)
ucup.uas(25)
ucup.check_status()



## CLASS VARIABLE
print("\n===== VARIABLE =====")

# class
class mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim  # public
        mahasiswa.jumlah_mahasiswa += 1

# main programnya

otong = mahasiswa("otong surotong", 13317001)
ucup = mahasiswa("michael ucup", 13317002)
cassandra = mahasiswa("cassandra aja", 13317002)

print(mahasiswa.jumlah_mahasiswa)



## CLASS INHERITANCE
 # mendapat turunan atau Akan sama dengan inangnya
print("\n===== INHERITANCE =====")

class Ojek():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_abang(self):
        print('nama:',self.nama,'\nmotor:',self.transmisi,'\ndaerah:',self.daerah)

class Gojek(Ojek): # mendapat semua di ojek (copas)

    def cek_id_abang(self):
        print('cek aplikasi gojek')


ojek1 = Ojek('mario','manual','bandung selatan')
ojek2 = Gojek('jackson','automatic','tasikmalaya')

ojek1.cek_id_abang()
ojek2.cek_id_abang()















