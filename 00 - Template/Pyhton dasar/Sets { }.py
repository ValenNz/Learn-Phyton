## HIMPUNAN
  # tidak punya urutan
  # 1 himpunan memiliki 2 nama yang sama dianggap 1 data 

#  himpunan:
superhero = set()

superhero.add("wiro sableng")
superhero.add("gundala")
superhero.add("saras 008")
superhero.add("saras 008") # akan menjadi 1 dng yang sama 
superhero.add(212) # bisa masuk tapi akan error jika di sorted

print(superhero) # hasil akan acak/ tidak urut
print(sorted(superhero)) # mengurutkan terkecil ke besar a -> z

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(ganjil.union(genap)) # Mencari himpunan Gabungan
print(ganjil.intersection(prima)) # Mencari himpunan irisan