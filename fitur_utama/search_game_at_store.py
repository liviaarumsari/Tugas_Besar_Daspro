from modul_fungsi.array_function import panjang
from modul_fungsi.array_function import print_data

def search_game_at_store (data):
    if currentuser = False:
        print("Maaf, anda harus login terlebih dahulu untuk megirim perintah selain 'login")
    else:
        idgame= input("Masukkan ID Game: ")
        nama = input("Masukkan Nama Game : ")
        harga = input("Masukkan Harga Game : ")
        kategori = input("Masukkan Kategori Game : ")
        tahun = input("Masukkan Tahun Rilis Game : ")

        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        g=0
        h=0
        i=0
        j=0
        k=0
        l=0
        m=0
        n=0
        o=0
        p=0
        q=0
        r=0
        s=0
        t=0
        u=0
        v=0
        w=0
        x=0
        y=0
        z=0
        aa=0
        ab=0
        ac=0
        ad=0
        ae=0
        af=0

        if idgame=="" and nama=="" and harga=="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                a+=1
                fin=print_data(arr[i])
                print(fin)
        elif idgame!="" and nama=="" and harga=="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame:
                    b+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame=="" and nama!="" and harga=="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][1]==nama:
                    c+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame=="" and nama=="" and harga!="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][4]==harga:
                    d+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame=="" and nama=="" and harga=="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][2]==kategori:
                    e+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame=="" and nama=="" and harga=="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][3]==tahun:
                    f+=1
                    fin=print_data(arr[i])
                    print(fin)
                
        elif idgame!="" and nama!="" and harga=="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama:
                    g+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame!="" and nama=="" and harga!="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][4]==harga:
                    h+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame!="" and nama=="" and harga=="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][2]==kategori:
                    i+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame!="" and nama=="" and harga=="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][3]==tahun:
                    j+=1
                    fin=print_data(arr[i])
                    print(fin)

        elif idgame=="" and nama!="" and harga!="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][4]==harga:
                    k+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame=="" and nama!="" and harga=="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][2]==kategori:
                    l+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame=="" and nama!="" and harga=="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][3]==tahun:
                    m+=1
                    fin=print_data(arr[i])
                    print(fin)
                    
        elif idgame=="" and nama=="" and harga!="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][2] == kategori and data[i][4]==harga:
                    n+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame=="" and nama=="" and harga!="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][3] == tahun and data[i][4]==harga:
                    o+=1
                    fin=print_data(arr[i])
                    print(fin)
                    
        elif idgame=="" and nama=="" and harga=="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][2] == kategori and data[i][3]==tahun:
                    p+=1
                    fin=print_data(arr[i])
                    print(fin)


        elif idgame!="" and nama!="" and harga!="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga:
                    q+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame!="" and nama!="" and harga=="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][2]==kategori:
                    r+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame!="" and nama!="" and harga=="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][3]==tahun:
                    s+=1
                    fin=print_data(arr[i])
                    print(fin)
                    
        elif idgame!="" and nama=="" and harga!="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][2]==kategori and data[i][4]==harga:
                    t+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame!="" and nama=="" and harga!="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][3]==tahun and data[i][4]==harga:
                    u+=1
                    fin=print_data(arr[i])
                    print(fin)

        elif idgame!="" and nama=="" and harga=="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][2]==kategori and data[i][3]==tahun:
                    v+=1
                    fin=print_data(arr[i])
                    print(fin)

        elif idgame=="" and nama!="" and harga!="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][4]==harga and data[i][2]==kategori:
                    w+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame=="" and nama!="" and harga!="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][4]==harga and data[i][3]==tahun:
                    x+=1
                    fin=print_data(arr[i])
                    print(fin)
                    
        elif idgame=="" and nama!="" and harga=="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][3]==tahun and data[i][2]==kategori:
                    y+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame=="" and nama=="" and harga!="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][3] == tahun and data[i][4]==harga and data[i][2]==kategori:
                    z+=1
                    fin=print_data(arr[i])
                    print(fin)

        elif idgame!="" and nama!="" and harga!="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga and data[i][2]==kategori:
                    aa+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame!="" and nama!="" and harga!="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga and data[i][3]==tahun:
                    ab+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame!="" and nama!="" and harga=="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][3]==tahun and data[i][2]==kategori:
                    ac+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame!="" and nama=="" and harga!="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][3]==tahun and data[i][4]==harga and data[i][2]==kategori:
                    ad+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame=="" and nama!="" and harga!="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][3] == tahun and data[i][1]==nama and data[i][4]==harga and data[i][2]==kategori:
                    ae+=1
                    fin=print_data(arr[i])
                    print(fin)
        elif idgame!="" and nama!="" and harga!="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga and data[i][2]==kategori and data[i][3]==tahun:
                    af+=1
                    fin=print_data(arr[i])
                    print(fin)
