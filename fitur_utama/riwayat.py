from modul_fungsi.array_function import print_data
from modul_fungsi.array_function import panjang
from modul_fungsi.array_function import buat_data_baru
from modul_fungsi.data_function import data_game_user

def riwayat(username, user, kepemilikan, riwayat):
    # Membuat array game ID yang dimiliki user
    game_user = data_game_user(username, user, kepemilikan)

    if (panjang(game_user) == 0):
        print("Maaf, kamu tidak memiliki game. Ketik perintah buy_game untuk membeli.")
    else:
        riwayat_user = []
        for i in range (panjang(game_user)):
            for j in range (panjang(riwayat)):
                if (game_user[i] == riwayat[j][0]):
                    riwayat_user += [riwayat[j]]

        if (panjang(riwayat_user) == 0):
            print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah buy_game untuk membeli.")
        else:
            print("Daftar game: ")
            data_baru = buat_data_baru(riwayat_user,[3])
            print_data(data_baru)