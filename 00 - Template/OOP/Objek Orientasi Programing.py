# OOP
# print("===== CLASS =====")

# class Hero: # template
#     pass


# hero1 = Hero() # object / instance (instansiate)
# hero2 = Hero()
# hero3 = Hero();

# hero1.name = "sniper" # atribute (suatu hal yang dimiliki oleh objek)
# hero1.health = 100

# hero2.name = "sven"
# hero2.health = 200

# hero3.name = "ucup"
# hero3.health = 1000

# print(hero1) # melihat identitas
# print(hero1.__dict__) # mendeskripsikan
# print(hero1.name) # menampilkan nama hero





# __INIT__
print("\n===== __init__ =====")
  # akan di eksekusi jika objek dibuat

class Hero: # template

    def __init__(self, inputName, inputHealth,inputPower, inputArmor):
    	self.name = inputName
    	self.health = inputHealth
    	self.power = inputPower
    	self.armor = inputArmor


hero1 = Hero("sniper",100, 10, 4) # objek + atribute
hero2 = Hero("mirana",100, 15, 1)
hero3 = Hero("ucup",1000, 100, 0)

print(hero1.__dict__) # komponen komponen pada hero
print(hero2.power) # memanggil/melihat power heronya
print(hero3.health) # melihat health heronya





# # CLASS VARIABLE AND INTANCE VARIABLE
# print("\n===== CLASS VARIABLE AND INTANCE VARIABLE =====")

# class Hero: #template
# 	#class variabel
# 	jumlah = 0

# 	def __init__(self,inputName,inputHealth,inputPower,inputArmor):
# 		# instance variabel
#            # akan dimiliki sang hero saja
# 		self.name = inputName
# 		self.health = inputHealth
# 		self.power = inputPower
# 		self.armor = inputArmor
# 		Hero.jumlah += 1
# 		print("membuat Hero dengan nama " + inputName)


# hero1 = Hero("sniper",100, 10, 4)
# print(Hero.jumlah)
# hero2 = Hero("mirana",100, 15, 1)
# print(Hero.jumlah)
# hero3 = Hero("ucup",1000, 100, 0)
# print(Hero.jumlah)





# ## METHOD
# print("\n===== METHOD =====")

# class Hero:
# 	# class variabel
# 	jumlah_hero = 0

# 	def __init__(self, inputName, inputHealth, inputPower, inputArmor):
# 		#instance variabel
# 		self.name = inputName
# 		self.health = inputHealth
# 		self.power = inputPower
# 		self.armor = inputArmor
# 		Hero.jumlah_hero += 1

# 	# void function, method tanpa return, tanpa argumen
# 	def siapa(self):
# 		print("namaku adalah " + self.name)

# 	# method dengan argumen, tanpa return
# 	def healthUp(self,up):
# 		self.health += up

# 	# method dengan return
# 	def getHealth(self):
# 		return self.health


# hero1 = Hero('sniper', 100, 10, 5)
# hero2 = Hero('mario bros', 90, 5, 10)

# hero1.siapa()
# hero1.healthUp(10)

# print(hero1.getHealth())


# Private variabel
print("\n==== PRIVATE VARIABEL ====")
class Hero:

	# class variabel
	jumlah = 0
	__privateJumlah = 0

	def __init__(self,name,health):
		self.name = name
		self.health = health

		# variabel instance private
		self.__private = "private"
		# variabel instance protected
		self._protected = "protected"



lina = Hero("lina",100)

print(lina.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)