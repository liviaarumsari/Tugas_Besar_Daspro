from modul_fungsi.array_function import tambah
from modul_fungsi.array_function import pisah
from modul_fungsi.array_function import enter

def load(folder, file):
    data = []
    with  open("./%s/%s.csv" % (folder, file), "r") as file:
        for line in file.readlines():
            data = tambah(data, (pisah(enter(line, "\n", ""), ";")))
    return data




