# Hero -> healt, attpower, armor (bisa dilihat client) = nilainya akan berubah sesuai level
# level akan berubah berdasarkan exsperients exsperients tidak bisa dilihat client)
# method = tambah experients

class Hero:

	#private class variabel
	__jumlah = 0

	def __init__(self,name,health,attPower,armor):
		self.__name = name
		self.__healthStandar = health # harus menggunakan healtawal supaya bisa dinaikan levelnya
		self.__attPowerStandar = attPower # harus menggunakan attpowerawal supaya bisa dinaikan levelnya
		self.__armorStandar = armor # harus menggunakan armorawal supaya bisa dinaikan levelnya
		self.__level = 1 # tidk boleh di setting
		self.__exp = 0

# menaikan healt, power, armor sesuai level
		self.__healthMax = self.__healthStandar * self.__level # healtMax = nilai tertinggi
		self.__attPower = self.__attPowerStandar * self.__level
		self.__armor = self.__armorStandar * self.__level
# healt sebenarnya/healt sekarang
		self.__health = self.__healthMax
# akan nambah setiap kita bikin hero baru
		Hero.__jumlah += 1
# membuat info sekarng heronya memiliki atribute
	@property
	def info(self):
		return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)
# mengambil experients
	@property
	def gainExp(self):
		pass
# mendapatkan exp
	@gainExp.setter
	def gainExp(self,addExp): # menambahkan exp
		self.__exp += addExp
		if (self.__exp >= 100): # setiap exp lebih dari 100 maka akan naik level
			print(self.__name, 'level up') # level naik
			self.__level += 1
			self.__exp -= 100 # setiap lebih dari 100 akan mereset dari 0 (sisa tetep ada)

			self.__healthMax = self.__healthStandar * self.__level
			self.__attPower = self.__attPowerStandar * self.__level
			self.__armor = self.__armorStandar * self.__level

	def attack(self,musuh):
		self.gainExp = 50

slardar = Hero('slardar', 100, 5, 10) # objek/hero
axe = Hero('axe', 100, 5, 10) # objek/hero
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe) # akan ganti exp
slardar.attack(axe) # akan ganti exp

print(slardar.info)
#print(slardar.gainExp) # menyembunyikan/ tdk dapat dilihat (none)
