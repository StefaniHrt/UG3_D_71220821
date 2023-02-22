plat=input("Masukkan Plat Nomor:").split(" ")
try:
    p=int(plat[1])
    if p>=0 and p<=3000:
        print("Plat nomor tersebut diperuntukkan untuk mobil")
    elif p>=3001 and p<=4000:
        print("Plat nomor tersebut diperuntukkan untuk motor")
    elif p>=4001 and p<=5000:
        print("Plat nomor tersebut diperuntukkan untuk angkutan umum")
    else :
        print("Plat nomor tidak terindikasi ketiga angkutan tersebut")
except:
    print("Plat nomor tidak terindikasi, setelah kode daerah harus berupa nomor kendaraan")