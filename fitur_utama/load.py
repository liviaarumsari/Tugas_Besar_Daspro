from modul_fungsi.array_function import tambah
from modul_fungsi.array_function import pisah
from modul_fungsi.array_function import enter
import os

import argparse
parser = argparse.ArgumentParser(description="Tidak ada nama folder yang diberikan!")
parser.add_argument("folder", help="Folder Penyimpanan")
args = parser.parse_args()

user=[]
game=[]
riwayat=[]
kepemilikan=[]


def load():
    global user, game, riwayat, kepemilikan
    if os.path.exists(args.folder):
        print("Loading...")
        with open(args.folder + "\\user.csv", "r") as file:
            for line in file.readlines():
                user = tambah(user, (pisah(enter(line, "\n", ""), ";")))
        with open(args.folder + "\\game.csv", "r") as file: 
            for line in file.readlines():
                game = tambah(game,(pisah(enter(line,"\n", ""), ";")))
        with open(args.folder + "\\riwayat.csv", "r") as file: 
            for line in file.readlines():
                riwayat = tambah(riwayat,(pisah(enter(line,"\n", ""), ";")))
        with open(args.folder + "\\kepemilikan.csv", "r") as file: 
            for line in file.readlines():
                kepemilikan = tambah(kepemilikan,(pisah(enter(line,"\n", ""), ";")))
        print('Selamat Datang di antarmuka "Binomo"')
    else :
        print(f"Folder {args.folder} tidak ditemukan.")

load()