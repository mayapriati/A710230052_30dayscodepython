#Hitung tahun kelahiran penumpang
tahun_kelahiran = int(input("Masukkan tahun kelahiran penumpang: "))

#Hitung harga tiket Kereta Api
harga_tiket = float(input("Masukkan harga tiket: "))

#Hitung usia penumpang
tahun_sekarang = 2023
usia = tahun_sekarang - tahun_kelahiran

#Variabel diskon
diskon = 0

if (usia >= 0 and usia <= 4):
        diskon = 1.0
elif (usia >= 5 and usia <= 11):
        diskon = 0.5
else:
        diskon = 0.0

#Hitung total harga setelah diskon
harga_setelah_diskon = harga_tiket*(1-diskon)

#output hasil
print(f'Diskon: {diskon*100}%')
print(f'Total harga setelah diskon: Rp {harga_setelah_diskon: }')