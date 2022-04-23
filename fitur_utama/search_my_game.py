from modul_fungsi.array_function import panjang, formatCariGame
from modul_fungsi.data_function import Exist, data_game_user

def game_owned(game_id, data):
    for i in range(panjang(data)):
        if data[i] == game_id:
            return True
    return False

def search_my_game(username, user, kepemilikan, game):
    
    Game_Id = input("Masukkan ID Game : ")
    year = input("Masukkan Tahun Rilis Game : ")

    game_user = data_game_user(username, user, kepemilikan)

    filtered_arr = []
    if Game_Id != "" and year == "":                            # Hanya input Game id 
        if Exist(game, Game_Id, 0) == True:                     # Cek apakah game ada di toko
            if game_owned(Game_Id, game_user) == True:          # Cek apakah user punya game itu
                for i in range(panjang(game)):
                    if game[i][0] == Game_Id:      
                        filtered_arr += [game[i]]               # Buat array yang sudah terfilter sesuai kriteria input user 


    elif Game_Id == "" and year != "":                          # Hanya input tahun
        if Exist(game, year, 3) == True:
            temp_arr = []                                       # Array berisi spek dengan tahun tertentu
            for i in range(panjang(game)):
                if game[i][3] == year:
                    temp_arr += [game[i]]
                    
            if not(temp_arr == []):                                         # Cek apakah game ada di toko
                for i in range(panjang(temp_arr)):
                    if game_owned(temp_arr[i][0], game_user) == True:       # Cek apakah user punya game itu     
                        filtered_arr += [temp_arr[i]]                           # Buat array yang sudah terfilter sesuai kriteria input user


    elif Game_Id != "" and year != "":                                          # input Game id + tahun
        if Exist(game, year, 3) == True and Exist(game, Game_Id, 0) == True:
            temp_arr1 = []                                                      # Array berisi spek dengan tahun tertentu
            temp_arr2 = []                                                      # Array berisi spek dengan tahun dan game id tertentu

            for i in range(panjang(game)):
                if game[i][3] == year:
                    temp_arr1 += [game[i]]
            
            for i in range(panjang(temp_arr1)):
                if temp_arr1[i][0] == Game_Id:
                    temp_arr2 += [temp_arr1[i]]

            if not(temp_arr2 == []):                                            # Cek apakah game ada di toko
                for i in range(panjang(temp_arr2)):
                    if game_owned(temp_arr2[i][0], game_user) == True:          # Cek apakah user punya game itu     
                        filtered_arr += [temp_arr2[i]]                          # Buat array yang sudah terfilter sesuai kriteria input user


    if filtered_arr == []:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:
        print(formatCariGame(filtered_arr))
