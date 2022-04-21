from modul_fungsi.array_function import print_data
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

def removeRow(data):
    data_baru=[]
    for i in range(panjang(data)):
        if data[i]!=['']:
            data_baru=data_baru+[data[i]]
    return data_baru

def buy_game(kepemilikan,user,game,riwayat,username):
    kepemilikan=removeRow(kepemilikan)
    user=removeRow(user)
    riwayat=removeRow(riwayat)
    game=removeRow(game)
    beli=(input('Masukkan id game: '))
    id= (DataLoc(user,username,1))
    split=splitchar(beli)
    pembelian=[beli,userID(id)]
    if split[1] == '0' and split[2]=='0':
        codegame=int(split[3])
    elif split[1]=='0' and split[2]!=0:
        codegame=int(split[2]+split[3])
    else:
        codegame=int(split[1]+split[2]+split[3])

    Exist=False

    for j in range(panjang(kepemilikan)):
        if pembelian==kepemilikan[j]:
            Exist=True

    if Exist==True:          
        print('Anda sudah memiliki game tersebut')
    elif int(game[codegame][5])==0: 
        print('Stok Game tersebut sedang habis!')
    elif int(game[codegame][4]) > int(user[id][5]): 
        print('Saldo anda tidak cukup untuk membeli Game tersebut!')
    else: 
        (game[codegame][5])=int(game[codegame][5])-1
        user[id][5]=str(int(user[id][5])-int(game[codegame][4]))
        kepemilikan=kepemilikan+[pembelian]
        riwayat=riwayat+[[beli,game[codegame][1],game[codegame][4],userID(id),2022]] #input tahun beli msh manual
        print('Game',f'"{game[codegame][1]}"','berhasil dibeli')




    return (kepemilikan,user,game,riwayat)


