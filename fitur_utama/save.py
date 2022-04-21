import os
def isEmpty(n):
    if n != '':
        return n

def panjang(arr):
    i = 0
    for c in arr:
        i += 1
    return i
# Matriks to CSV
def save_data(data, nama_folder, nama_file):
    file=open(f"{nama_folder}"+f"/{nama_file}.csv", "w")    
    for i in range(panjang(data)):
        for j in range(panjang(data[0])):
            if (j == panjang(data[0])-1):
                file.write(str(data[i][j])+'\n')
            else:
                file.write(str(data[i][j]+';'))
    file.close()

def removeRow(data):
    data_baru=[]
    for i in range(panjang(data)):
        if data[i]!=['']:
            data_baru=data_baru+[data[i]]
    return data_baru

def save(kepemilikan,user,game,riwayat):
    kepemilikan=removeRow(kepemilikan)
    user=removeRow(user)
    riwayat=removeRow(riwayat)
    game=removeRow(game)

    folder=input('Masukkan nama folder penyimpanan: ')
    while not isEmpty(folder):
        folder=input('Masukkan nama folder penyimpanan: ')

    if not os.path.exists(folder):
        os.makedirs(folder)

    save_data(game,folder,'game')
    save_data(riwayat,folder,'riwayat')
    save_data(kepemilikan,folder,'kepemilikan')
    save_data(user,folder,'user')
    print('saving...')
    print(f'Data telah disimpan pada folder {folder}')

















