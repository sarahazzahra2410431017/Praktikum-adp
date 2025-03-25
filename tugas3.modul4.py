while True:
    r = int(input("Masukkan jumlah baris kursi (minimal 4): "))
    c = int(input("Masukkan jumlah kolom kursi (minimal 4): "))
    if r >= 4 and c >= 4:
        break
    else:
        print("Ukuran kursi minimal 4x4. Silakan coba lagi.")

kursi_tersedia = r * c
kursi_dipesan = 0 

while True:
    print("\nLayout Kursi Bioskop:")
    nomor = 1
    for i in range(r):
        for j in range(c):
            if kursi_dipesan % (10 ** nomor) >= 10 ** (nomor - 1):
                print("X", end="\t")
            else:
                print(nomor, end="\t")
            nomor += 1
        print()  

    nomor_kursi = int(input(f"Masukkan nomor kursi yang ingin dipesan (1-{r * c}, 0 untuk berhenti): "))

    if nomor_kursi == 0:
        print("Terima kasih telah menggunakan layanan pemesanan tiket bioskop.")
        break

    elif nomor_kursi < 1 or nomor_kursi > r * c:
        print("Nomor kursi tidak valid. Silakan coba lagi.")
        continue

    elif kursi_dipesan % (10 ** nomor_kursi) >= 10 ** (nomor_kursi - 1): 
        print("Kursi sudah dipesan. Silakan pilih kursi lain.")
    else:
        kursi_dipesan += 10 ** (nomor_kursi - 1) 
        kursi_tersedia -= 1
        print(f"Kursi {nomor_kursi} berhasil dipesan.")

    print(f"Jumlah kursi tersedia: {kursi_tersedia}\n")
