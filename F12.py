
from tkinter import E
from modul_fungsi.array_function import panjang

def Exist(arr,data, column):		    # Validasi apakah data ada
	i = 0
	for i in range(panjang(arr)):
		LookUp = arr[i][column]
		if LookUp == data:
			return True
		else:
			return False

username=input('Masukkan username: ')
topup=int(input('Masukkan saldo: '))

user=[['001','mikdar','ghaylan','1234','user',30000],['002','zenn','fatih','4321','user',20000]]

if Exist(user,username,1)==False:
    print(f'Username “{username}” tidak ditemukan.')

for i in range (panjang(user)):
    if user[i][1] == username:
        if (user[i][5] + topup)<0:
            print('Masukan tidak valid')
        else:
            print(f'Top up berhasil. Saldo {username} bertambah menjadi {user[i][5] + topup}')
            user[i][5]= user[i][5]+ topup
print(user)