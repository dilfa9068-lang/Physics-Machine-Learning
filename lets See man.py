import math

L = 5
C = 10e-4
t = 0.05

def f(R):
    try:
        # Perbaikan kurung pada pembagi (2*L)
        suku_1 = math.exp(-R * t / (2 * L)) # Asumsi peluruhan (negatif)
        
        # Cek apakah nilai dalam akar negatif untuk menghindari error
        isi_akar = (1 / (L * C)) - (R / (2 * L))**2
        if isi_akar < 0: return 1e10 
        
        suku_2 = math.sqrt(isi_akar)
        suku_3 = math.cos(t * suku_2)
        return (suku_1 * suku_3) - 0.01 # Contoh target f(R)=0.01, sesuaikan dengan soal
    except ZeroDivisionError:
        return 1e10

def Bisection_method(batas_bawah, batas_atas, error_target):
    # Cek syarat awal: f(a) dan f(b) harus beda tanda
    if (f(batas_bawah) * f(batas_atas)) >= 0:
        return None

    R_sekarang = 0
    ea = 100
    iterasi = 0

    while ea > error_target:
        iterasi += 1
        R_lama = R_sekarang
        R_sekarang = (batas_atas + batas_bawah) / 2
        
        if R_sekarang != 0:
            ea = abs((R_sekarang - R_lama) / R_sekarang) * 100
        
        # LOGIKA INI YANG PENTING: Update batasnya, bukan variabel R_sekarang
        if f(batas_bawah) * f(R_sekarang) < 0:
            batas_atas = R_sekarang
        else:
            batas_bawah = R_sekarang

    return R_sekarang

# Eksekusi
hasil = Bisection_method(320, 340, 1e-7)
if hasil:
    print(f"Nilai resistansi (R) adalah: {hasil:.4f}")

