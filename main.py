# Judul program
print(18*"=","Mini Project 1(NIM ganjil)",18*"=")

# Membuat program login sederhana
# Data user yang sudah terdaftar
Nama_terdaftar = "Yardan Raditya Rafi' Widyadhana"
NIM_terdaftar = "2409116037"

# Input data user
ulang = True
while (ulang==True):
    print("\nMasukkan nama dan NIM anda")
    nama = input("Masukkan nama anda : ")
    NIM = input("Masukkan NIM anda : ")

# Mengecek apakah nama dan NIM sudah terdaftar atau belum
    if nama == Nama_terdaftar and NIM == NIM_terdaftar:
        print("------------------------------------------------------------------------------------")
        print("Login berhasil! Selamat datang",Nama_terdaftar,"dengan NIM",NIM_terdaftar)
        print("------------------------------------------------------------------------------------")
        break # Keluar dari loop jika login berhasil
    else:
        print("------------------------------------------------")
        print("Login gagal! Nama atau NIM salah.")
        print("------------------------------------------------")
    
# Input data karyawan
ulang = True
while (ulang==True):
    Jam_kerja = float(input("Masukkan jam kerja karyawan : "))
    Gaji = float(input("Masukkan total gaji karyawan : "))

# Mengecek apakah karyawan mendapatkan bonus gaji atau tidak
    if Jam_kerja > 160:
        Bonus = Gaji * 0.10
        Total_gaji = Gaji + Bonus
        print(f"\nJam kerja : {Jam_kerja} jam")
        print(f"Total gaji dengan bonus : {Total_gaji}")
        pilihan = True
        while (pilihan==True):
            t = str(input("\nApakah anda ingin menghitung gaji lagi? (ya/tidak) : "))
            if (t == "ya"):
                ulang = True
                pilihan = False
            elif (t == "tidak"):
                ulang = False
                pilihan = False
                print("--------------------------------------------------------------")
                print("Baiklah, terimakasih sudah menggunakan program ini ^-^")
                print("--------------------------------------------------------------")
    else:
        Total_gaji = Gaji
        print(f"\nJam kerja : {Jam_kerja} jam")
        print("Anda tidak mendapatkan bonus")
        print(f"Total gaji : {Total_gaji}")
        pilihan = True
        while (pilihan==True):
            t = str(input("\nApakah anda ingin menghitung gaji lagi? (ya/tidak) : "))
            if (t == "ya"):
                ulang = True
                pilihan = False
            elif (t == "tidak"):
                ulang = False
                pilihan = False
                print("--------------------------------------------------------------")
                print("Baiklah, terimakasih sudah menggunakan program ini ^-^")
                print("--------------------------------------------------------------")

# Program selesai