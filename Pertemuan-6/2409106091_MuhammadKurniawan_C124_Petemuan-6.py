# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
#  print(daftar_buku["Buku1"])
#  print(daftar_buku["Buku2"])
#  print(daftar_buku["Buku3"])


# Biodata = {
#     "Nama" : "Aldy Ramadhan Saputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahaiswa_Aktif" : True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848",
#         "Email" : "iniemail@gmail.com"
#     }
# }

# print(Biodata["KRS"[0]])
# print(Biodata["Social Media"]["Email"])


# Games = {
#     "Game1" : "PUBG Mobile",
#     "Game2" : "Mobile Legends",
#     "Game3" : "COC"
# }
# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = {"nama" : {123 : "informatika" }})
# print(games['Valorant']['nama'][123])

# Games = {
#     "Game1" : "PUBG Mobile",
#     "Game2" : "Mobile Legends",
#     "Game3" : { 
#         "nama" : "COC",
#         "genre" : "Strategy"
#     }
# }

# print((Games.get('Game3')).get('genre'))


# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")
# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller",
#              "Rush Hour" : "comedy",
#              "Obvilion" : "Science Fiction"})

# #Setelah Ditambah
# print(Film)

# Pengunaan del
# del Film["Avenger Endgame"]
# print(Film)
# simpan = Film.pop('Hours')
# Film.clear()
# print("Film")
# Film["Hours"] = simpan
# print(Film)
# print("Jumlah Film = ", len(Film))

# movies = Film.copy()
# print(movies)


# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)


# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "TheParis"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }

# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
# print("")


# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
# print("")


# Latihan
# Buatlah sebuah dictionary yang memiliki 5 key (Nama, Umur, NIM,
# Jurusan, Angkatan). Setelah itu buatlah dictionary ini dapat :
# -Menambahkan Item baru sesuai dengan inputan User
# -Mengubah salah satu key sesuai dengan inputan User
# -Menghapus salah satu key sesuai dengan Inputan user



# Membuat dictionary dengan data mata pelajaran dan nilainya
nilai_mata_pelajaran = {
    "Matematika": 90,
    "Fisika": 80,
    "Biologi": 80,
    "Kimia": 70
}

total = 0
for i in nilai_mata_pelajaran.values(): 
    total += i
print(f"total nilai adalah {total}")
print(f"rata rata nilai adalah {total/4}")

# ATAU

# # Menghitung total nilai
# total_nilai = sum(nilai_mata_pelajaran.values())

# # Menghitung rata-rata nilai
# jumlah_mapel = len(nilai_mata_pelajaran)
# rata_rata_nilai = total_nilai / jumlah_mapel

# # Menampilkan hasil
# print("Jumlah Total Nilai Adalah:", total_nilai)
# print("Rata-rata Nilai:", rata_rata_nilai)