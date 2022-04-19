from modul_fungsi.array_function import split, panjang

# CSV to matriks
def load_data(nama_folder,nama_file):
    # Buka dan baca file csv
    file = open("./%s/%s.csv" % (nama_folder, nama_file), "r")
    data = file.read()

    # Memisahkan tiap baris data csv
    baris = split(data, "\n")

    # Memisahkan antardata yang terpisah dengan ";"
    hasil_data = []
    for line in baris:
        data_baris = split(line, ";")
        hasil_data += [data_baris]

    # Pastiin perlu pake header atau engga
    # Menghapus header
    # hasil_data_baru = []
    # for i in range (1,array_function.panjang(hasil_data)):
    #     data_baru_baris = []
    #     for j in range (array_function.panjang(hasil_data[0])):
    #             data_baru_baris += [hasil_data[i][j]]
    #     hasil_data_baru += [data_baru_baris]

    return hasil_data

# Matriks to CSV
def save_data(data, nama_folder, nama_file):
    file=open("./%s/%s.csv" % (nama_folder, nama_file), "w")    
    for i in range(panjang(data)):
        for j in range(panjang(data[0])):
            if (j == panjang(data[0])-1):
                file.write(data[i][j])
            else:
                file.write(data[i][j] + ";")
        file.write("\n")
    file.close()