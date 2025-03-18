nama=input("silahkan masukkan nama anda:",)
umur=int(input("silahkan masukkan umur anda:",))
jenis_kelamin=input("pilih P atau L:",)
print("\n")
print("kode penerbangan , tujuan       ,ekonomi   ,bisnis    ,first class"),print("3012             ,padang jakarta,Rp.800000 ,Rp.850000 ,Rp.900000"),
print("4015             ,padang batam  ,Rp.500000 ,Rp.550000 ,Rp.700000"),print("4050             ,padang bandung,Rp.700000 ,Rp.750000 ,Rp.850000")
print("\n")
kode_kelas=input("kode_kelas=")
if kode_kelas== "3012_ekonomi":
    print("jakarta")
    harga= 800000
elif kode_kelas== "3012_bisnis":
    print("jakarta")
    harga= 850000
elif kode_kelas== "3012_first class":
    print("jakarta")
    harga= 900000
elif kode_kelas== "4015_ekonomi":
    print("batam")
    harga= 500000
elif kode_kelas== "4015_bisnis":
    print("batam")
    harga= 550000
elif kode_kelas == "4015_first class":
    print("batam")
    harga= 700000
elif kode_kelas== "4050_ekonomi":
    print("bandung")
    harga= 700000
elif kode_kelas== "4050_bisnis":
    print("bandung")
    harga= 750000
elif kode_kelas == "4050_first class":
    print("bandung")
    harga= 850000
jumlah=int(input("jumlah beli tiket:"))
#print()
if jumlah >= 3:
    potongan= (jumlah*harga)*0.20
else:
    potongan =0
total = int(jumlah*harga-potongan)
jumlah_bayar=total

print("==================================")
print("nama         :", nama)
print("umur         :", umur)
print("jenis kelamin:", jenis_kelamin)
print("kode_kelas  :", kode_kelas)
print("==================================")
print("jumlah beli :",jumlah)
print("harga tiket :Rp",harga)
print("potongan    :Rp", potongan)
print("jumlah bayar:Rp",jumlah_bayar)
print("============terimakasi============")





