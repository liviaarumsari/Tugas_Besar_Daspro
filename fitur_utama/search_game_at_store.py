from modul_fungsi.array_function import panjang
from modul_fungsi.array_function import print_data

def search_game_at_store (data):
    idgame= input("Masukkan ID Game: ")
    nama = input("Masukkan Nama Game : ")
    harga = input("Masukkan Harga Game : ")
    kategori = input("Masukkan Kategori Game : ")
    tahun = input("Masukkan Tahun Rilis Game : ")

    fin = []
    if idgame=="" and nama=="" and harga=="" and kategori=="" and tahun=="":
        for i in range(panjang(data)):
            fin = data
    elif idgame!="" and nama=="" and harga=="" and kategori=="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][0] == idgame:
                fin += [data[i]]             
    elif idgame=="" and nama!="" and harga=="" and kategori=="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][1]==nama:
                fin += [data[i]]
    elif idgame=="" and nama=="" and harga!="" and kategori=="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][4]==harga:
                fin=print_data(data[i])
                print(fin)
    elif idgame=="" and nama=="" and harga=="" and kategori!="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][2]==kategori:
                fin=print_data(data[i])
                print(fin)
    elif idgame=="" and nama=="" and harga=="" and kategori=="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][3]==tahun:
                fin=print_data(data[i])
                print(fin)
            
    elif idgame!="" and nama!="" and harga=="" and kategori=="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][1]==nama:
                fin=print_data(data[i])
                print(fin)
    elif idgame!="" and nama=="" and harga!="" and kategori=="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][4]==harga:
                fin=print_data(data[i])
                print(fin)
    elif idgame!="" and nama=="" and harga=="" and kategori!="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][2]==kategori:
                i+=1
                fin=print_data(data[i])
                print(fin)
    elif idgame!="" and nama=="" and harga=="" and kategori=="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][3]==tahun:
                fin=print_data(data[i])
                print(fin)

    elif idgame=="" and nama!="" and harga!="" and kategori=="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][1] == nama and data[i][4]==harga:
                fin=print_data(data[i])
                print(fin)
    elif idgame=="" and nama!="" and harga=="" and kategori!="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][1] == nama and data[i][2]==kategori:
                fin=print_data(data[i])
                print(fin)
    elif idgame=="" and nama!="" and harga=="" and kategori=="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][1] == nama and data[i][3]==tahun:
                fin=print_data(data[i])
                print(fin)
                
    elif idgame=="" and nama=="" and harga!="" and kategori!="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][2] == kategori and data[i][4]==harga:
                fin=print_data(data[i])
                print(fin)
    elif idgame=="" and nama=="" and harga!="" and kategori=="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][3] == tahun and data[i][4]==harga:
                fin=print_data(data[i])
                print(fin)
                
    elif idgame=="" and nama=="" and harga=="" and kategori!="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][2] == kategori and data[i][3]==tahun:
                fin=print_data(data[i])
                print(fin)


    elif idgame!="" and nama!="" and harga!="" and kategori=="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga:
                fin=print_data(data[i])
                print(fin)
    elif idgame!="" and nama!="" and harga=="" and kategori!="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][1]==nama and data[i][2]==kategori:
                fin=print_data(data[i])
                print(fin)
    elif idgame!="" and nama!="" and harga=="" and kategori=="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][1]==nama and data[i][3]==tahun:
                fin=print_data(data[i])
                print(fin)
                
    elif idgame!="" and nama=="" and harga!="" and kategori!="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][2]==kategori and data[i][4]==harga:
                fin=print_data(data[i])
                print(fin)
    elif idgame!="" and nama=="" and harga!="" and kategori=="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][3]==tahun and data[i][4]==harga:
                fin=print_data(data[i])
                print(fin)

    elif idgame!="" and nama=="" and harga=="" and kategori!="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][2]==kategori and data[i][3]==tahun:
                fin=print_data(data[i])
                print(fin)

    elif idgame=="" and nama!="" and harga!="" and kategori!="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][1] == nama and data[i][4]==harga and data[i][2]==kategori:
                fin=print_data(data[i])
                print(fin)
    elif idgame=="" and nama!="" and harga!="" and kategori=="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][1] == nama and data[i][4]==harga and data[i][3]==tahun:
                fin=print_data(data[i])
                print(fin)
                
    elif idgame=="" and nama!="" and harga=="" and kategori!="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][1] == nama and data[i][3]==tahun and data[i][2]==kategori:
                fin=print_data(data[i])
                print(fin)
    elif idgame=="" and nama=="" and harga!="" and kategori!="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][3] == tahun and data[i][4]==harga and data[i][2]==kategori:
                fin=print_data(data[i])
                print(fin)

    elif idgame!="" and nama!="" and harga!="" and kategori!="" and tahun=="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga and data[i][2]==kategori:
                fin=print_data(data[i])
                print(fin)
    elif idgame!="" and nama!="" and harga!="" and kategori=="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga and data[i][3]==tahun:
                fin=print_data(data[i])
                print(fin)
    elif idgame!="" and nama!="" and harga=="" and kategori!="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][1]==nama and data[i][3]==tahun and data[i][2]==kategori:
                fin=print_data(data[i])
                print(fin)
    elif idgame!="" and nama=="" and harga!="" and kategori!="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][3]==tahun and data[i][4]==harga and data[i][2]==kategori:
                fin=print_data(data[i])
                print(fin)
    elif idgame=="" and nama!="" and harga!="" and kategori!="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][3] == tahun and data[i][1]==nama and data[i][4]==harga and data[i][2]==kategori:
                fin=print_data(data[i])
                print(fin)
    elif idgame!="" and nama!="" and harga!="" and kategori!="" and tahun!="":
        for i in range(panjang(data)):
            if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga and data[i][2]==kategori and data[i][3]==tahun:
                fin=print_data(data[i])
                print(fin)

    print("Daftar game pada toko yang memenuhi kriteria: ")
    print_data(fin)