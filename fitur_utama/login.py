from modul_fungsi.array_function import panjang 


def login(data_f, currentuser):
    if currentuser == True:
        print("Sudah login, masukan perintah selanjutnya.")
    else:
        username = input("Masukan username: ")
        password = input("Masukan password: ")
        for i in range(panjang(data_f)):
            if data_f[i][1] == username:
                if data_f[i][3] == password:
                    print("Halo {}!, Selamat datang di 'Binomo'.".format(data_f[i][2]))
                    return username, True #tandanya udah login
                else:
                    print("Password atau username salah atau tidak ditemukan.")
                    return username, False    # gagal login
            if (i == panjang(data_f)-1):
                print("Password atau username salah atau tidak ditemukan.")
                return username, False
    

