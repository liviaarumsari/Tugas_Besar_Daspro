currentuser = False
while True:
    perintah=input()
    if perintah=="login":
        login(data_f)
    elif perintah=="tambah_game":
        tambah_game(data, nama_folder)
    elif perintah=="ubah_game":
        ubah_game(data)
    elif perintah=="ubah_stok":
        ubah_stock(arr)
    elif perintah=="list_game_toko":
        list_game_toko(data)
    elif perintah=="buy_game":
        beli_game(kepemilikan,user,game,riwayat)
    elif perintah=="list_game":
        list_game(data)
    elif perintah=="search_my_game":
        search_my_game(arr)
    elif perintah=="search_game_at_store":
        search_game_at_store(data)
    elif perintah=="topup":
        tambah_saldo(user)
    elif perintah=="riwayat":
        riwayat(data)
    elif perintah=="help":
        help()
    elif perintah=="save":
        save(kepemilikan,user,game,riwayat)
    elif perintah=="exit":
        exit()
