# nama = ["shandy", 106, True,
#         ["yuyun", 145],3.96,
#         [123,"ALVITO",False,3.66],
#         "rehan"]
# print(nama[4])
# matkul = ["APD",
#           "APL", 
#           "WEB", 
#           "JARKOM",
#           "BASDAT",
#           "STRUKDAT",
#           "PTI",
#           "KALKULUS",
#           "PROBAS"
# ]

# print(matkul[6])

# makanan = ["Bakso", "Sate", "Soto","nasi goreng","mie ayam","ayam bakar","cumi goreng"]
# print("sebelum: ")
# print(makanan)
# makanan.append("Nasi Goreng")
# print("Sesudah: ")
# data = makanan.pop(5)
# print(makanan)
# print(data)
# makanan.insert(2,"Nasi Goreng") 
# makanan[2] = ["AYAM","BEBEK"] # MENGUBAH
# print(makanan)
# makanan.clear()
# print(makanan)


# Muhammad Kurniawan
# minuman 6. 3(dihapus) 6(air putih) 1(jus tomat)

# minuman = ["Sprite","Fanta","Coca Cola","Teh","Mineral","Kopi"]
# print("sebelum: ")
# print(minuman)

# print("sesudah: ")
# minuman.append("Air putih")
# print(minuman)

# print("sesudah: ")
# minuman.insert(1, "Jus Tomat")
# print(minuman)

# print("sesudah: ")
# del minuman[2]
# print(minuman)

# print("sesudah: ")
# minuman[2] = "Muhammad Kurniawan"


# Abhista
# minuman = ["susu","jus mangga","jus sirsak",
#            "es teler","es teh","es buah"]
# print("sebelum: ")
# print(minuman)
# del minuman[2]
# print("sesudah: ")
# print(minuman)
# minuman[4] ="air putih"
# print(minuman)
# minuman.insert(0,"Jus Tomat")
# print(minuman)

# makanan = [["bakso","soto","sate","ikan","bebek"],["teh","kopi","air"]]

# for i in makanan :
#     for j in i : 
#         print(j, end=", ")


# makanan = ["ayam","ikan", ["bakso","soto","sate","ikan","bebek"],
#            ["teh","kopi","air"]]

# for i in makanan :
#     if isinstance(i, list):
#         for j in i : 
#             print(j)
#     else:
#         print(i)
# for i in makanan : 
#     for j in i :
#         print(j)

# akuns = []

# while True:
#     print("Halo! selamat datang di aplikasi catatan")
#     print("Silahkan pilih 'daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan login")
#     print("1. Daftar akun")
#     print("2. Login")
#     print("3. Exit")
#     print("______________________")
#     opsi = input("Pilih Opsi: ")
#     print(" ")

#     if opsi == "1":
#         print("Halo Pengguna baru! Ayo buat akun dulu")
#         Username = input("Username: ")
#         akuna = False
#         for akun in akuns:
#             if akun[0] == Username:  # Memeriksa apakah username sudah ada
#                 akuna = True
#                 break
#     if akuna: 
#         print("Nama Sudah Terpakai unutk Registrasi Silahkan Coba Lagi")
#     else:
#         Password = input("Password: ")
#         akuns.append([Username, Password, []]) #Simpan USername, password dan catatan (sebagai list kosong)
#         print(f"Akun Anda Berhasil Terdaftar Dengan ID: {Username}")