import os

def cls():
    os.system("cls")


def print_home():
    print("="*5, "SELAMAT DATANG DI BNMO", "="*5)
    print("="*13, "Login", "="*14)
    print("="*14, "Help", "="*14)

def menu_user():
    print("="*20, "MENU BNMO", "="*20)
    print("""
1. List Game Toko           || Ketik: list_game_toko
2. Buy Game                 || Ketik: buy_game
3. List Game                || Ketik: list_game
4. Search My Game           || Ketik: search_my_game
5. Search Game at Store     || Ketik: search_game_at_store
6. Riwayat                  || Ketik: riwayat
7. Help                     || Ketik: help
8. Save                     || Ketik: save
9. Exit                     || Ketik: exit

Bonus game~
Magic Conch Shell           || Ketik: kerangajaib
Tic Tac Toe                 || Ketik: tictactoe
    """)

def menu_admin():
    print("="*20, "MENU BNMO", "="*20)
    print("""
1. Register                 || Ketik: register
2. Tambah Game              || Ketik: tambah_game
3. Ubah Game                || Ketik: ubah_game
4. Ubah Stok                || Ketik: ubah_stok
5. List Game Toko           || Ketik: list_game_toko
6. Search Game at Store     || Ketik: search_game_at_store
7. Topup Saldo              || Ketik: topup
8. Help                     || Ketik: help
9. Save                     || Ketik: save
10. Exit                    || Ketik: exit

Bonus game~
Magic Conch Shell           || Ketik: kerangajaib
Tic Tac Toe                 || Ketik: tictactoe
    """)

