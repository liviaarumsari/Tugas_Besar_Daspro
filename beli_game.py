rom modul_fungsi.array_function import print_data
from modul_fungsi.array_function import panjang


def splitchar(word):					# Mengubah kata menjadi huruf
    return [char for char in word]

def DataLoc(arr, data, column):			# Mencari baris ke berapa lokasi data tersebut berada
	found = -1
	for i in range(panjang(arr)):
		if arr[i][column] == data:
			found += i+1
			break	
		
	if found > -1:
		return found

def userID(int):
	if int<10:
		return '00' + str(int)
	elif 10 <=int <= 99:
		return '0'+ str(int)
	else:
		return str(int)

kepemilikan= [['G001','002'],['G002','002'],['G033','002']]
user=[['001','mikdar','ghaylan','1234','user',30000],['002','zenn','fatih','4321','user',20000]] #CONTOH DATA, HAPUS SAAT PEMAKAIAN
game=[['G001','pyhton','action','2015',25000,25],['G002','dota','action','2015',20000,2]]
riwayat=[['G001','python','001',2022],['G002','dota','001',2022],['G001','python','002',2022]]
def beli_game(kepemilikan,user,game,riwayat)
    beli=(input('Masukkan id game: '))
    username=input('Masukkan username: ')
    id= userID(DataLoc(user,username,1)+1)
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

    Exist=False

    for j in range(panjang(kepemilikan)):
        if pembelian==kepemilikan[j]:
            Exist=True
            break
    if Exist==True:          
        print('Anda sudah memiliki game tersebut')
    elif game[codegame-1][5]==0: 
        print('Stok Game tersebut sedang habis!')
    elif game[codegame-1][4] > user[id2][5]: 
        print('Saldo anda tidak cukup untuk membeli Game tersebut!')
    else: 
        game[codegame-1][5]=game[codegame-1][5]-1
        user[id2][5]=user[id2][5]-game[codegame-1][4]
        kepemilikan=kepemilikan+[pembelian]
        riwayat=riwayat+[beli,game[codegame][1],2022] #input tahun beli msh manual
        print('Game',f'"{game[codegame][1]}"','berhasil dibeli')
    return game,user,kepemilikan,riwayat


