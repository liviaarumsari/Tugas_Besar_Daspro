from modul_fungsi.array_function import panjang
from modul_fungsi.array_function import print_data

def slice(str,first,last):
    if(
        first<0
        or last >= panjang(str)
        or last<0
        or first >= panjang(str)
        or first>last
    ):
        return ""

    ans=""
    for i in range(first,last+1):
        ans+=str[i]
    return ans

def intID(idgame):
    if panjang(idgame)==0:
        return 0

    int_start=-1
    found=False

    for i in range(len(str(idgame))):
        c=idgame[i]
        int_start+=1
        if c>="0" and c<="9":
            found=True
            continue
        
    if not found:
        return 0
    else:
        return(int(slice(idgame,int_start, panjang(idgame)-1)))

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
            if intID(data[j][ind]) > intID(data[j+1][ind]):
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
        

                
