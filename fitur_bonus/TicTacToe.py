from modul_fungsi.bonus_function import Board, Coor, CurrentUser, IsInputValid, IsTaken, IsWin, IsiBoard, QuitGame
def TicTacToe():
  board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
  ]

  user = True # when true it refers to x, otherwise o
  turns = 0

  while turns < 9:
    active_user = CurrentUser(user)
    Board(board)
    user_input = input("Masukkan posisi 1 sampai 9 atau masukkan \"q\" untuk berhenti bermain:")
    if QuitGame(user_input): break
    if not IsInputValid(user_input):
      print("Coba lagi.")
      continue
    user_input = int(user_input) - 1
    coords = Coor(user_input)
    if IsTaken(coords, board):
      print("Coba lagi.")
      continue
    IsiBoard(coords, board, active_user)
    if IsWin(active_user, board): 
      print(f"{active_user.upper()} Menang!")
      break
    
    turns += 1
    if turns == 9: print("Seri!")
    user = not user
