from modul_fungsi.array_function import panjang

def removeRow(data):
    data_baru=[]
    for i in range(panjang(data)):
        if data[i]!=['']:
            data_baru=data_baru+[data[i]]
    return data_baru

def topup(user):   #user=data
    user=removeRow(user)
    username=input('Masukkan username: ')

    topup=int(input('Masukkan saldo: '))


    for i in range (panjang(user)):
        if user[i][1] == username:
            if (int(user[i][5]) + topup)<0:
                print('Masukan tidak valid')
                break
            elif i==(panjang(user)-1) and user[i][1]!=username:
                print(f'Username {username} tidak ditemukan.')
            else:
                print(f'Top up berhasil. Saldo {username} bertambah menjadi {int(user[i][5]) + topup}')
                user[i][5]= int(user[i][5])+ topup
                user[i][5]= str(user[i][5])
                
    return user
       
