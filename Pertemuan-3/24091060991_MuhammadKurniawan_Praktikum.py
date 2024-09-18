cuaca = int(input("masukan cuaca hari ini"))

if cuaca == "mendung":
    print("diam di rumah")
else: 
     print("hari ini mendung")
     


Umur = int(input("Masukan Umur anda : "))
if Umur > 0:
    if Umur <= 10: 
        print("Umur anda termasuk kategori anak-anak")
    elif Umur <= 18: 
        print("umur anda termasuk lategori remaja")
    elif Umur <= 35:
        print("Umur anda termasuk kategori dewasa")
    elif Umur <= 65: 
        print("Umur anda termasuk kategori paruh baya")
    else:
        print("Umur anda termasuk kategori tua")
else:
    print("input usia harus bilangan positif")

nim = int(input("masukan nim: "))



if nim >= 1 and nim <= 50 :
    if nim >= 1 and nim <= 25 : 
        print("kelas A'1")
    else :
        print("kelas A'2")
elif nim >=51 and nim <= 100: 
    if nim >= 51 and nim <= 75 : 
        print("kelas B'1")
    else :
        print("kelas B'2")
elif nim >= 101 and nim <= 121 : 
    if nim >= 101 and nim <= 110 : 
        print("kelas C'1")
    else : 
        print("kelas C'2")
else : 
    print("Anda bukan mahasiswa informatika 24")



angka = int(input("Masukkan angka: "))
result = "Genap" if angka % 2 == 0 else "Ganjil"
print(angka, "adalah angka",result)

    

nim = int(input("Masukan nim"))
hasil = "Kelas A" if nim >= 1 and nim <= 50 else "Kelas B" if nim >= 51 and nim <= 100 else "Kelas C" if nim >= 101 and nim <= 121 else "mahasiswa siluman"
print(hasil)