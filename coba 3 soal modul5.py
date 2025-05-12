# Input jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa praktikum ADP: "))

# Data mahasiswa dalam array satu dimensi 
data = []

i = 0
while i < jumlah:
    print("\nMahasiswa ke-", i+1)
    nama = input("Nama: ")
    pretest = float(input("Nilai pretest: "))
    posttest = float(input("Nilai posttest: "))
    makalah = float(input("Nilai makalah: "))

    # Hitung nilai akhir
    nilai_akhir = (0.4 * pretest) + (0.4 * posttest) + (0.2 * makalah)

    # Simpan ke array
    data.append(nama)
    data.append(nilai_akhir)

    i = i + 1

# Tampilkan tabel nama dan nilai akhir
print("\n--- TABEL NILAI MAHASISWA ---")
j = 0
while j < len(data):
    print("Nama:", data[j], "  | Nilai Akhir:", data[j+1])
    j = j + 2

# Hitung rata-rata
total = 0
jumlah_mahasiswa = 0
k = 1
while k < len(data):
    total = total + data[k]
    jumlah_mahasiswa = jumlah_mahasiswa + 1
    k = k + 2

rata_rata = total / jumlah_mahasiswa
print("\nRata-rata nilai akhir kelas:", rata_rata)

# Cari nilai tertinggi dan terendah
max_nilai = data[1]
min_nilai = data[1]
j = 1
while j < len(data):
    if data[j] > max_nilai:
        max_nilai = data[j]
    if data[j] < min_nilai:
        min_nilai = data[j]
    j = j + 2

# Cari nama yang dapat nilai tertinggi & terendah
print("\nMahasiswa dengan nilai tertinggi:")
j = 1
while j < len(data):
    if data[j] == max_nilai:
        print(data[j-1], "dengan nilai", data[j])
    j = j + 2

print("Mahasiswa dengan nilai terendah:")
j = 1
while j < len(data):
    if data[j] == min_nilai:
        print(data[j-1], "dengan nilai", data[j])
    j = j + 2

# Mahasiswa yang nilainya di atas rata-rata
print("\nMahasiswa dengan nilai di atas rata-rata:")
j = 1
while j < len(data):
    if data[j] > rata_rata:
        print(data[j-1], "dengan nilai", data[j])
    j = j + 2
mahasiswa = []

