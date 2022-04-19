# Fungsi untuk pencarian dan validasi data

from modul_fungsi.array_function import panjang, splitchar

def Exist(arr,data, column):		    # Validasi apakah data ada
	i = 0
	for i in range(panjang(arr)):
		LookUp = arr[i][column]
		if LookUp == data:
			return True
		else:
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






