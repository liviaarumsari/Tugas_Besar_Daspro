# Fungsi-fungsi untuk manipulasi array

def split(string1, delimiter):
    N = 1
    for c in string1:
        if (c == delimiter):
            N += 1
    word = ["" for i in range (N)]
    i = 0
    for c in string1:
        if (c == delimiter):
            i += 1
        else:
            word[i] += c
    return word

def splitchar(word):					# Mengubah kata menjadi huruf
    return [char for char in word]

def panjang(arr):
    i = 0
    for c in arr:
        i += 1
    return i


def print_data(data):
    baris = panjang(data)
    kolom = panjang(data[0])

    # Mencari panjang maksimal setiap kolom
    pjg_maks = []
    for i in range (kolom):
        pjg_kolom = 0
        for j in range (baris):
            if(panjang(data[j][i]) > pjg_kolom):
                pjg_kolom = panjang(data[j][i])
        pjg_maks += [pjg_kolom]

    for i in range (baris):
        print(i+1, ". ", end="")
        for j in range (kolom):
            print(data[i][j], " "*(pjg_maks[j] - panjang(data[i][j])), end="")
            if(j < kolom-1):
                print("| ", end="")
        print()

def isXmember(arr, x):
    for i in range (panjang(arr)):
        if (arr[i] == x):
            return True
        else:
            return False
        

def buat_data_baru(data, hapus_kolom):
    data_baru = []
    for i in range (panjang(data)):
        data_baru_baris = []
        for j in range (panjang(data[0])):
            if (isXmember(hapus_kolom,j) == False):
                data_baru_baris += [data[i][j]]
        data_baru += [data_baru_baris]
    return data_baru



    



#




