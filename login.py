currentuser = False
def login(data_f):
    if currentuser = True:
        print("Sudah login, masukan perintah selanjutnya.")
    else:
        username= input("Masukan username: ")
        password= input("Masukan password: ")


        for i in range(len(data_f)):
            if data_f[i][1] == username:
                if data_f[i][3] == password:
                    print("Halo {}!, Selamat datang di 'Binomo'.".format(data_f[i][2]))
                    currentuser = True #tandanya udah login
                    break
                else:
                    print("Password atau username salah atau tidak ditemukan.")
            if i==len(data_f):
                print("Password atau username salah atau tidak ditemukan.")
    

