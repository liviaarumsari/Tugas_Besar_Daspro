currentuser=True

def search_game_at_store(data):
    if currentuser == False:
        print("Maaf, anda harus login terlebih dahulu untuk megirim perintah selain 'login")
    else:
        idgame= input("Masukkan ID Game: ")
        nama = input("Masukkan Nama Game : ")
        harga = input("Masukkan Harga Game : ")
        kategori = input("Masukkan Kategori Game : ")
        tahun = input("Masukkan Tahun Rilis Game : ")

        count = 1
        if idgame =='' and nama =='' and harga =='' and tahun =='' and kategori =='':
           for row in data:
                print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                count = count+1
        else:
            print("Daftar game pada toko yang memenuhi kriteria:")
            if idgame != '' and nama == '' and harga == '' and tahun == '' and kategori == '':
                for row in data:
                    if idgame == row[0]:
                        searchID = f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} "
                        print (searchID)
                        count = count+1   

            elif idgame == '' and nama != '' and harga == '' and tahun == '' and kategori == '':
                for row in data:
                    if nama == row[1]:
                        searchNama = f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} "
                        print (searchNama)
                        count = count+1  

            elif idgame == '' and nama == '' and harga != '' and tahun == '' and kategori == '':
                for row in data:
                    if harga == row[4]:
                        searchHarga= f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} "
                        print (searchHarga)
                        count = count+1  
    
            elif idgame =='' and nama =='' and tahun !='' and kategori =='' and harga =='':
                for row in data:
                    if tahun == row[3]:
                        searchTahun = f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} "
                        print (searchTahun) 
                        count = count+1
        
            elif idgame =='' and nama=='' and tahun =='' and kategori!='' and harga=='':
                for row in data:
                    if kategori == row[2]:
                        searchKategori = f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} "
                        print (searchKategori) 
                        count = count+1
    
            elif idgame !='' and nama !='' and tahun =='' and kategori =='' and harga=='':
                for row in data:
                    if idgame==row[0]:
                        if nama == row[1]:
                            print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                            count = count+1

            elif idgame == '' and nama!='' and kategori !='' and tahun =='' and harga =='':
                for row in data:
                    if nama==row[1]:
                        if kategori == row[2]:
                            print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                            count = count +1

            elif idgame == '' and nama =='' and kategori !=''and tahun !='' and harga=='':
                for row in data:
                    if kategori ==row[2]:
                        if tahun ==row[3]:
                            print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                            count = count +1

            elif idgame =='' and nama =='' and kategori =='' and tahun !='' and harga!='':
                for row in data:
                    if tahun == row[3]:
                        if harga == row[4]:
                            print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                            count = count +1
    
            elif idgame !='' and nama == '' and kategori!='' and tahun =='' and harga=='':
                for row in data:
                    if idgame == row[0]:
                        if kategori== row[2]:
                            print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                            count = count +1

            elif idgame !='' and nama=='' and kategori=='' and tahun !='' and harga=='':
                for row in data:
                    if idgame == row[0]:
                        if tahun == row[3]:
                            print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                            count = count +1

            elif idgame != '' and nama=='' and kategori=='' and tahun =='' and harga !='':
                for row in data:
                    if idgame == row[0]:
                        if harga == row[4]:
                            print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                            count = count +1

            elif idgame =='' and nama !='' and kategori =='' and tahun !='' and harga =='':
                for row in data:
                    if nama == row[1]:
                        if tahun == row[3]:
                            print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                            count = count +1

            elif idgame =='' and nama !='' and kategori =='' and tahun=='' and harga != '':
                for row in data:
                    if nama == row[1]:
                        if harga == row[4]:
                            print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                            count = count +1
    
            elif idgame =='' and nama =='' and kategori !='' and tahun=='' and harga != '':
                for row in data:
                    if kategori == row[2]:
                        if harga == row[4]:
                            print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                            count = count +1

            elif idgame !='' and nama != '' and kategori !='' and tahun =='' and harga =='':
                for row in data:
                    if idgame == row[0]:
                        if nama==row[1]:
                            if kategori==row[2]:
                                print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                count = count +1

            elif idgame !='' and nama == '' and kategori !='' and tahun !='' and harga =='':
                for row in data:
                    if idgame==row[0]:
                        if kategori == row[2]:
                            if tahun ==row[3]:
                                print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                count = count +1
                
            elif idgame =='' and nama != '' and kategori !='' and tahun !='' and harga =='':
                for row in data:
                    if nama == row[1]:
                        if kategori ==row[2]:
                            if tahun == row[3]:
                                print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                count = count +1
            
            elif idgame !='' and nama != '' and kategori =='' and tahun !='' and harga =='':
                for row in data:
                    if idgame == row[0]:
                        if nama == row[1]:
                            if tahun == row[3]:
                                print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                count = count +1
        
            elif idgame !='' and nama != '' and kategori =='' and tahun =='' and harga !='':
                for row in data:
                    if idgame == row[0]:
                        if nama == row[1]:
                            if harga == row[4]:
                                print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                count = count +1
        
            elif idgame =='' and nama != '' and kategori !='' and tahun =='' and harga !='':
                for row in data:
                    if nama ==row[1]:
                        if kategori == row[2]:
                            if harga == row[4]:
                                print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                count = count +1
    
            elif idgame =='' and nama == '' and kategori !='' and tahun !='' and harga !='':
                for row in data:
                    if kategori == row[2]:
                        if tahun == row[3]:
                            if harga == row[4]:
                                print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                count = count +1
        
            elif idgame !='' and nama == '' and kategori =='' and tahun !='' and harga !='':
                for row in data:
                    if idgame == row[0]:
                        if tahun == row[3]:
                            if harga == row[4]:
                                print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                count = count +1
        
            elif idgame =='' and nama != '' and kategori =='' and tahun !='' and harga !='':
                for row in data:
                    if nama == row[1]:
                        if tahun == row[3]:
                            if harga == row[4]:
                                print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                count = count +1
        
            elif idgame !='' and nama == '' and kategori !='' and tahun =='' and harga !='':
                for row in data:
                    if idgame == row[0]:
                        if kategori == row[2]:
                            if harga == row[4]:
                                print(f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                count = count +1
        
            elif idgame != '' and nama != '' and harga == '' and tahun != '' and kategori != '':
                arr = []
                for row in data:
                    if idgame == row[0]:
                        if nama == row[1]:
                            if kategori == row[2]:
                                if tahun == row[3]:
                                    print (f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                    count = count+1    
    
            elif idgame =='' and harga !='' and tahun !=''and kategori !='' and nama !='':
                for row in data:
                    if nama == row[1]:
                        if kategori == row[2]:
                            if tahun == row[3]:
                                if harga == row[4]:
                                    print (f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ") 
                                    count = count+1

            elif idgame !='' and nama =='' and tahun !='' and kategori != '' and harga!='':
                for row in data:
                    if idgame== row[0]:
                        if kategori == row[2]:
                            if tahun == row[3]:
                                if harga == row[4]:
                                    print (f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ") 
                                    count = count+1

            elif idgame !='' and nama !='' and tahun !='' and kategori =='' and harga !='':
                for row in data:
                    if idgame ==row[0]:
                        if nama == row[1]:
                            if tahun == row[3]:
                                if harga == row[4]:
                                    print (f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ") 
                                    count = count+1
    
            elif idgame !='' and nama!='' and tahun =='' and kategori!='' and harga!='':
                for row in data:
                    if idgame == row[0]:
                        if nama == row[1]:
                            if kategori == row[2]:
                                if harga == row[4]:
                                    print (f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                    count = count+1

            elif idgame !=''and nama!='' and tahun !='' and kategori !='' and harga !='':
                for row in data:
                    if idgame == row[0]:
                        if nama == row[1]:
                            if kategori == row[2]:
                                if tahun == row[3]:
                                    if harga == row[4]:
                                        print (f"{count}. {row[0]} | {row[1]} | {row[4]} | {row[3]} | {row[2]} | {row[5]} ")
                                        count = count+1
            if count == 1:
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
