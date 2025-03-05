def inisialisasi_matriks_simpleks(matriks_awal):
    return [baris[:] for baris in matriks_awal]

def cari_kolom_pivot(matriks):
    return matriks[0].index(min(matriks[0][:-1]))

def cari_baris_pivot(matriks, kolom_pivot):
    rasio = []
    for i in range(1, len(matriks)):
        if matriks[i][kolom_pivot] > 0:
            rasio.append(matriks[i][-1] / matriks[i][kolom_pivot])
        else:
            rasio.append(float('inf'))
    return rasio.index(min(rasio)) + 1

def lakukan_operasi_baris(matriks, baris_pivot, kolom_pivot):
    pivot = matriks[baris_pivot][kolom_pivot]
    matriks[baris_pivot] = [x / pivot for x in matriks[baris_pivot]]
    
    for i in range(len(matriks)):
        if i != baris_pivot:
            faktor = matriks[i][kolom_pivot]
            matriks[i] = [matriks[i][j] - faktor * matriks[baris_pivot][j] for j in range(len(matriks[i]))]

def metode_simpleks(matriks_awal):
    matriks = inisialisasi_matriks_simpleks(matriks_awal)
    
    while any(x < 0 for x in matriks[0][:-1]):
        kolom_pivot = cari_kolom_pivot(matriks)
        baris_pivot = cari_baris_pivot(matriks, kolom_pivot)
        lakukan_operasi_baris(matriks, baris_pivot, kolom_pivot)
    
    return matriks

# Contoh pemanggilan metode simpleks
data_matriks = [
    [1, -3, -5, 0, 0, 0, 0],
    [0, 1,  1, 1, 0, 0, 4],
    [0, 2,  0.5, 0, 1, 0, 6],
    [0, 0,  1, 0, 0, 1, 3]
]

hasil = metode_simpleks(data_matriks)
print("Matriks Akhir setelah Simpleks:")
for baris in hasil:
    print([round(x, 2) for x in baris])
