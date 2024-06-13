def apakah_prima(angka):
    # Bilangan prima harus lebih besar dari 1
    if angka > 1:
        # Periksa faktor-faktor dari 2 hingga akar kuadrat dari angka
        for i in range(2, int(angka**0.5) + 1):
            if (angka % i) == 0:
                print("Bukan Bilangan Prima")
                break
        else:
            print("Bilangan Prima")
    else:
        print("Bukan Bilangan Prima")

# Contoh penggunaan
bilangan = 17
apakah_prima(bilangan)
