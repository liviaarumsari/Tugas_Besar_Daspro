from fitur_utama.save import save


def exit(kepemilikan, user, game, riwayat):
    i = False
    while (i == False):
        print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        opt = input()
        if (opt == "y") or (opt == "Y") or (opt == "n") or (opt == "y"):
            i = True
    if (opt == "y") or (opt == "Y"):
        # Jalankan fungsi save
        save(kepemilikan, user, game, riwayat)

