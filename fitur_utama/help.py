
def help(currentuser, role):
    if currentuser == True:     # Lihat di fungsi login()
        if (role == "admin"):  
            print('=================== Help ===================')
            print('register                 |  Mendaftarkan pengguna baru')
            print('login                    |  Untuk masuk/login kedalam sistem')
            print('tambah_game              |  Menambahkan game baru kedalam sistem')
            print('ubah_game                |  Mengubah Spesifikasi dari game yang sudah ada')
            print('ubah_stock               |  Menambah atau mengurangi jumlah stok game')
            print('list_game_toko           |  Menampilkan list game yang ada di toko')
            print('search_game_at_store     |  Mencari Game di toko')
            print('topup                    |  Menambahkan atau mengurangi saldo kepada User')
            print('help                     |  Menampilkan list perintah yang dapat dimasukkan')
            print('load                     |  Melakukan loading kedalam sistem')
            print('save                     |  Menyimpan data ke dalam file setelah melakukan perubahan')
            print('exit                     |  Keluar aplikasi')

        else:
            print('=================== Help ===================')
            print('list_game_toko           |  Menampilkan list game yang ada di toko')
            print('buy_game                 |  Membeli game yang terdapat di toko')
            print('list_game                |  Menampilkan daftar game yang dimiliki')
            print('search_my_game           |  Mencari Game yang dimiliki pengguna')
            print('search_game_at_store     |  Mencari Game di toko')
            print('riwayat                  |  Menampilkan riwayat pembelian user')
            print('help                     |  Menampilkan list perintah yang dapat dimasukkan')
            print('load                     |  Melakukan loading kedalam sistem')
            print('save                     |  Menyimpan data ke dalam file setelah melakukan perubahan')
            print('exit                     |  Keluar aplikasi')
    else:
        print('=================== Help ===================')
        print('login    |  Untuk masuk/login kedalam sistem')
        print('help     |  Menampilkan list perintah yang dapat dimasukkan')
