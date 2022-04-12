from modul_fungsi.array_function import panjang

def ada(user,username,kolom):
    i=0
    while i<panjang(user):
        if user[i][kolom]==username:
            break
        return True

username=input('Masukkan username: ')

topup=int(input('Masukkan saldo: '))

user=[['001','mikdar','ghaylan','1234','user',30000],['002','zenn','fatih','4321','user',20000],['003','owo','alif','2323','user',40000]]

if ada(user,username,1)==False:
    print(f'Username {username} tidak ditemukan.')


for i in range (panjang(user)):
    if user[i][1] == username:
        if (user[i][5] + topup)<0:
            print('Masukan tidak valid')
        else:
            print(f'Top up berhasil. Saldo {username} bertambah menjadi {user[i][5] + topup}')
            user[i][5]= user[i][5]+ topup

print(user)
