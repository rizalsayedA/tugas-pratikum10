data = {}
while True:
    print("")
    g = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar: ")
    # Untuk keluar dari program
    if g.lower() == "k":
        print("Keluar dari program")
        break
    # untuk melihat list
    elif g.lower() == "l":
        if data.items():
            print("~~~Daftar Nilai~~~")
            print()
            print("======================================================================================")
            print("|  No  |      NIM     |      NAMA      |   TUGAS  |   UTS   |   UAS   | AKHIR  |")
            print("======================================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:4} | {0:13s} | {1:13} | {2:8d} |  {3:6d} | {4:7d} | {5:12.2f} | " \
                      .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
                print("======================================================================================")
                print("")
        else:
            print("~~~Daftar Nilai~~~")
            print()
            print("======================================================================================")
            print("|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |")
            print("======================================================================================")
            print("|                                 Tidak Ada Daftar Nilai                             |")
            print("======================================================================================")
    # Untuk menambahkan data
    elif g.lower() == "t":
        print("Tambah Data")
        nim = int(input("NIM            : "))
        nama = input("Nama              : ")
        uts = int(input("Nilai UTS      : "))
        uas = int(input("Nilai UAS      : "))
        tugas = int(input("NIlai Tugas  : "))
        nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
    # Untuk mengubah data
    elif g.lower() == "u":
        print("Edit Data Nilai Mahasiswa")
        nama = input(" Masukan Nama:")
        if nama in data.keys():
            nim = input("NIM               :")
            tugas = int(input("Nilai Tugas Baru  : "))
            uts = int(input("Nilai UTS Baru    : "))
            uas = int(input("Nilai UAS Baru    : "))
            nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
            data[nama] = nim, tugas, uts, uas, nilaiakhir
        else:
            print("Data nilai{0} tidak ada ".format(nama))
    # Untuk menghapus data
    elif g.lower() == "h":
        print("Hapus Data Nilai Mahasiswa")
        nama = input(" Masukan Nama:")
        if nama in data.keys():
            del data[nama]
        else:
            print("Data {0} tidak ada".format(nama))
        

else:
    print("Pilih Menu Yang Tersedia")
