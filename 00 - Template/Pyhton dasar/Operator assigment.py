## OPERATOR ASSIGMENT
 # operasi yang dapat dilakukan dengan penyingkatan
 # operasi yang di tambah assigment


print("\n+++++++++++++++++++++ ASSIGMENT ++++++++++++++++++")
a = 5 # ini adalah assigment
a += 1 # artinya a = a + 1
print("nilai a += 1, nilai a menjadi",a)
a -= 2 # artinya a = a - 2
print("nilai a -= 2, nilai a menjadi",a)
a *= 5 # artinya a = a * 5
print("nilai a *= 1, nilai a menjadi",a)
a /= 2 # artinya a = a / 2
print("nilai a /= 1, nilai a menjadi",a)


print("\n+++++++++++++ MODULUS AND FLOOR DIVISION +++++++++++")
b = 10
print("nilai b =",b)
b %= 3
print("nilai b %= 3, Nilai b menjadi",b)


print("\n++++++++++++++++++++ ARITMATIKA+++++++++++++++++")
a = 5
print("nilai a =",a)
a **= 3
print("nilai a **= 3, Nilai a menjadi",a)


print("\n++++++++++++++++++++ BITWISE ++++++++++++++++++++++")

print("====OR====")
c = True
print("Nilai c =",c)
c |= False
print("Nilai c |= False, Nilai c menjadi",c)
c = False
print("Nilai c =",c)
c |= False
print("Nilai c |= False, Nilai c menjadi",c)

print("====AND====")
c = True
print("Nilai c =",c)
c &= False
print("Nilai c &= False, Nilai c menjadi",c)
c = True
print("Nilai c =",c)
c &= True
print("Nilai c &= False, Nilai c menjadi",c)

print("====XOR====")
c = True
print("Nilai c =",c)
c ^= False
print("Nilai c ^= False, Nilai c menjadi",c)
c = True
print("Nilai c =",c)
c ^= True
print("Nilai c ^= False, Nilai c menjadi",c)


print("\n++++++++++++++++++++ BINARY ++++++++++++++++++++++")
d = 0b0100
print("Nilai d =",format(d,"04b"))
d >>= 2
print("Nilai d >>= 2, Nilai d menjadi",format(d,"04b"))
d <<= 1
print("Nilai d <<= 2, Nilai d menjadi",format(d,"04b"))