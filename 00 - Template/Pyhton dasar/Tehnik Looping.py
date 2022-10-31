# # teknik looping

nama_band = ['Payung Teduh',
             'Fourtwnty',
             'Dialog Dini Hari',
             'Mr. Sonjaya',
             'Parahyena',
             'Syahrini'] # tdk akana ditampilkan jika tidak sama banyak dengan lawan main list

iterasi = 0; # untuk menampilak index nya
for band in nama_band: # meng out put semua daftar
     print(band)
     print,('no:', iterasi, 'namaband', band) 
     iterasi+=1 # memberikan nomer

kumpulan_lagu = ['Akad',
        'Zona Nyaman',
        'Rumahku',
        'Sang Filsuf',
        'Sindoro',
        'Jodohku']

# ## enumerate
   # memberikan nomer
print("===== ENUMERATE =====")

for index,band in enumerate(nama_band):
     print(index,':',band)

## zip
  # menggabungkan 2 list dalam 1 looping
print("===== ZIP =====")

for band,lagu in zip(nama_band,kumpulan_lagu):
     print(band,'menyanyikan lagu yang berjudul:',lagu)

## set
print("===== SET =====")
playlist = {'baby baby', 'ada apa dengan cinta', 'cenat-cenut', 'jaran goyang', 'jaran goyang', 'gorgom', 'kuda', 'kucing'}

for lagu in sorted(playlist): # mengurutkan a -> b
     print(lagu)

# dictionary
print("===== DICTIONARY =====")

playlist2 = {'Payung Teduh': 'akad',
             'Fourtwnty':'Zona Nyaman',
             'Dialog Dini Hari':'Rumahku',
             }

for i in playlist2.items(): # mengambil semua
    print(i,'lagunya:')

for i,v in playlist2.items(): # mengambil semua dibagi 2 tanpa ada kurung dan ""
    print(i,'lagunya:',v)

for i in playlist2.keys(): # mengambil keys saja
    print(i)

for i in playlist2.value(): # mengambil value saja
    print(i)

for i in reversed(range(1,10,1)): # 9 -.1
    print(i)