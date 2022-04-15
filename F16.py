import os
def isEmpty(n):
    n != ''
    return n

def panjang(arr):
    i = 0
    for c in arr:
        i += 1
    return i
def save_data(data, nama_folder, nama_file):
    file=open("./%s/%s.csv" % (nama_folder, nama_file), "w")    
    for i in range(panjang(data)):
        for j in range(panjang(data[0])):
            if (j == panjang(data[0])-1):
                file.write(str(data[i][j]))
            else:
                file.write(str(data[i][j]) + ";")
        file.write("\n")
    file.close()

def save(kepemilikan,user,game,riwayat):

    kepemilikan= [['G010','002'],['G002','002'],['G033','002']]
    user=[['001','mikdar','ghaylan','1234','user',30000],['002','zenn','fatih','4321','user',20000]]
    game=[['G001','pyhton','action','2015',25000,25],['G002','dota','action','2015',20000,2]]
    riwayat=[['G001','python','001',2022],['G002','dota','001',2021],['G001','python','002',2022]]


    folder=input('Masukkan nama folder penyimpanan: ')
    while not isEmpty(folder):
        folder=input('Masukkan nama folder penyimpanan: ')
    path=os.path.join('D:/tubes daspro/Tugas_Besar_Daspro-main/',folder)

    if os.path.isdir(path)==False:
        os.mkdir(path)
        save_data(game,folder,'game')
        save_data(user,folder,'user')
        save_data(riwayat,folder,'riwayat')
        save_data(kepemilikan,folder,'kepemilikan')
        print(f'Data telah disimpan pada folder {folder}')
    else:
        save_data(game,folder,'game')
        save_data(user,folder,'user')
        save_data(riwayat,folder,'riwayat')
        save_data(kepemilikan,folder,'kepemilikan')
        print(f'Data telah disimpan pada folder {folder}')
















print('saving...')
