def list_game_toko (df):
    if currentuser = False:
        print("Anda belum login. Silahkan login terlebih dahulu.")
    else:
        import pandas as pd
        df = pd.read_csv("namafile.csv")
        
        sort=input("Skema sorting : ")
        if sort=="tahun-":
            print(df.sort_values(["tahun_rilis"], ascending=[0]))
        elif sort=="tahun+":
            print(df.sort_values(["tahun_rilis"], ascending=[1]))
        elif sort=="harga-":
            print(df.sort_values(["harga"], ascending=[0]))
        elif sort=="harga+":
            print(df.sort_values(["harga"], ascending=[1]))
        elif sort=="":
            print(df.sort_values(["id"], ascending=[1]))
        else:
            print("Skema sorting tidak valid!")
            
        
