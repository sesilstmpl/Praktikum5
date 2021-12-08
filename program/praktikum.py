x = {}
print("========================")
print("Program Input Nilai")
print("========================")
while True:
    print("")
    c = input("L)ihat, T)ambah, U)bah, H)apus, C)ari, K)eluar: ")
    if c.lower() == 't':
        print("Tambah Data")
        nama = input("Masukkan Nama Mahasiswa   : ")
        nim = input("Masukkan NIM              : ")
        tugas = int(input("Masukkan Nilai Tugas      : "))
        uts = int(input("Masukkan Nilai UTS        : "))
        uas = int(input("Masukkan Nilai UAS        : "))
        akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
        x[nama] = nim , tugas, uts , uas , akhir

    elif  c . lower () ==  'u' :
        print ( "Ubah Data" )
        nama = input("Masukkan Nama Mahasiswa   : ")
        if  nama in  x . keys ():
            nim = input("Masukkan NIM              : ")
            tugas = int(input("Masukkan Nilai Tugas      : "))
            uts = int(input("Masukkan Nilai UTS        : "))
            uas = int(input("Masukkan Nilai UAS        : "))
            akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
            x[nama] = nim , tugas, uts , uas , akhir
        else :
            print ( "Nama{0} Tidak Ditemukan" . format(nama ))

    elif  c . lower () ==  'h' :
        print ( "Hapus Data" )
        nama = input("Masukkan Nama Mahasiswa   : ")
        if  nama in  x . keys ():
            del  x [ nama ]
        else :
            print ( "Nama {0} Tidak Ditemukan" . format ( nama ))

    elif  c . lower () ==  'c' :
        print ( "Cari Data" )
        nama  =  input ( "Masukkan Nama : " )
        if  nama in  x . keys ():
            print("---------------------------------------------------------------------------------")
            print("\n                               DAFTAR NILAI MAHASISWA                    ")
            print("---------------------------------------------------------------------------------")
            print("|      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
            print("---------------------------------------------------------------------------------")
            print("| {0:14s} | {1:11s} | {2:7d} | {3:7d} | {4:7d} | {5:7f}   |"
                . format(nama, nim, uts,uas, tugas, akhir))
            print("---------------------------------------------------------------------------------")
        else :
            print ( "Nama {0} Tidak Ditemukan" . format ( nama ))

    elif c.lower() == 'l':
        if x.items():
            print("---------------------------------------------------------------------------------")
            print("\n                               DAFTAR NILAI MAHASISWA                    ")
            print("---------------------------------------------------------------------------------")
            print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
            print("---------------------------------------------------------------------------------")
            i = 0                                                                         
            for b in x.items():                                                             
                i += 1
                print("| {no:2d} | {0:14s} | {1:11s} | {2:7d} | {3:7d} | {4:7d} | {5:7f}   |"
                    . format ( b [ 0 ][: 14 ], b [ 1 ][ 0 ], b [ 1 ][ 1 ], b [ 1 ][ 2 ], b [ 1 ][ 3 ], b [ 1 ][ 4 ] , no = i ))
            print("---------------------------------------------------------------------------------")
        else :
            print("---------------------------------------------------------------------------------")
            print("\n                               DAFTAR NILAI MAHASISWA                    ")
            print("---------------------------------------------------------------------------------")
            print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
            print("---------------------------------------------------------------------------------")
            print("|                                TIDAK ADA DATA                                 |")
            print("---------------------------------------------------------------------------------")

    elif  c . lower() ==  'k' :
        break
    else :
        print("Kode Salah")