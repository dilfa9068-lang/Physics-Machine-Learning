import math as m
g = 9.81
M = 82
v = 36
t = 4
def f(c):
    faktor_1 = g*M/c
    faktor_2 = 1-m.exp(-c/M*t)
    return (faktor_1*faktor_2)-v
def bisection_methode(batas_bawah,batas_atas,error):
    iterasi = 0
    c_lama = 0
    c_terbaru = 0
    while True:
        c_lama = c_terbaru
        c_terbaru = (batas_bawah+batas_atas)/2
        error = 100
        if c_terbaru != 0:
            ea = abs((c_terbaru-c_lama)/c_terbaru)*100
        if f(batas_bawah)*f(c_terbaru)<0:
            batas_atas = c_terbaru
        else:
            batas_bawah = c_terbaru
        if ea<error:
            break
        return c_terbaru
f_terbaru = bisection_methode(batas_bawah=3,batas_atas=5,error=2)
print(f"nilai drag coeficient adalah:{f_terbaru:.4f}")




