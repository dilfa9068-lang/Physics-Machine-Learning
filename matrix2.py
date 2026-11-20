import numpy as np

m = np.array([[11.,-13.,-8.,-20.,],
              [-9.,8.,10.,5.,],
              [-10.,3.,-1.,0.,]])

n = len(m)

# gauss
for i in range(n-1):
    pivot = m[i][i]
    for j in range(i+1,n):
        c = m[j][i]/pivot
        for k in range(i,n+1):
            m[j][k] = m[j][k] - c*m[i][k]
    print("eliminasi ke", i+1)
    print(m)

# back
x = np.zeros((n,1))
x[n-1] = m[n-1][n] / m[n-1][n-1]

for i in range(n-2,-1,-1):
    s = 0
    for j in range(i+1,n):
        s = s + m[i][j] * x[j]
    x[i] = (m[i][n] - s) / m[i][i]

print(x)