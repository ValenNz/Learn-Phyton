class Hero:

	def __init__(self,name,health,attackPower,armorNumber):
		self.name = name
		self.health = health
		self.attackPower = attackPower
		self.armorNumber = armorNumber

	def serang(self, lawan):
		print(self.name + ' menyerang ' + lawan.name ) # menunjukan bahwa sniper menyetang rikimaru
		lawan.diserang(self, self.attackPower) # menunjukan bahwa rikimaru diserang sniper

	def diserang(self, lawan, attackPower_lawan):
		print(self.name + ' diserang ' + lawan.name)
		attack_diterima = attackPower_lawan/self.armorNumber
		print('serangan terasa : ' + str(attack_diterima)) # menunjukan serangan sniper yang terasa di rikimaru
		self.health -= attack_diterima
		print('darah ' + self.name + ' tersisa ' + str(self.health)) # memnunjukan darah rikimaru akibat diserang sniper

sniper = Hero('sniper',100,10,5)
rikimaru = Hero('rikimaru',100,20,10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)