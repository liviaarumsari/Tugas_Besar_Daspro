from modul_fungsi.array_function import panjang
from modul_fungsi.data_function import validasi_harga, validasi_tahun


def ubah_game(data):
    id = input("Masukkan ID Game: ")
    # Mencari baris array dengan id game yang diinput
    found = False
    for i in range (panjang(data)):
        if(data[i][0] == id):
            baris = i
            found = True
    if (found == True):
        nama = input("Masukkan nama game: ")
        empty = 0
        if(nama != ""):
            data[baris][1] = nama
        else:
            empty += 1
        kategori = input("Masukkan kategori: ")
        if(kategori != ""):
            data[baris][2] = kategori
        else:
            empty += 1
        tahun_rilis = input("Masukkan tahun rilis: ")
        if(tahun_rilis != ""):
            tahun_rilis = validasi_tahun(tahun_rilis)
            data[baris][3] = tahun_rilis
        else:
            empty += 1
        harga = input("Masukkan harga: ")
        if(harga != ""):
            harga = validasi_harga(harga, "Masukan harga tidak valid. Silahkan ulangi pengisian harga", "Masukkan harga: ")
            data[baris][4] = harga
        else:
            empty += 1
        if (empty == 4):
            print("Seluruh data tidak ada yang diisi. Game tidak berubah.")
        else: # empty < 4
            print("Game berhasil diubah.")
    else:
        print("Maaf ID game tersebut tidak tersedia.")
    return data

    