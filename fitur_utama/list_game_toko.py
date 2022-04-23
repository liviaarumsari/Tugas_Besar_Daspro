from modul_fungsi.array_function import panjang
from modul_fungsi.array_function import print_data

def sortTahunNaik(data, ind=3):
    for i in range(panjang(data)):
        for j in range(1,(panjang(data)-1-i)):
            if int(data[j][ind]) > int(data[j+1][ind]):
                data[j],data[j+1] = data[j+1], data[j]
    return data

def sortTahunTurun(data, ind=3):
    for i in range(panjang(data)):
        for j in range(1,(panjang(data)-1-i)):
            if int(data[j+1][ind]) > int(data[j][ind]):
                data[j],data[j+1] = data[j+1], data[j]
    return data

def sortHargaNaik(data, ind=4):
    for i in range(panjang(data)):
        for j in range(1,(panjang(data)-1-i)):
            if int(data[j][ind]) > int(data[j+1][ind]):
                data[j],data[j+1] = data[j+1], data[j]
    return data

def sortHargaTurun(data, ind=4):
    for i in range(panjang(data)):
        for j in range(1,(panjang(data)-1-i)):
            if int(data[j+1][ind]) > int(data[j][ind]):
                data[j],data[j+1] = data[j+1], data[j]
    return data

def sortID(data, ind=0):
    for i in range(panjang(data)):
        for j in range(1,(panjang(data)-1-i)):
            if int(data[j][ind]) > int(data[j+1][ind]):
                data[j],data[j+1] = data[j+1], data[j]
    return data

def list_game_toko (data):
    sort=str(input("Skema sorting : "))
    
    if sort=="tahun-":
        x=sortTahunTurun(data, ind=3)
        y=print_data(x)
        print(y)
        
    elif sort=="tahun+":
        x=sortTahunNaik(data, ind=3)
        y=print_data(x)
        print(y)
        
    elif sort=="harga-":
        x=sortHargaTurun(data, ind=4)
        y=print_data(x)
        print(y)
        
    elif sort=="harga+":
        x=sortHargaNaik(data, ind=4)
        y=print_data(x)
        print(y)
        
    elif sort=="":
        x=sortID(data, ind=0)
        y=print_data(x)
        print(y)

    else:
        print("Skema sorting tidak valid!")
        

                
