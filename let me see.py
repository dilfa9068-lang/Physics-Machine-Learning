P = 1
R = 0.082
T = 383
A = 24.06
B = 0.1463

def f(v):
    try:
        faktor_1 = (P + A / v**2)
        faktor_2 = (v - B)
        faktor_3 = R * T
        return faktor_1 * faktor_2 - faktor_3
    except ZeroDivisionError:
        return 1e10

def Bisection_method(batas_bawah, batas_atas, error_target):
    iterasi = 0
    v_sekarang = 0
    v_lama = 0
    ea = 100
    if f(batas_bawah) * f(batas_atas) > 0:
        return None

    while True:
        iterasi = iterasi + 1 # Perbaikan nama variabel (hapus 'l')
        v_lama = v_sekarang 
        v_sekarang = (batas_atas + batas_bawah) / 2
        
        if v_sekarang != 0:
            # Perbaikan rumus error relatif
            ea = abs((v_sekarang - v_lama) / v_sekarang) * 100

        # Update batas
        if f(v_sekarang) * f(batas_bawah) > 0:
            batas_bawah = v_sekarang
        else:
            batas_atas = v_sekarang
            
        # Cek kriteria berhenti
        if ea < error_target:
            break
    return v_sekarang
hasil = Bisection_method(0.5, 50, 0.01)
if hasil is None:
    print(f"Hasil faktor v adalah: {hasil:.4f}")

