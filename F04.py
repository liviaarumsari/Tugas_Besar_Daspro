from modul_fungsi.array_function import panjang

def isEmpty(n):
    n != ''
    return n

data= [['G1','dota','moba','2002','300','20']]

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
        arr=['G'+str(panjang(data)+1),namaGame, kategori, tahunRilis, harga, stok]
        print(f'Selamat! Berhasil menambahkan game {namaGame}.')
        file=open('game.csv', 'w')     #gatau cara nambahin ke csvnya, jadi sementara jadiin matriks dlu
        for element in arr:       
            file.write(element+' ')
        file.write('\n')
        file.close()
        data=data + [arr]
        print(data)
        break

print(panjang(data))