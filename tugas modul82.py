buku_list = [
    {
        "ISBN": "9786234567129",
        "Judul": "Belajar Matematika Seru",
        "Penulis": "Prof.Yohanes Surya",
        "Stok": 4,
        "Harga Beli": 60000,
        "Harga Jual": 95000},
    {
        "ISBN": "9789793062799",
        "Judul": "Negeri 5 Menara",
        "Penulis": "Ahmad Fuadi",
        "Stok": 10,
        "Harga Beli": 45000,
        "Harga Jual": 70000},
    {
        "ISBN": "9786230123456",
        "Judul": "The Power Of Doa",
        "Penulis": "Aa Gym",
        "Stok": 7,
        "Harga Beli": 60000,
        "Harga Jual": 100000},
    {
        "ISBN": "9786020381230",
        "Judul": "Bumi",
        "Penulis": "Tere Liye",
        "Stok": 6,
        "Harga Beli": 48000,
        "Harga Jual": 80000},
    {
        "ISBN": "9786020329607",
        "Judul": "Hujan",
        "Penulis": "Tere Liye",
        "Stok": 2,
        "Harga Beli": 50000,
        "Harga Jual": 82000},
    {
        "ISBN": "9786025678902",
        "Judul": "coding of Beginners",
        "Penulis": "Mark Zuckerberg",
        "Stok": 5,
        "Harga Beli": 100000,
        "Harga Jual": 180000},
    {
        "ISBN": "9786237890124",
        "Judul": "Seni Hidup Minimalis",
        "Penulis": "Marie Kondo",
        "Stok": 12,
        "Harga Beli": 70000,
        "Harga Jual": 125000},
    {
        "ISBN": "9786020321601",
        "Judul": "Perahu Kertas",
        "Penulis": "Dewi Lestari",
        "Stok": 5,
        "Harga Beli": 49000,
        "Harga Jual": 78000},
    {
        "ISBN": "9789799772123",
        "Judul": "Cantik itu Luka",
        "Penulis": "Eka Kurniawan",
        "Stok": 3,
        "Harga Beli": 75000,
        "Harga Jual": 100000},
    {
        "ISBN": "9786027890134",
        "Judul": "The Psychology Of Money",
        "Penulis": "Erisca Febriani",
        "Stok": 8,
        "Harga Beli": 90000,
        "Harga Jual": 150000}
]
file = open("laporan_inventaris.txt", "w")
file.write("ISBN,Judul,Penulis,Stok,Harga Beli,Harga Jual,Potensi Keuntungan\n")
for buku in buku_list:
    keuntungan = (buku["Harga Jual"] - buku["Harga Beli"]) * buku["Stok"]
    buku["Potensi Keuntungan"] = keuntungan
    baris = (
        f"{buku['ISBN']},{buku['Judul']},{buku['Penulis']},"
        f"{buku['Stok']},{buku['Harga Beli']},{buku['Harga Jual']},{keuntungan}\n")
    file.write(baris)
file.close()
tertinggi = buku_list[0]
terendah = buku_list[0]
total_nilai_inventaris = 0
restock = []
for buku in buku_list:
    if buku["Potensi Keuntungan"] > tertinggi["Potensi Keuntungan"]:
        tertinggi = buku
    if buku["Potensi Keuntungan"] < terendah["Potensi Keuntungan"]:
        terendah = buku
    total_nilai_inventaris += buku["Stok"] * buku["Harga Beli"]

    if buku["Stok"] < 5:
        restock.append(buku)
print("\nBuku dengan Potensi Keuntungan Tertinggi:")
print(f"{tertinggi['Judul']} - Rp{tertinggi['Potensi Keuntungan']}")
print("\nBuku dengan Potensi Keuntungan Terendah:")
print(f"{terendah['Judul']} - Rp{terendah['Potensi Keuntungan']}")
print(f"\nTotal Nilai Inventaris: Rp{total_nilai_inventaris}")
print("\nBuku yang Perlu Segera Di-Restock (Stok < 5):")
for buku in restock:
    print(f"- {buku['Judul']} (Stok: {buku['Stok']})")
