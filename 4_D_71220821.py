nama=input("Masukkan nama lengkap anda:")
prodi=input("Masukkan prodi anda:")
nilai=input("Masukkan nilai (dalam huruf) yang anda dapat:")
try:
    if nilai=="A":
        print("nilai anda 4.0, tbl tbl serem banget lohh")
    elif nilai=="A-":
        print("nilai anda 3.75, kamu keren!")
    elif nilai=="B+":
        print("nilai anda 3.25, udah bagus nih")
    elif nilai=="B":
        print("nilai anda 3.0, ayo tingkatin lagi") 
    elif nilai=="B-":
        print("nilai anda 2.75, kurang semangat belajar nihh")
    elif nilai=="C+":
        print("nilai anda 2.25, belajar yang bener lain kali")
    elif nilai=="C":
        print("nilai anda 2.0, semoga ketemu lagi")
    elif nilai=="D":
        print("nilai anda 1.0, apakah sudah ada pikiran pindah jurusan?")
    elif nilai=="E":
        print("nilai anda 0, niat kuliah gk sih???")
    else:
        print("Inputan nilai yang anda masukkan tidak valid")
except:
    print("Tidak dapat dibaca")