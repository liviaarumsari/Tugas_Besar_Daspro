from modul_fungsi.array_function import print_data
from modul_fungsi.array_function import panjang
from modul_fungsi.array_function import buat_data_baru

def riwayat(data):
    if (panjang(data) == 0):
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else:
        data_baru = buat_data_baru(data,[3])
        print_data(data_baru)