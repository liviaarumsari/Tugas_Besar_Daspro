from modul_fungsi.array_function import panjang


def ubah_game(data):
    id = input("Masukkan ID Game: ")
    # Mencari baris array dengan id game yang diinput
    for i in range (panjang(data)):
        if(data[i][0] == id):
            baris = i
    nama = input("Masukkan nama game: ")
    if(nama != ""):
        data[baris][1] = nama
    kategori = input("Masukkan kategori: ")
    if(kategori != ""):
        data[baris][2] = kategori
    tahun_rilis = input("Masukkan tahun rilis: ")
    if(tahun_rilis != ""):
        data[baris][3] = tahun_rilis
    harga = input("Masukkan harga: ")
    if(harga != ""):
        data[baris][4] = harga
    return data

data_baru = ubah_game(data)
print(data_baru)
    