# def salam():
#     print("Halo selamat sore")

# salam()

# def penjumlahan():
#     hasil = 7+3
#     print (hasil)

# penjumlahan()



# def penjumlahan(a,b,c):
#     hasil = a+b+c
#     print(hasil)

# penjumlahan(3,6,8)


# def perkalian(a,b):
#     hasil = a*b
#     print(hasil)

# perkalian(5,3)

# def luas_persegi(sisi):
#     luas = sisi*sisi
#     print(f"Luas persegi: {luas}")

# sisi = int(input("Sisi persegi: "))

# luas_persegi(sisi)

# def volume_persegi(sisi):
#     volume = sisi*sisi*sisi
#     print(f"volume persegi: {volume}")

# sisi = int(input("sisi persegi: "))

# volume_persegi(sisi)


# def penjumlahan():
# a = int(input ("bilangan pertama: "))
# c = int(input ("bilangan kedua: "))
# a = int(input ("bilangan ketiga: "))







# def kali(a,b):
#     hasil = a*b
#     return hasil

# print(kali(5,3))

# def luas_persegi(sisi):
#     luas = sisi*sisi
#     return luas
# # rumus: sisi*sisi*sisi
# def volume_persegi(sisi): 
#     volume = luas_persegi(sisi)*sisi
#     print("volume persegi = ", volume)
# # pemanggilan fungsi
# volume_persegi(6)



# def penjumlahan(a):
#     hasil = a+a
#     return hasil

# def perkalian(a):
#     hasil = penjumlahan(a)*a
#     print(f"hasil perkaliannya adalah = {hasil}")

# a = int(input("masukan bilangan yang kamu inginkan: "))
# perkalian(a)

# a = 1
# b = 2

# def penjumlahan(a,b):
#     a= 5
#     b= 4
#     hasil = a+b   # prioritas nya yang lokal dlu klo tidak ad yg lokal maka akan ke global

# penjumlahan(a,b)


# buku =[]
# def show_data():
#     if len(buku) <= 0:
#         print ("Belum Ada data")
#     else:
#         print("ID", "Nama Buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])
            
# fungsi untuk menambah data
# def insert_data():
#     buku_baru = input("Judul Buku : ")
#     buku.append(buku_baru)
    
# # fungsi untuk edit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         buku[indeks] = judul_baru
        
# # fungsi untuk menhapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         buku.remove(buku[indeks])
        
# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")
    
# while (True):
#     show_menu()