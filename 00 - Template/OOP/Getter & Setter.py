class Hero:

	def __init__(self, name, health, armor):
		self.name = name
		self.__health = health
		self.__armor = armor
		#self.info = "name {} : \n\thealth: {}".format(self.name,self.__health)

	@property # merubah sebua variable menjadi method
	def info(self):
		return "name {} : \n\thealth: {}".format(self.name,self.__health)

	@property
	def armor(self):
		pass

	@armor.getter # mendapatkan
	def armor(self):
		return self.__armor

	@armor.setter # merubah
	def armor(self, input):
		self.__armor = input

	@armor.deleter # menghapus variable method
	def armor(self):
		print('==== armor di delet ====')
		self.__armor = None

sniper = Hero('sniper',100,10)

print('==== merubah info ====')
print(sniper.info)
sniper.name = 'dadang'
print(sniper.info)

print('===== getter dan setter untuk __armor: ====')
print(sniper.armor) # Getter
sniper.armor = 50 # setter = menyetel 
print(sniper.armor)

print('==== delete armor ====') # menghapus variable delet
del sniper.armor
print(sniper.__dict__)