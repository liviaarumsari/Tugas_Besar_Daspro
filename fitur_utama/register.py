from modul_fungsi.data_function import UserValid
from modul_fungsi.data_function import Exist
from modul_fungsi.array_function import panjang
from modul_fungsi.data_function import userID

def removeRow(data):
    data_baru=[]
    for i in range(panjang(data)):
        if  data[i]!=['']:
            data_baru=data_baru+[data[i]]
        elif data[i]==['','','','']:
            data_baru=data_baru+[data[i]]
    return data_baru

def isEmpty(n):
    if n == '':
        return False
    else:
        return n

def register(data):
    data = removeRow(data)
    new_nama = input("Masukkan Nama: ")
    new_username = input("Masukkan Username: ")
    while UserValid(new_username) == False:
        print('Username hanya boleh memuat a-z , "-" , "_" )')
        new_username = input("Masukkan Username: ")
    new_password = input("Masukkan Password: ")


    while True: 
        if not isEmpty(new_nama) or not isEmpty(new_username) or not isEmpty(new_password):
            print('Mohon masukkan semua data yang diperlukan.')
            new_nama = input("Masukkan Nama: ")
            new_username = input("Masukkan Username: ")
            while UserValid(new_username) == False:
                print('Username hanya boleh memuat a-z , "-" , "_" )')
                new_username = input("Masukkan Username: ")
            new_password = input("Masukkan Password: ")

        else:
            if Exist(data,new_username,1) == True:
                print("Username {} sudah terpakai, silakan menggunakan username lain.".format(new_username))
            else: 
                arr = [userID(panjang(data)), new_username, new_nama, new_password, 'user', '0']
                data = data + [arr]
                print(f'Selamat! Berhasil menambahkan user {new_nama}.')
                return (data)
