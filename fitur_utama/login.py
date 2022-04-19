from modul_fungsi.array_function import panjang 


def login(data_f, username, password, currentuser):
    if currentuser == True:
        print("Sudah login, masukan perintah selanjutnya.")
    else:
        for i in range(panjang(data_f)):
            if data_f[i][1] == username:
                if data_f[i][3] == password:
                    print("Halo {}!, Selamat datang di 'Binomo'.".format(data_f[i][2]))
                    currentuser = True #tandanya udah login
                    break
                else:
                    print("Password atau username salah atau tidak ditemukan.")
            if (i == panjang(data_f)-1):
                print("Password atau username salah atau tidak ditemukan.")
    

