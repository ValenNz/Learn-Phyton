angka = 1

while angka < 5:
    print( 'nilai angka adalah:', angka)
    angka = angka + 1

print('di luar while')


# sVarieable bolean
print("\n===== BOOLEAN ======")

start = True 
angka = 0

while start:
    print("di dalam while")
    if angka is 10:
        start = False
        print('oke angka 100 diketemukan')
    angka += 1


# else, break, continue, pass
angka = 0

while angka < 10:

    if angka is 5:
         #print('checkpoint 1')
         break
         #angka += 1 # continue
         #continue
         #pass
         #print('checkpoint 2')

    print( 'nilai angka adalah:', angka)
    angka += 1
else:
    print('nilai angka diakhir while adalah',angka)

print('di luar while')