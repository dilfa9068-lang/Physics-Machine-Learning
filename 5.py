import numpy as np
import pandas as pd
def turunan_numerik(x,y):
    n = len(x)
    hasil = np.zeros(n)
    for i in range (n):
        if i == 0: # ini untuk beda maju
            hasil[i]= (y[i+1]-y[i])/(x[i+1]-x[i])
        elif i == n-1: # ini beda mundur
            hasil[i]=(y[i]-y[i-1])/(x[i]-x[i-1])
        else:
            hasil[i]=(y[i+1]-y[i-1])/2*(x[i+1]-x[i-1])
    return hasil
t = np.array([0,1,2,3,4,5,6,7])
h = np.array([1000,995,980,956,933,877,760,510])
v1 = turunan_numerik(t,h)
V = np.abs(v1)
df = pd.DataFrame({'|Data waktu (s)|':t,'|Ketinggian (m)|':h, '|Kecepatan (m/s)|':V})
print("-"*40)
print("output program")
print(df.to_string(index = False))