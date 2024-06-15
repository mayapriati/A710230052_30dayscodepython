class Mahasiswa():
    def __init__ (self, nim, nama, angkatan, prodi):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.prodi = prodi 
    def kartu_mahasiswa (self):
        print(f"Data Mahasiswa\n NIM: {self.nim}\n Nama: {self.nama}\n Angkatan: {self.angkatan}\n Prodi: {self.prodi}\n")
    def selamat (self):
        print(f"Selamat datang {self.nama} di kampus UMS")
Kartu_saya = Mahasiswa("A710230052", "Maya", 2023, "PTI")
mahasiswa1 = Mahasiswa("A710230001", "Isma", 2022, "Teknik Informatika")
mahasiswa2 = Mahasiswa("A710230002", "Arief", 2023, "Manajemen")
Kartu_saya.kartu_mahasiswa()
Kartu_saya.selamat()
mahasiswa1.kartu_mahasiswa()
mahasiswa1.selamat()
mahasiswa2.kartu_mahasiswa()
mahasiswa2.selamat()