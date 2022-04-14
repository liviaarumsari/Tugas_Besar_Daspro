from modul_fungsi.array_function import panjang

def search_game_at_store (data):
    if currentuser = False:
        print("Anda belum login. Login terlebih dahulu.")
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
                print (f'{a}.' + arr[i])
        elif idgame!="" and nama=="" and harga=="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame:
                    b+=1
                    print (f'{b}.' + arr[i])
        elif idgame=="" and nama!="" and harga=="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][1]==nama:
                    c+=1
                    print (f'{c}.' + arr[i])
        elif idgame=="" and nama=="" and harga!="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][4]==harga:
                    d+=1
                    print (f'{d}.' + arr[i])
        elif idgame=="" and nama=="" and harga=="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][2]==kategori:
                    e+=1
                    print (f'{e}.' + arr[i])
        elif idgame=="" and nama=="" and harga=="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][3]==tahun:
                    f+=1
                    print (f'{f}.' + arr[i])
                
        elif idgame!="" and nama!="" and harga=="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama:
                    g+=1
                    print (f'{g}.' + arr[i])
        elif idgame!="" and nama=="" and harga!="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][4]==harga:
                    h+=1
                    print (f'{h}.' + arr[i])
        elif idgame!="" and nama=="" and harga=="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][2]==kategori:
                    i+=1
                    print (f'{i}.' + arr[i])
        elif idgame!="" and nama=="" and harga=="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][3]==tahun:
                    j+=1
                    print (f'{j}.' + arr[i])

        elif idgame=="" and nama!="" and harga!="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][4]==harga:
                    k+=1
                    print (f'{k}.' + arr[i])
        elif idgame=="" and nama!="" and harga=="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][2]==kategori:
                    l+=1
                    print (f'{l}.' + arr[i])
        elif idgame=="" and nama!="" and harga=="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][3]==tahun:
                    m+=1
                    print (f'{m}.' + arr[i])
                    
        elif idgame=="" and nama=="" and harga!="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][2] == kategori and data[i][4]==harga:
                    n+=1
                    print (f'{n}.' + arr[i])
        elif idgame=="" and nama=="" and harga!="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][3] == tahun and data[i][4]==harga:
                    o+=1
                    print (f'{o}.' + arr[i])
                    
        elif idgame=="" and nama=="" and harga=="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][2] == kategori and data[i][3]==tahun:
                    p+=1
                    print (f'{p}.' + arr[i])


        elif idgame!="" and nama!="" and harga!="" and kategori=="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga:
                    q+=1
                    print (f'{q}.' + arr[i])
        elif idgame!="" and nama!="" and harga=="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][2]==kategori:
                    r+=1
                    print (f'{r}.' + arr[i])
        elif idgame!="" and nama!="" and harga=="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][3]==tahun:
                    s+=1
                    print (f'{s}.' + arr[i])
                    
        elif idgame!="" and nama=="" and harga!="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][2]==kategori and data[i][4]==harga:
                    t+=1
                    print (f'{t}.' + arr[i])
        elif idgame!="" and nama=="" and harga!="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][3]==tahun and data[i][4]==harga:
                    u+=1
                    print (f'{u}.' + arr[i])

        elif idgame!="" and nama=="" and harga=="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][2]==kategori and data[i][3]==tahun:
                    v+=1
                    print (f'{v}.' + arr[i])

        elif idgame=="" and nama!="" and harga!="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][4]==harga and data[i][2]==kategori:
                    w+=1
                    print (f'{w}.' + arr[i])
        elif idgame=="" and nama!="" and harga!="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][4]==harga and data[i][3]==tahun:
                    x+=1
                    print (f'{x}.' + arr[i])
                    
        elif idgame=="" and nama!="" and harga=="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][1] == nama and data[i][3]==tahun and data[i][2]==kategori:
                    y+=1
                    print (f'{y}.' + arr[i])
        elif idgame=="" and nama=="" and harga!="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][3] == tahun and data[i][4]==harga and data[i][2]==kategori:
                    z+=1
                    print (f'{z}.' + arr[i])

        elif idgame!="" and nama!="" and harga!="" and kategori!="" and tahun=="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga and data[i][2]==kategori:
                    aa+=1
                    print (f'{aa}.' + arr[i])
        elif idgame!="" and nama!="" and harga!="" and kategori=="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga and data[i][3]==tahun:
                    ab+=1
                    print (f'{ab}.' + arr[i])
        elif idgame!="" and nama!="" and harga=="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][3]==tahun and data[i][2]==kategori:
                    ac+=1
                    print (f'{ac}.' + arr[i])
        elif idgame!="" and nama=="" and harga!="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][3]==tahun and data[i][4]==harga and data[i][2]==kategori:
                    ad+=1
                    print (f'{ad}.' + arr[i])
        elif idgame=="" and nama!="" and harga!="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][3] == tahun and data[i][1]==nama and data[i][4]==harga and data[i][2]==kategori:
                    ae+=1
                    print (f'{ae}.' + arr[i])
        elif idgame!="" and nama!="" and harga!="" and kategori!="" and tahun!="":
            for i in range(panjang(data)):
                if data[i][0] == idgame and data[i][1]==nama and data[i][4]==harga and data[i][2]==kategori and data[i][3]==tahun:
                    af+=1
                    print (f'{af}.' + arr[i])
