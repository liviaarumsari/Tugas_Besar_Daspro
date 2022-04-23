# Fungsi untuk pencarian dan validasi data

from modul_fungsi.array_function import panjang, splitchar

def Exist(arr,data, column):		    # Validasi apakah data ada
	i = 0
	for i in range(panjang(arr)):
		LookUp = arr[i][column]
		if LookUp == data:
			return True
	return False

def UserValid(username):			    # Memvalidasi username
	lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	number = ['1','2','3','4','5','6','7','8','9','0','_','-']
	
	letter = splitchar(username)
	count = 0
	for i in range (panjang(letter)):
		if (letter[i] in lowercase) or (letter[i] in uppercase) or (letter[i] in number) :
			count += 1

	if count == panjang(letter):
		return True
	else:
		return False

def DataLoc(arr, data, column):			# Mencari baris ke berapa lokasi data tersebut berada
	found = 0
	for i in range(panjang(arr)):
		if arr[i][column] == data:
			found = i
			break	
	return found

def userID(int):
	if int<10:
		return '00' + str(int)
	elif 10 <=int <= 99:
		return '0'+ str(int)
	else:
		return str(int)

def gameID(int):
	if int<10:
		return "G" + '00' + str(int)
	elif 10 <=int <= 99:
		return "G" + '0' + str(int)
	else:
		return "G" + str(int)

def isAdmin(arr,username):				# Cek Apakah Admin
	if arr[DataLoc(arr, username, 1)][4] == 'admin':
		return True
	else:
		return False

def getuserID (data, username):			# Mendapatkan user ID dari username
	for i in range (panjang(data)):
		if (data[i][1] == username):
			return data[i][0]

def data_game_user(username, user, kepemilikan):		# Membuat array game ID yang dimiliki user
	g_user = []
	id_user = getuserID(user, username)
	for i in range (panjang(kepemilikan)):
		if (kepemilikan[i][1] == id_user):
			game_id = kepemilikan[i][0]
			g_user += [game_id]
	return g_user

def validasi_tahun(tahun):				# Menerima input berupa string tahun dan melakukan looping jika input tahun tidak valid, tahun valid 1900 <= tahun <= 2022
	i = False
	while (i == False):
		if (panjang(tahun) == 4):
			if (1900 <= int(tahun) <= 2022):
				i = True
				return tahun					# Mengembalikan nilai tahun yang sudah valid
		else:
			print("Masukan tahun tidak valid!")
			tahun = input("Masukkan tahun rilis: ")

def validasi_harga(harga, pesan_error, pesan_input):				# Menerima input berupa string harga dan melakukan looping jika input harga tidak valid, harga valid berupa angka
	i = False
	while (i == False):
		# Menghapus tanda baca titik yang mungkin diinput saat memasukkan harga
		harga_baru = ""
		for i in range (panjang(harga)):
			c = harga[i]
			if (c != "."):
				harga_baru += c
		
		# Mengecek apakah input hanya berupa angka
		bool_int = True
		try: 
			int(harga_baru)
		except ValueError: 
			bool_int = False
		if (bool_int == True):
			i = True
			harga_valid = str(int(harga_baru))
			return harga_valid					# Mengembalikan nilai harga yang sudah valid
		else:
			print(pesan_error)
			harga = input(pesan_input)			
