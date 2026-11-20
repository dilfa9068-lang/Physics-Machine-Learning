n = 1
R = 0.082
T0 = 25
N = 100
def f(V):
    return n*R*T0/V
def Persegi_panjang(b,a,N):
    delta = (b-a)/N
    jumlah = 0
    for i in range(100):
        faktor = a + i* delta
        jumlah += f(faktor)
        luas = delta* jumlah
    return luas

W = Persegi_panjang(2.15,2,100)
print("hasil W: {W:.4f}")
def Persegi_panjang(b,a,N):
    delta = (b-a)/N
    jumlah = 0
    for i in range(100):
        faktor = a + i* delta
        jumlah += f(faktor)
        luas = delta* jumlah
    return luas

W = Persegi_panjang(2.15,2,100)
print(f"hasil W: {W:.4f}")