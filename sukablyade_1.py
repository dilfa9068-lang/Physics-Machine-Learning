import numpy as np
def backsubtitution (a,b):
    n = len(b)
    x = np.zeros(n)
    for i in range (n-1, -1, -1):
        jumlah = 0
        for j in range (i+1,n):
            jumlah += a[i,j]*x[j]
        x[i] = (b[i]- jumlah)/a[i,i]
    return x
a = np.array([[2,2,1],[0,3,5],[0,0,6]])
b = np.array([13,17,6])
hasil = backsubtitution (a,b)
for i in range(len(hasil)):
    print(f"x{i+1} = [{hasil[i]}]")

