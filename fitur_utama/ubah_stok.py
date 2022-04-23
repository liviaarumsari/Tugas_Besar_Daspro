from modul_fungsi.data_function import Exist, DataLoc, panjang
from modul_fungsi.array_function import splitchar


def jumlahValid(char):
    valid_int = ['0','1','2','3','4','5','6','7','8','9']
    character = splitchar(char)
    flag = False
    for i in range(panjang(character)):
        for j in range(panjang(valid_int)):
            if character[i] == valid_int[j]:
                flag = True
    return flag


def ubah_stok(arr):
    idgame = input("Masukkan ID game: ")
    while idgame == "":
        print("Silakan input ID game terlebih dahulu")
        idgame = input("Masukkan ID game: ")

    while Exist(arr,idgame, 0) == False:
        print("Tidak ada game dengan ID tersebut")
        idgame = input("Masukkan ID game: ")

    jumlahstr = input("Masukkan Jumlah: ")
    while jumlahstr == "":
        print("Jumlah tidak boleh kosong, Tulis 0 bila tidak ingin melakukan perubahan")
        jumlahstr = input("Masukkan Jumlah: ")
    
    while jumlahValid(jumlahstr) == False:
        print("Jumlah harus berupa angka")
        jumlahstr = input("Masukkan Jumlah: ")

    jumlah = int(jumlahstr)
    edit = int(arr[DataLoc(arr,idgame,0)][5]) + (jumlah)
    if edit < 0:
        print(f"Stock game {arr[DataLoc(arr,idgame,0)][1]} gagal dikurangi karena stock kurang. Stock sekarang: {arr[DataLoc(arr,idgame,0)][5]}")
        return arr
    else:
        if jumlah < 0:
            print(f'Stok game {arr[DataLoc(arr,idgame,0)][1]} berhasil dikurangi. Stok sekarang : {edit}')
            arr[DataLoc(arr,idgame,0)][5] = edit
            return arr
        elif jumlah > 0:
            print(f'Stok game {arr[DataLoc(arr,idgame,0)][1]} berhasil ditambah. Stok sekarang : {edit}')
            arr[DataLoc(arr,idgame,0)][5] = edit
            return arr
        else:
            print(f'Stok game {arr[DataLoc(arr,idgame,0)][1]} tidak berubah. Stok sekarang : {edit}')

