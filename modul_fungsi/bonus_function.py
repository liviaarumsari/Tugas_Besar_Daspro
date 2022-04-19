# Untuk Kerang ajaib
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

# Untuk TicTacToe
def forTictac():
    def Board(board):
      for row in board:
        for slot in row:
          print(f"{slot} ", end="")
        print()

    def QuitGame(user_input):
      if user_input == "q" or user_input == "Q": 
        print("Terimakasih sudah bermain dengan Binomo")
        return True
      else: 
        return False

    def IsInputValid(user_input):
      # check if its a number
      if not IsNumberValid(user_input): 
        return False

      user_input = int(user_input)
      # check if its 1 - 9
      if not NumberValid(user_input): 
        return False

      return True

    def IsNumberValid(user_input):
      number = ['1','2','3','4','5','6','7','8','9']

      if not (user_input in number):
        print("Angka masukan tidak valid")
        return False
      else: 
        return True

    def NumberValid(user_input):
      if user_input > 9 or user_input < 1: 
        print("Angka diluar batas valid (1-9).")
        return False
      else: 
        return True

    def IsTaken(coords, board):
      row = coords[0]
      col = coords[1]
      if board[row][col] != "-":
        print("Posisi tersebut sudah digunakan.")
        return True
      else: return False

    def Coor(user_input):
      row = int(user_input / 3)
      col = user_input
      if col > 2: col = int(col % 3)
      return (row,col)

    def IsiBoard(coords, board, active_user):
      row = coords[0]
      col = coords[1]
      board[row][col] = active_user

    def CurrentUser(user):
      if user: 
        return "x"
      else: 
        return "o"

    def IsWin(user, board):
      if check_row(user, board): 
        return True
      if check_col(user, board): 
        return True
      if check_diag(user, board): 
        return True
      return False

    def check_row(user, board):
      for row in board:
        complete_row = True
        for slot in row:
          if slot != user:
            complete_row = False
            break
        if complete_row: return True
      return False 

    def check_col(user, board):
      for col in range(3):
        complete_col = True
        for row in range(3):
          if board[row][col] != user:
            complete_col = False
            break
        if complete_col: return True
      return False

    def check_diag(user, board):
      #top left to bottom right
      if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
      elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
      else: return False
