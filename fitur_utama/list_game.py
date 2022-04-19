from modul_fungsi.array_function import print_data, panjang, buat_data_baru
from modul_fungsi.data_function import getuserID

def list_game(username, user, kepemilikan, game):
    game_user = []
    id_user = getuserID(user, username)
    for i in range (panjang(kepemilikan)):
        if (kepemilikan[i][1] == id_user):
            game_id = kepemilikan[i][0]
            game_user += [game_id]

    if (panjang(game_user) == 0):
        print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")
    else:
        data_game_user = []
        for i in range (panjang(game_user)):
            for j in range (panjang(game)):
                if (game_user[i] == game[j][0]):
                    data_game_user += [game[j]]

        print("Daftar game: ")
        data_baru = buat_data_baru(data_game_user,[5])
        print_data(data_baru)



