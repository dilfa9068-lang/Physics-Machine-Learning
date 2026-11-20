
import math

P = 1
T = 383
R = 0.082
A = 24.06
B = 0.1463

def f(v):
    try:
        faktor_1 = R * T
        faktor_2 = v - B
        faktor_3 = P + A / v**2
        return (faktor_3 * faktor_2) - faktor_1
    except ZeroDivisionError:
        return 1e10

def bisection_method(batas_bawah, batas_atas, target_error):
    if f(batas_bawah) * f(batas_atas) >= 0:
        return None

    v_sekarang = 0
    v_lama = 0
    iterasi = 0
    while True:
        v_lama = v_sekarang
        v_sekarang = (batas_atas + batas_bawah) / 2
        iterasi += 1
        ea = 100
        if v_sekarang != 0:
            ea = abs((v_sekarang - v_lama) / v_sekarang) * 100
        if f(batas_bawah) * f(v_sekarang) < 0:
            batas_atas = v_sekarang 
        else:
            batas_bawah = v_sekarang 
        
        if ea < target_error:
            break
            
    return v_sekarang
hasil = bisection_method(1, 50, 0.01)

if hasil:
    print(f"Hasil volume jenis (v): {hasil:.4f}")