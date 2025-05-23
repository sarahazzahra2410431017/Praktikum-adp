while True:
    print("TAMPILAN 1: INPUT MATRIKS")
    
    # Input ukuran matriks pertama
    print("Masukkan jumlah baris matriks pertama: ")
    baris_pertama = int(input())
    print("Masukkan jumlah kolom matriks pertama: ")
    kolom_pertama = int(input())
    
    # Input ukuran matriks kedua
    print("Masukkan jumlah baris matriks kedua: ")
    baris_kedua = int(input())
    print("Masukkan jumlah kolom matriks kedua: ")
    kolom_kedua = int(input())
    
    # Input elemen matriks pertama
    print("\nInput elemen matriks pertama:")
    matriks_pertama = []
    for i in range(baris_pertama):
        baris = []
        for j in range(kolom_pertama):
            print(f"Matriks pertama [{i+1}][{j+1}]: ", end='')
            nilai = float(input())
            baris.append(nilai)
        matriks_pertama.append(baris)
    
    # Input elemen matriks kedua
    print("\nInput elemen matriks kedua:")
    matriks_kedua = []
    for i in range(baris_kedua):
        baris = []
        for j in range(kolom_kedua):
            print(f"Matriks kedua [{i+1}][{j+1}]: ", end='')
            nilai = float(input())
            baris.append(nilai)
        matriks_kedua.append(baris)
    
    while True:
        print("\nTAMPILAN 2: MENU OPERASI")
        print("1. Penjumlahan matriks")
        print("2. Pengurangan matriks")
        print("3. Perkalian matriks")
        print("4. Determinan matriks")
        print("5. Invers matriks")
        print("6. Transpose matriks")
        print("7. Keluar")
        print("Pilih operasi (1-7): ")
        pilihan = int(input())
        
        if pilihan == 1:  # Penjumlahan
            if baris_pertama == baris_kedua and kolom_pertama == kolom_kedua:
                hasil = []
                for i in range(baris_pertama):
                    baris_hasil = []
                    for j in range(kolom_pertama):
                        baris_hasil.append(matriks_pertama[i][j] + matriks_kedua[i][j])
                    hasil.append(baris_hasil)
                
                print("\nHasil Penjumlahan:")
                for baris in hasil:
                    for nilai in baris:
                        print(f"{nilai:8.2f}", end=' ')
                    print()
            else:
                print("Ukuran matriks tidak sama!")
        
        elif pilihan == 2:  # Pengurangan
            if baris_pertama == baris_kedua and kolom_pertama == kolom_kedua:
                hasil = []
                for i in range(baris_pertama):
                    baris_hasil = []
                    for j in range(kolom_pertama):
                        baris_hasil.append(matriks_pertama[i][j] - matriks_kedua[i][j])
                    hasil.append(baris_hasil)
                
                print("\nHasil Pengurangan:")
                for baris in hasil:
                    for nilai in baris:
                        print(f"{nilai:8.2f}", end=' ')
                    print()
            else:
                print("Ukuran matriks tidak sama!")
        
        elif pilihan == 3:  # Perkalian
            if kolom_pertama == baris_kedua:
                hasil = []
                for i in range(baris_pertama):
                    baris_hasil = []
                    for j in range(kolom_kedua):
                        total = 0
                        for k in range(kolom_pertama):
                            total += matriks_pertama[i][k] * matriks_kedua[k][j]
                        baris_hasil.append(total)
                    hasil.append(baris_hasil)
                
                print("\nHasil Perkalian:")
                for baris in hasil:
                    for nilai in baris:
                        print(f"{nilai:8.2f}", end=' ')
                    print()
            else:
                print("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua!")
        
        elif pilihan == 4:  # Determinan
            # Determinan matriks pertama
            if baris_pertama == kolom_pertama:
                ukuran = baris_pertama
                salinan_matriks = [baris[:] for baris in matriks_pertama]
                det = 1
                
                for i in range(ukuran):
                    if salinan_matriks[i][i] == 0:
                        for j in range(i+1, ukuran):
                            if salinan_matriks[j][i] != 0:
                                salinan_matriks[i], salinan_matriks[j] = salinan_matriks[j], salinan_matriks[i]
                                det = -det
                                break
                    
                    if salinan_matriks[i][i] == 0:
                        det = 0
                        break
                    
                    det *= salinan_matriks[i][i]
                    for j in range(i+1, ukuran):
                        faktor = salinan_matriks[j][i] / salinan_matriks[i][i]
                        for k in range(i, ukuran):
                            salinan_matriks[j][k] -= faktor * salinan_matriks[i][k]
                
                print(f"\nDeterminan matriks pertama: {det:.2f}")
            else:
                print("Matriks pertama harus persegi untuk menghitung determinan")
            
            # Determinan matriks kedua
            if baris_kedua == kolom_kedua:
                ukuran = baris_kedua
                salinan_matriks = [baris[:] for baris in matriks_kedua]
                det = 1
                
                for i in range(ukuran):
                    if salinan_matriks[i][i] == 0:
                        for j in range(i+1, ukuran):
                            if salinan_matriks[j][i] != 0:
                                salinan_matriks[i], salinan_matriks[j] = salinan_matriks[j], salinan_matriks[i]
                                det = -det
                                break
                    
                    if salinan_matriks[i][i] == 0:
                        det = 0
                        break
                    
                    det *= salinan_matriks[i][i]
                    for j in range(i+1, ukuran):
                        faktor = salinan_matriks[j][i] / salinan_matriks[i][i]
                        for k in range(i, ukuran):
                            salinan_matriks[j][k] -= faktor * salinan_matriks[i][k]
                
                print(f"Determinan matriks kedua: {det:.2f}")
            else:
                print("Matriks kedua harus persegi untuk menghitung determinan")
        
        elif pilihan == 5:  # Invers
            # Invers matriks pertama
            if baris_pertama == kolom_pertama:
                ukuran = baris_pertama
                matriks_perluasan = []
                
                for i in range(ukuran):
                    baris_perluasan = matriks_pertama[i][:] + [1.0 if j == i else 0.0 for j in range(ukuran)]
                    matriks_perluasan.append(baris_perluasan)
                
                for i in range(ukuran):
                    if matriks_perluasan[i][i] == 0:
                        for j in range(i+1, ukuran):
                            if matriks_perluasan[j][i] != 0:
                                matriks_perluasan[i], matriks_perluasan[j] = matriks_perluasan[j], matriks_perluasan[i]
                                break
                    
                    if matriks_perluasan[i][i] == 0:
                        print("\nMatriks pertama tidak memiliki invers!")
                        break
                    
                    elemen_poros = matriks_perluasan[i][i]
                    for j in range(i, 2*ukuran):
                        matriks_perluasan[i][j] /= elemen_poros
                    
                    for k in range(ukuran):
                        if k != i and matriks_perluasan[k][i] != 0:
                            pengali = matriks_perluasan[k][i]
                            for j in range(i, 2*ukuran):
                                matriks_perluasan[k][j] -= pengali * matriks_perluasan[i][j]
                else:
                    invers = [baris[ukuran:] for baris in matriks_perluasan]
                    print("\nInvers matriks pertama:")
                    for baris in invers:
                        for nilai in baris:
                            print(f"{nilai:8.2f}", end=' ')
                        print()
            else:
                print("Matriks pertama harus persegi untuk memiliki invers")
            
            # Invers matriks kedua
            if baris_kedua == kolom_kedua:
                ukuran = baris_kedua
                matriks_perluasan = []
                
                for i in range(ukuran):
                    baris_perluasan = matriks_kedua[i][:] + [1.0 if j == i else 0.0 for j in range(ukuran)]
                    matriks_perluasan.append(baris_perluasan)
                
                for i in range(ukuran):
                    if matriks_perluasan[i][i] == 0:
                        for j in range(i+1, ukuran):
                            if matriks_perluasan[j][i] != 0:
                                matriks_perluasan[i], matriks_perluasan[j] = matriks_perluasan[j], matriks_perluasan[i]
                                break
                    
                    if matriks_perluasan[i][i] == 0:
                        print("\nMatriks kedua tidak memiliki invers!")
                        break
                    
                    elemen_poros = matriks_perluasan[i][i]
                    for j in range(i, 2*ukuran):
                        matriks_perluasan[i][j] /= elemen_poros
                    
                    for k in range(ukuran):
                        if k != i and matriks_perluasan[k][i] != 0:
                            pengali = matriks_perluasan[k][i]
                            for j in range(i, 2*ukuran):
                                matriks_perluasan[k][j] -= pengali * matriks_perluasan[i][j]
                else:
                    invers = [baris[ukuran:] for baris in matriks_perluasan]
                    print("\nInvers matriks kedua:")
                    for baris in invers:
                        for nilai in baris:
                            print(f"{nilai:8.2f}", end=' ')
                        print()
            else:
                print("Matriks kedua harus persegi untuk memiliki invers")
        
        elif pilihan == 6:  # Transpose
            # Transpose matriks pertama
            transpose = []
            for j in range(kolom_pertama):
                baris = []
                for i in range(baris_pertama):
                    baris.append(matriks_pertama[i][j])
                transpose.append(baris)
            
            print("\nTranspose matriks pertama:")
            for baris in transpose:
                for nilai in baris:
                    print(f"{nilai:8.2f}", end=' ')
                print()
            
            # Transpose matriks kedua
            transpose = []
            for j in range(kolom_kedua):
                baris = []
                for i in range(baris_kedua):
                    baris.append(matriks_kedua[i][j])
                transpose.append(baris)
            
            print("\nTranspose matriks kedua:")
            for baris in transpose:
                for nilai in baris:
                    print(f"{nilai:8.2f}", end=' ')
                print()
        
        elif pilihan == 7:
            break
        
        else:
            print("Pilihan tidak valid")
    
    print("\nApakah Anda ingin menggunakan kalkulator lagi? (ya/tidak): ")
    jawaban = input()
    if jawaban == 'ya' or jawaban == 'y':
        continue
    else:
        print("Terima kasih telah menggunakan kalkulator matriks!")
        break