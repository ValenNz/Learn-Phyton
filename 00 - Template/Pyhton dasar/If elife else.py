# if
  # melakukan penilaian (jika)
print("++++++++++++++++++++++++++ IF +++++++++++++++++++++++++++")
nilai = 50

if nilai == 75: # equal eksplisit
    print("Nilai anda:",nilai)

if nilai is 60: # equal
    print("Nilai anda:", nilai)

if nilai is not 60: # not equal
    print("Nilai anda:", nilai)





# ELIFE
   # jika tidak masuk di pertama akun dicoba di setelahnya (syarat tambahan)
print("\n+++++++++++++++++++++++++ ELIFE +++++++++++++++++++++++++++")

nilai = 65

if 80 <= nilai <= 100: # step 1
    print("Nilai anda adalah A")

elif 70 <= nilai < 80: # step 2
    print("Nilai anda adalah B") 

elif 60 <= nilai < 70: # step 3
    print("Nilai anda adalah C")

elif 50 <= nilai < 60: # step 4
    print("Nilai anda adalah T, lakukan perbaikan")

else: # jika nggak masuk kesemua (elif maupun if )
    print("maaf anda tidak lulus mata kuliah ini")





print("\n+++++++++++ operator logika list dan string ++++++++++++++++\n")

gorengan=["bakwan","cireng","bala-bala","gehu","combro","pisang goreng","pukis","risoles"]
beli = "bakwan"

if beli in gorengan:
    print('" ya, saya jual',beli,'"')

if not beli in gorengan:
    print('"saya gak jual',beli,'"')

# MENGECEK CHARACTER
karakter = "k"
if karakter in beli:
    print("ada", karakter, "di",beli)
else:
    print("tidak ada",karakter,"di",beli)