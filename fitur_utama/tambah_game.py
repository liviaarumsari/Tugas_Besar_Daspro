from modul_fungsi.array_function import panjang
from modul_fungsi.csv_function import save_data
from modul_fungsi.data_function import gameID

def isEmpty(n):
    n != ''
    return n

data= [['G1','dota','moba','2002','300','20']]

def tambah_game(data):
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
            arr=[gameID(panjang(data)+1),namaGame, kategori, tahunRilis, harga, stok]
            data_baru = data + [arr]
            print(f'Selamat! Berhasil menambahkan game {namaGame}.')       
            return(data_baru)

