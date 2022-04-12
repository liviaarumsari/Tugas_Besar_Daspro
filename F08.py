from modul_fungsi.array_function import print_data
from modul_fungsi.array_function import panjang

def splitchar(word):					# Mengubah kata menjadi huruf
    return [char for char in word]


kepemilikan= [['G001','001'],['G002','002'],['G033','002']]
user=[['001','mikdar','ghaylan','1234','user',30000],['002','zenn','fatih','4321','user',20000]]
game=[['G001','pyhton','action','2015',25000,25],['G002','dota','action','2015',20000,2]]
id='002'

beli=(input('Masukkan id game: '))
split=splitchar(beli)
pembelian=[beli,id]

if split[1] == '0' and split[2]=='0':
    codegame=int(split[3])
elif split[1]=='0' and split[2]!=0:
    codegame=int(split[2]+split[3])
else:
    codegame=int(split[1]+split[2]+split[3])

split2=splitchar(id)
if split2[0] == '0' and split2[1]=='0':
    id2=int(split[2])
elif split2[0]=='0' and split2[1]!=0:
    id2=int(split2[1]+split2[2])
else:
    id2=int(split2[0]+split2[1]+split2[2])

for j in range(panjang(kepemilikan)):
    if pembelian==kepemilikan[j]:
        Exist=True
        break

if Exist==True:          #cuma bisa G001 dan id='001'
    print('Anda sudah memiliki game tersebut')
elif game[codegame-1][5]==0: #aman
    print('Stok Game tersebut sedang habis!')
elif game[codegame-1][4] > user[id2-1][5]: #aman
    print('Saldo anda tidak cukup untuk membeli Game tersebut!')
else: #aman
    kepemilikan=kepemilikan+[pembelian]
print_data(kepemilikan)

