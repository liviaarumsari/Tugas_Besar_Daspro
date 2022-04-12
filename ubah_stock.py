from modul_fungsi.array_function import Exist
from modul_fungsi.array_function import DataLoc


def ubah_stock(arr):
    idgame = input("Masukkan ID game: ")
    if Exist(arr,idgame, 0) == True:
        jumlah = int(input("Masukkan Jumlah: "))
        edit = int(arr[DataLoc(arr,idgame,0)][5]) + jumlah
        if edit < 0:
            print(f"Stock game {arr[DataLoc(arr,idgame,0)][1]} gagal dikurangi karena stock kurang. Stock sekarang: {arr[DataLoc(arr,idgame,0)][5]}")
        else:
            if jumlah < 0:
                print(f'Stok game {arr[DataLoc(arr,idgame,0)][1]} berhasil dikurangi. Stok sekarang : {edit}')
                arr[DataLoc(arr,idgame,0)][5] = edit
                print(arr[DataLoc(arr,idgame,0)][5])
            elif jumlah > 0:
                print(f'Stok game {arr[DataLoc(arr,idgame,0)][1]} berhasil ditambah. Stok sekarang : {edit}')
                arr[DataLoc(arr,idgame,0)][5] = edit
                print(arr[DataLoc(arr,idgame,0)][5])
    else:
        print("Tidak ada game dengan ID tersebut")