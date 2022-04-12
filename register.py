from modul_fungsi.data_function import UserValid
from modul_fungsi.data_function import Exist
from modul_fungsi.array_function import panjang
from modul_fungsi.data_function import userID


def register(arr):
    new_nama = input("Masukkan Nama: ")
    new_username = input("Masukkan Username: ")
    while UserValid(new_username) == False:
        new_username = input("Masukkan Username: ")

    new_password = input("Masukkan Password: ")

    if Exist(arr,new_username,1) == True:
        return "Username {} sudah terpakai, silakan menggunakan username lain.".format(new_username)
    else: 
        data_f = arr + [[f'{userID(panjang(arr))+1}',f'{new_username}',f'{new_nama}',f'{new_password}','user','0']]
        return data_f
# Baru nambahin data baru ke array belum update csv
