## STACKS
 # data yang keluarnya di akhir

print("===== STACKS =====")
tumpukan = [1,2,3,4,5,6]
print('data sekarang: ',tumpukan)

# memasukan data baru
tumpukan.append(7)
print('data masuk: ',7)
print('data sekarang: ',tumpukan)
tumpukan.append(8)
print('data masuk: ',8)
print('data sekarang: ',tumpukan)

out = tumpukan.pop()  # pop() menghilangkan data paling belakang
print('data keluar: ',out)
print('data sekarang: ',tumpukan)


## QUEUES
 # data yang keluar di awal
from collections import deque

antrian = deque([1,2,3,4,5]) # deque() menambah or mengurangi data depan

print('data sekarang: ',antrian)

# menambahkan data
antrian.append(6)
print('data masuk: ',6)
print('data sekarang: ',antrian)

antrian.append(7)
print('data masuk: ',7)
print('data sekarang: ',antrian)

# mengurangi antrian
out = antrian.popleft() # popleft() mengurangi data yang depan
print('data keluar: ',out)
print('data sekarang: ',antrian)

out = antrian.popleft() # popleft() mengurangi data yang depan
print('data keluar: ',out)
print('data sekarang: ',antrian)

out = antrian.popleft() # popleft() mengurangi data yang depan
print('data keluar: ',out)
print('data sekarang: ',antrian)

antrian.append(8)
print('data masuk: ',8)
print('data sekarang: ',antrian)