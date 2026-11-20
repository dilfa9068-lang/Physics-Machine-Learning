import numpy as np

m = np.array([[0.,2.,3.,18.,],
              [8.,-4.,9.,26.,],
              [6.,1.,7.,44.,]])

n = len(m)

# gauss pivot
for i in range(n-1):
    if m[i][i] == 0:
        for r in range(i+1,n):
            if m[i][r] != 0:
                m[[i,r]] = m[[r,i]]
                print(f"ganti {i} ke {r}")
                print(m)
                break
            else:
                print("tidak diganti")
                continue
    
    pivot = m[i][i]
    
    #eliminasi
    for j in range(i+1,n):
        c = m[j][i]/ pivot
        for k in range(i,n+1):
            m[j][k] = m[j][k] - c*m[i][k]
        print("eliminasi ke",i+1)
        print(m)

# back sub
x = np.zeros((n,1))
x[n-1,0] = m[n-1][n] / m[n-1][n-1]

for i in range(n-2,-1,-1):
    s = 0
    for j in range(i+1,n):
        s = s + m[i][j]* x[j,0]
    x[i,0] = (m[i][n] - s)/ m[i][i]

print (x)
    

