# Input data mahasiswa
def input_data():
    n = int(input("Masukkan jumlah mahasiswa: "))
    data = []
    for i in range(n):
        print("\nMahasiswa ke-", i+1)
        nama = input("Nama: ")
        nim = int(input("NIM: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        tugas = float(input("Nilai Tugas: "))
        data.append([nama, nim, uts, uas, tugas])
    return data

# Hitung rata-rata dari kolom tertentu
def rata(data, index):
    total = 0
    for i in range(len(data)):
        total += data[i][index]
    return total / len(data)

# Tambah nilai akhir ke data
def tambah_nilai_akhir(data):
    for i in range(len(data)):
        uts = data[i][2]
        uas = data[i][3]
        tugas = data[i][4]
        akhir = 0.35 * uts + 0.35 * uas + 0.3 * tugas
        data[i].append(akhir)

# Urutkan berdasarkan nilai akhir (index ke-5) dan tambah peringkat
def urutkan_dan_peringkat(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i][5] < data[j][5]:
                var = data[i]
                data[i] = data[j]
                data[j] = var
    for i in range(len(data)):
        data[i].append(i+1)

# Tampilkan tabel
def tampil(data, rata2_uts, rata2_uas, rata2_tugas, rata2_akhir):
    print("\n" + "="*80)
    print("{:<15}{:<10}{:<10}{:<10}{:<12}{:<13}{:<9}".format(
        "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Peringkat"))
    print("-"*80)
    for i in range(len(data)):
        print("{:<15}{:<10}{:<10}{:<10}{:<12}{:<13.2f}{:<9}".format(
            data[i][0], data[i][1], data[i][2], data[i][3],
            data[i][4], data[i][5], data[i][6]))
    print("-"*80)
    print("{:<15}{:<10}{:<10.2f}{:<10.2f}{:<12.2f}{:<13.2f}".format(
        "RATA-RATA", "", rata2_uts, rata2_uas, rata2_tugas, rata2_akhir))
    print("="*80)


# Jalankan langkah-langkah
data = input_data()
tambah_nilai_akhir(data)
urutkan_dan_peringkat(data)

# Hitung rata-rata
rata2_uts = rata(data, 2)
rata2_uas = rata(data, 3)
rata2_tugas = rata(data, 4)
rata2_akhir = rata(data, 5)

# Tampilkan
tampil(data, rata2_uts, rata2_uas, rata2_tugas, rata2_akhir)