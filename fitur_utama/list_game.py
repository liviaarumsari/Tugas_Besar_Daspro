from modul_fungsi.array_function import print_data, panjang, buat_data_baru
from modul_fungsi.data_function import data_game_user

def list_game(username, user, kepemilikan, game):
    # Membuat array game ID yang dimiliki user
    game_user = data_game_user(username, user, kepemilikan)

    if (panjang(game_user) == 0):
        print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")
    else:
        # Menyusun data game yang hanya dimiliki user
        data_g_user = []
        for i in range (panjang(game_user)):
            for j in range (panjang(game)):
                if (game_user[i] == game[j][0]):
                    data_g_user += [game[j]]

        # Print data game
        print("Daftar game: ")
        data_baru = buat_data_baru(data_g_user,[5])
        print_data(data_baru)



