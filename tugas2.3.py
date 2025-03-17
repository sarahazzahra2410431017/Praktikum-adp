print("========ANGKA BOM=========")
print("pemain 1")
n=int(input("masukkan batas angka positif :"))
k=int(input("pilih angka bomnya :"))
for i in range(1,n+1):
    if i%k==0:
        print("BOM", end=" " )
    else:
        print(i, end=" " )
print("\n")
print("pemain 2")
for i in range(1,n+1):
    tebakan=int(input("tebak angka bom:"))
    if 1<=tebakan<=n:
        break
    else:
        print(f"angka yang dimasukkan harus dari 1 sampai {n}. silahkan ulang lagi")
for i in range (1,n+1):
    if tebakan %k==0:
        print(f"BOM angka {tebakan} salah. pemain 2 kalah")
        break
    else:
        print(f"selamat angka {tebakan} bukan bom. pemain 2 menang")
        break
