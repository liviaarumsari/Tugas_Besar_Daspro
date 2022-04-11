from modul_fungsi import array_function

def load_data(nama_folder,nama_file):
    # Buka dan baca file csv
    file = open("./%s/%s.csv" % (nama_folder, nama_file), "r")
    data = file.read()

    # Memisahkan tiap baris data csv
    baris = array_function.split(data, "\n")

    # Memisahkan antardata yang terpisah dengan ";"
    hasil_data = []
    for line in baris:
        data_baris = array_function.split(line, ";")
        hasil_data += [data_baris]

    # Menghapus header
    hasil_data_baru = []
    for i in range (1,array_function.panjang(hasil_data)):
        data_baru_baris = []
        for j in range (array_function.panjang(hasil_data[0])):
                data_baru_baris += [hasil_data[i][j]]
        hasil_data_baru += [data_baru_baris]

    return hasil_data_baru


