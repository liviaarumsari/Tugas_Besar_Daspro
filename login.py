from modul_fungsi.array_function import panjang 

currentuser = False
def login(data):
    if currentuser = True:
        print("Sudah login, masukan perintah selanjutnya.")
    else:
        username= input("Masukan username: ")
        password= input("Masukan password: ")


        for i in range(panjang(data)):
            if data[i][1] == username:
                if data[i][3] == password:
                    print("Halo {}!, Selamat datang di 'Binomo'.".format(data_f[i][2]))
                    currentuser = True #tandanya udah login
                    break
                else:
                    print("Password atau username salah atau tidak ditemukan.")
            if i==panjang(data-1):
                print("Password atau username salah atau tidak ditemukan.")
    

