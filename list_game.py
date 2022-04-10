from modul_fungsi.array_function import print_data
from modul_fungsi.array_function import panjang
from modul_fungsi.array_function import buat_data_baru

def list_game(data):
    if (panjang(data) == 0):
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        data_baru = buat_data_baru(data,[5])
        print_data(data_baru)


