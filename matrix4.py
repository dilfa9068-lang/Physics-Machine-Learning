import numpy as np

m = np.array([[2.,5.,1.,29.,],
              [4.,-3.,6.,35.,],
              [8.,9.,7.,95.,]])

n = len(m)

for i in range(n):
    pivot = m[i][i]
    m[i] = m[i] / pivot

    for j in range(n):
        if j != i:
            c = m[j][i]
            m[j] = m[j] - c*m[i]

            print("langkah ke", i+1)
            print(m)

print(m)
x = m[:,n]

for i in range(n):
    print(f"x{i+1} = {x[i]}")