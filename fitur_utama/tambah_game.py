from modul_fungsi.array_function import panjang
from modul_fungsi.data_function import gameID, validasi_harga, validasi_tahun

def isEmpty(n):
    if n == '':
        return False
    else:
        return n

def removeRow(data):
    data_baru=[]
    for i in range(panjang(data)):
        if  data[i]!=['']:
            data_baru=data_baru+[data[i]]
        elif data[i]==['','','','']:
            data_baru=data_baru+[data[i]]
    return data_baru

def tambah_game(data):
    data=removeRow(data)
    namaGame=input('Masukkan nama game: ')
    kategori=input('Masukkan kategori: ')
    tahunRilis=(input('Masukkan tahun rilis: '))
    harga=(input('Masukkan harga: '))
    stok=(input('Masukkan stok awal: '))

    while True: 
        if not isEmpty(namaGame) or not isEmpty(kategori)or not isEmpty(tahunRilis) or not isEmpty(harga) or not isEmpty(stok):
            print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.')
            namaGame=input('Masukkan nama game: ')
            kategori=input('Masukkan kategori: ')
            tahunRilis=(input('Masukkan tahun rilis: '))
            harga=(input('Masukkan harga: '))
            stok=(input('Masukkan stok awal: '))
        else:
            tahunRilis = validasi_tahun(tahunRilis)
            harga = validasi_harga(harga, "Masukan harga tidak valid. Silahkan ulangi pengisian harga", "Masukkan harga: ")
            arr=[gameID(panjang(data)),namaGame,kategori,tahunRilis,harga,stok]
            data = data + [arr]
            print(f'Selamat! Berhasil menambahkan game {namaGame}.')       
            return(data)

