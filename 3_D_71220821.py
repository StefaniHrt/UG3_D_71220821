awal=int(input("Masukkan awal deret:"))
akhir=int(input("Masukkan akhir deret:"))
for angka in range(awal,akhir):
    print(angka, end=" ") if (angka%6!=0) and (angka%8!=0) else not print