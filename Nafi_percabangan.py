# nama:Nafi
# kelas:XI TKJ 1
# no absen:16

# Input total belanjaan pelanggan
total_belanja = float(input("Masukkan total belanjaan pelanggan: "))

# Inisialisasi variabel diskon
diskon = 0

# Menghitung diskon berdasarkan aturan
if total_belanja > 500000:
    diskon = 0.10  # 10% diskon
elif 300000 <= total_belanja <= 500000:
    diskon = 0.05  # 5% diskon

# Menghitung jumlah diskon
jumlah_diskon = total_belanja * diskon

# Menghitung total bayar setelah diskon
total_bayar = total_belanja - jumlah_diskon

# Menampilkan hasil
print(f"Total belanjaan: Rp {total_belanja:,.2f}")
print(f"Diskon: Rp {jumlah_diskon:,.2f}")
print(f"Total bayar setelah diskon: Rp {total_bayar:,.2f}")