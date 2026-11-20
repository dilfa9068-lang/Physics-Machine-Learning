import numpy as np

m = np.array([[2.,2.,1.,13.,],
              [0.,3.,5.,17.,],
              [0.,0.,6.,6.,]])

n = len(m)

#back sub
x = np.zeros((n,1))
x[n-1] = m[n-1][n] / m[n-1][n-1]

for i in range(n-2,-1,-1):
    s = 0
    for j in range(i+1,n):
        s = s + m[i][j] * x[j]
    x[i] = (m[i][n] - s) / m[i][i]

print(x)