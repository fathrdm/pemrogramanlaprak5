def hitungan(nilai1, nilai2):
    nilai1=int(nilai1) 
    nilai2=int(nilai2)
    return nilai1 - nilai2
def mutlak(angka):
    angka = int(angka)
    return abs(angka)
a, c, b, d = map(int, input().split())
Hasil = hitungan(a, b) + hitungan(c, d)
print(mutlak(Hasil))