from modul_fungsi.array_function import panjang

def search_my_game (arr):  # Hanya untuk User
    Game_Id = input("Masukkan ID Game : ")
    year = input("Masukkan Tahun Rilis Game : ")

    j = 0
    k = 0
    l = 0

    if Game_Id != "" and year == "":
        for i in range (panjang(arr)):              #Range blm bener harusnya number of row
            if arr[i][0] == Game_Id:
                j += 1
                return print(f'{j}.' + arr[i])
    elif Game_Id == "" and year != "":
        for i in range(panjang(arr)):               #Range blm bener harusnya number of row
            if arr[i][3] == year:
                k += 1
                return print(f'{k}.' + arr[i])
    elif Game_Id != 0 and year != 0:
        for i in range(panjang(arr)):               #Range blm bener harusnya number of row
            if arr[i][3] == year and arr[i][0] == Game_Id:
                l += 1
                return print(f'{l}.' + arr[i])          #kemungkinan cuma print 1, coba hapus return
