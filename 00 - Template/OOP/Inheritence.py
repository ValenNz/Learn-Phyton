# INHERITENCE (PEWARISAN)
  # sesuatu yang diwariskan/ diturunkan berlaku antara class ke class
      # mewariskan ke class 1 (superclass) ke class 2 (subclass)
 # ingin menghindari pengulangan
 
class Hero:

	def __init__(self,name,health):
		self.name = name
		self.health = health

class Hero_intelligent(Hero): # kekuatan kepintaran
	pass

class Hero_strength(Hero): #kekuatannya di kekuatan (mewariskan yang sudah ada di class Hero)
	pass

lina = Hero('lina',100)
techies = Hero_intelligent('techies',50)
axe = Hero_strength('axe',200)

print(lina.name)
print(techies.name)
print(axe.name)