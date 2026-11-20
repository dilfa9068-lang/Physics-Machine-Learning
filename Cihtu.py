import numpy as np
n = 1
R = 8.314
T = 298.15
f = n*R*T
N = int(input("Enter Value of N:"))
V1 = 2.15*1e-3
V2 = 2.00*1e-3
delta_x = (V2-V1)/N
data_set = []
for i in range(N):
    vi = V1 + i*delta_x
    fi = f/vi
    data_set.append(fi)
jumlah_data = np.array(data_set)
e = -np.sum(jumlah_data*delta_x)
print("Nilai w adalah:", e.round(2))