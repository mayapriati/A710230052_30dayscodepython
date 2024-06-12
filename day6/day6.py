teman = []

for i in range (1, 6):
    nama = input(f'Masukkan Nama ke-{i}: ')
    no_hp = input(f'Masukkan no hp {nama}: ')
    teman.append((nama, no_hp))

    print()
    kalimat = 'Phone Book'
    print(kalimat.center(50))
    print()
    for i in range(5):
        nama, no_hp = teman [i]
        print(f'{i + 1}. [{nama}] = [{no_hp}]')