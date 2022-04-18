# Fungsi untuk pencarian dan validasi data

import array_function

def Exist(arr,data, column):		    # Validasi apakah data ada
	i = 0
	for i in range(array_function.panjang(arr)):
		LookUp = arr[i][column]
		if LookUp == data:
			return True
		else:
			return False

def UserValid(username):			    # Memvalidasi username
	lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	number = ['1','2','3','4','5','6','7','8','9','0','_','-']
	
	letter = array_function.splitchar(username)
	count = 0
	for i in range (array_function.panjang(letter)):
		if (letter[i] in lowercase) or (letter[i] in uppercase) or (letter[i] in number) :
			count += 1

	if count == array_function.panjang(letter):
		return True
	else:
		return False

def DataLoc(arr, data, column):			# Mencari baris ke berapa lokasi data tersebut berada
	found = -1
	for i in range(array_function.panjang(arr)):
		if arr[i][column] == data:
			found += i+1
			break	
		
	if found > -1:
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
	if arr[DataLoc(username,1)][4] == 'admin':
		return True
	else:
		return False
print(gameID(1))


def LCG(N,S):               # linear congruential generator (LCG)
    a = 7**3
    M = 2**5-1

    def f(S):
        return (a*S) % M
    
    U = 0
    for i in range(N):
        S = f(S)
        U += (S/M)
    return U




