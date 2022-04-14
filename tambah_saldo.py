from modul_fungsi.array_function import panjang

def tambah_saldo(user):   #user=data
    username=input('Masukkan username: ')

    topup=int(input('Masukkan saldo: '))

    Exist=False

    for j in range(panjang(user)):
        if user[j][1] == username:        
            Exist=True
            break
    if Exist==True:
        for i in range (panjang(user)):
            if user[i+1][1] == username:
                if (user[i+1][5] + topup)<0:
                    print('Masukan tidak valid')
                else:
                    print(f'Top up berhasil. Saldo {username} bertambah menjadi {user[i+1][5] + topup}')
                    user[i+1][5]= user[i+1][5]+ topup
    else:
        print(f'Username {username} tidak ditemukan.')
