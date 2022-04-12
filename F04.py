def isEmpty(n):
    n != ''
    return n


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
        arr=[namaGame, kategori, tahunRilis, harga, stok]
        print(f'Selamat! Berhasil menambahkan game {namaGame}.')
        file=open('game.csv', 'w')
        for element in arr:
            file.write(element+' ')
        file.write('\n')
        file.close()
        break

