import time
from modul_fungsi.data_function import LCG


def kerangajaib():
    input("Apa pertanyaanmu? ")
    number = time.time()
    if 0 <= LCG(1,number) <= 0.33:
        return "Tidak"
    elif 0.33 < LCG(1,number) <= 0.67:
        return "Mungkin"
    else:
        return "Ya"

