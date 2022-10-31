# # Memprotek (variable) supaya tidak bisa dirubah
# class Hero:

# 	def __init__(self,name,health,attackPower):
# 		self.__name = name
# 		self.__health = health
# 		self.__attackPower = attackPower

# 	# getter
# 	def getName(self):
# 		return self.__name

# 	def getHealth(self):
# 		return self.__health

# 	# setter

# 	def diserang(self,serangPower):
# 		self.__health -= serangPower # mengurangi darah

# 	def setAttackPower(self,nilaibaru): # merubah damage
# 		self.__attackPower = nilaibaru

# # awal dari game
# earthshaker = Hero("earthshaker",50, 5)

# # game berjalan

# print(earthshaker.getName()) # untuk memamnggil nama hero
# print(earthshaker.getHealth()) # untuk memanggil darah
# earthshaker.diserang(5)
# print(earthshaker.getHealth()) # untuk memanggil darah yang telah diserang

# Membuat Enapsulasi class Hero
class Hero:

	#private class variabel
	__jumlah = 0;

	def __init__(self,name):
		self.__name = name
		Hero.__jumlah += 1

	# method ini hanya berlaku untuk objek
	def getJumlah(self):
		return Hero.__jumlah

	# method ini tidak berlaku untuk objek tapi berlaku untuk class
	def getJumlah1():
		return Hero.__jumlah

	# method static (decorator) nempel ke objek dan class
	@staticmethod
	def getJumlah2():
		return Hero.__jumlah

	@classmethod
	def getJumlah3(cls):
		return cls.__jumlah

sniper = Hero('sniper')
print(Hero.getJumlah1())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2())
drowranger = Hero('drowranger')
print(Hero.getJumlah3())