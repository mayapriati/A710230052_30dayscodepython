prodi = 'Pendidikan Teknik Informatika'

nama_depan = input('Masukkan Nama Depan: ')
nama_belakang = input('Masukkan Nama Belakang: ')
nama_lengkap = ''.join([nama_depan,nama_belakang])

print('----------------------------------------------------------------')

nim = 'A710230052'
fkip = 'Fakultas Keguruan dan Ilmu Pendidikan'
univ = 'universitas muhammadiyah surakarta'

print(prodi.center(50))
print('Nama :', nama_lengkap)
print('NIM : {}'. format(nim))
print(fkip)
kapital = univ.upper()
print(kapital.center(50))
