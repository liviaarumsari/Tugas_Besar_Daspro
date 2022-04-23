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

def append(list, element):
    list+=[element]

def print_data(data):
    baris = panjang(data)
    kolom = panjang(data[0])

    # Mencari panjang maksimal setiap kolom
    pjg_maks = []
    for i in range (kolom):
        pjg_kolom = 0
        for j in range (baris):
            if(panjang(str(data[j][i])) > pjg_kolom):
                pjg_kolom = panjang(str(data[j][i]))
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

def tambah(arr,string):
    a=["*" for i in range(panjang(arr)+1)]
    for i in range (panjang(arr)+1):
        if i==panjang(arr):
            a[i]=string
        else:
            a[i]=arr[i]
    return a

def enter(string,char,subchar):
    result=""
    for i in string:
        if i==char:
            result+=subchar
        else:
            result+=i
    return result

def pisah(string, delimiter): 
    result = []
    x = ''
    for i in string :
        if i != delimiter :
            x += i
        else :
            result = tambah(result, x)
            x = ''  
    result = (tambah(result, x))
    return result


def maxchar(arr, column):
    max = 0
    for i in range(panjang(arr)):
        long = panjang(splitchar(str(arr[i][column])))  # Hitung panjang words yang diubah jadi array
        if long > max:
            max = long
    return max


def formatCariGame(arr):
    # from
    # [['G001','Binomo','Judi Online', '2020', 10000, 10],['G002','kacang','Garing', '2020', 10000, 10]]
    # to
    # G001 | Binomo | 10.000 | Judi Online | 2022
    # G002 | kacang | 10.000 | Garing | 2022
    
    text = ""
    numbering = 1
    for i in range(panjang(arr)):
        gameID = str(arr[i][0])
        nama = str(arr[i][1])
        harga =  str(arr[i][4])
        kategori = str(arr[i][2])
        tahun = str(arr[i][3])

        if panjang(splitchar(gameID)) != maxchar(arr,0):
            space = " " * (maxchar(arr,0) - (panjang(splitchar(gameID))))
            gameID += space
        if panjang(splitchar(nama)) != maxchar(arr,1):
            space = " " * (maxchar(arr,1) - (panjang(splitchar(nama))))
            nama += space
        if panjang(splitchar(harga)) != maxchar(arr,4):
            space = " " * (maxchar(arr,4) - (panjang(splitchar(harga))))
            harga += space
        if panjang(splitchar(kategori)) != maxchar(arr,2):
            space = " " * (maxchar(arr,2) - (panjang(splitchar(kategori))))
            kategori += space
        if panjang(splitchar(tahun)) != maxchar(arr,3):
            space = " " * (maxchar(arr,3) - (panjang(splitchar(tahun))))
            tahun += space
        
        newtext = f"{str(numbering)}. {gameID} | {nama} | {harga} | {kategori} | {tahun} \n"
        text += newtext
        numbering += 1
    
    return text




