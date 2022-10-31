## scope variable : local
   # nama kucing tidak merubah variable global 
namaKucing = 'cassandra'

def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru # variable global
    print('saya rubah nama kucing menjadi',namaKucing)

rubahNamaKucing('ketie')

print('nama kucing saya menjadi',namaKucing)#,'dan makan',makananKucing)



# scope variable : Global

namaKucing = 'cassandra'
makananKucing = 'royal canin'

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru # variable global
    print('saya rubah nama kucing menjadi',namaKucing)

def kasihMakanKucing(makanan,nama):
     global namaKucing,makananKucing
     namaKucing = nama
     makananKucing = makanan

rubahNamaKucing('ketie')

kasihMakanKucing('universal','alex')

print('nama kucing saya menjadi',namaKucing,'dan makan',makananKucing)