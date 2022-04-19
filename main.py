from fitur_utama.register import register
from fitur_utama.login import login
from fitur_utama.tambah_game import tambah_game
from fitur_utama.help import help
from fitur_utama.buy_game import buy_game
from fitur_utama.exit import exit
from fitur_utama.list_game import list_game
from fitur_utama.list_game_toko import list_game_toko
from fitur_utama.riwayat import riwayat
from fitur_utama.save import save
from fitur_utama.search_my_game import search_my_game
from fitur_utama.ubah_game import ubah_game
from fitur_utama.ubah_stok import ubah_stok
from fitur_utama.search_game_at_store import search_game_at_store
from fitur_utama.topup import topup
from fitur_bonus.kerangajaib import kerangajaib
from fitur_bonus.TicTacToe import TicTacToe
from modul_fungsi.csv_function import load_data
from modul_fungsi.data_function import isAdmin
from modul_fungsi.display_function import cls, menu_admin, menu_user, print_home

# Program argaparse untuk akses folder
nama_folder = "folder_data"                 # Keperluan testing

# Loading data dari csv
data_user = load_data(nama_folder, "user")
data_game = load_data(nama_folder, "game")
data_kepemilikan = load_data(nama_folder, "kepemilikan")
data_riwayat = load_data(nama_folder, "riwayat")

print(data_user)
# Home BNMO
print_home()
i = False
currentuser = False
username = ""
while (i == False) or (currentuser == False):
    opt = input("Masukkan pilihan kamu >>> ").lower()
    if (opt == "login"):
        username = input("Masukan username: ")
        password = input("Masukan password: ")
        login(data_user, currentuser, username, password)
        i = True
    elif (opt == "help"):
        help(currentuser, "gen")
        i = True
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”")


# Setelah berhasil login
if(isAdmin(data_user, username) == True):
    cls()
    menu_admin()
    bool_admin = False
    while (bool_admin == False):
        opt1 = input(">>> ")
        if (opt1 == "login"):
            login(data_user, username, password, currentuser)
        elif (opt1 == "register"):
            data_user = register(data_user)
        elif (opt1 == "tambah_game"):
            data_game = tambah_game(data_game)
        elif (opt1 == "ubah_game"):
            data_game = ubah_game(data_game)
        elif (opt1 == "ubah_stok"):
            data_game = ubah_stok(data_game)
        elif (opt1 == "list_game_toko"):
            list_game_toko(data_game)
        elif (opt1 == "search_game_at_store"):
            search_game_at_store(data_game)
        elif (opt1 == "topup"):
            data_user = topup(data_user)
        elif (opt1 == "help"):
            help(currentuser, "admin")
        elif (opt1 == "save"):
            save(data_kepemilikan, data_user, data_game, data_riwayat)
        elif (opt1 == "kerangajaib"):
            kerangajaib()
        elif (opt1 == "tictactoe"):
            TicTacToe()
        elif (opt1 == "buy_game") or (opt1 == "list_game") or (opt1 == "search_my_game") or (opt1 == "riwayat"):
            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        elif (opt1 == "exit"):
            exit(data_kepemilikan, data_user, data_game, data_riwayat)
            bool_admin = True
        else:
            print("Maaf, perintah yang dimasukkan tidak tersedia.")
        cls()
else:
    cls()
    menu_user()
    bool_user = False
    while (bool_user == False):
        opt2 = input(">>> ")
        if (opt2 == "login"):
            login(data_user, username, password, currentuser)
        elif (opt2 == "buy_game"):
            data_kepemilikan, data_user, data_game, data_riwayat = buy_game(data_kepemilikan, data_user, data_game, data_riwayat)
        elif (opt2 == "list_game"):
            list_game(data_game)
        elif (opt2 == "search_my_game"):
            search_my_game(data_game)
        elif (opt2 == "list_game_toko"):
            list_game_toko(data_game)
        elif (opt2 == "search_game_at_store"):
            search_game_at_store(data_game)
        elif (opt2 == "riwayat"):
            riwayat(data_riwayat)
        elif (opt2 == "help"):
            help(currentuser, "user")
        elif (opt2 == "save"):
            save(data_kepemilikan, data_user, data_game, data_riwayat)
        elif (opt2 == "kerangajaib"):
            kerangajaib()
        elif (opt2 == "tictactoe"):
            TicTacToe()
        elif (opt2 == "register") or (opt2 == "tambah_game") or (opt2 == "ubah_game") or (opt2 == "ubah_stok") or (opt2 == "topup"):
            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        elif (opt2 == "exit"):
            exit(data_kepemilikan, data_user, data_game, data_riwayat)
            bool_user = True
        else:
            print("Maaf, perintah yang dimasukkan tidak tersedia.")
        cls()

