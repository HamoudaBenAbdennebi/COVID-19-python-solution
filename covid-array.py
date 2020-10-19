import numpy as np

N = int(input("donner N : "))
while not ((N <= 100) and (N > 0)):
    N = int(input("donner N : "))
# ?declaration tbl
tbl = np.zeros(N)
for i in range(N):
    print("donner la temperature du patient numero", i+1, ":", end=" ")
    T = float(input())
    while not ((T <= 42) and (T >= 36)):
        print("donner la temperature du patient numero", i+1, ":", end=" ")
        T = float(input())
    tbl[i] = T

mn = tbl[0]
for i in range(1, N):
    if(mn > tbl[i]):
        mn = tbl[i]
mx = tbl[0]
for i in range(1, N):
    if(mx < tbl[i]):
        mx = tbl[i]
sm = 0
for i in range(N):
    sm += tbl[i]
m = (sm / N)
nbp = 0
print("la liste des chambres vulnerables : ",)
for i in range(N):
    if (tbl[i] >= 38):
        nbp += 1
        print(i+1)
print("la temperature maximale : ", mx)
print("la temperature minimale : ", mn)
print("le nombre de malades vulnerables : ", nbp)
print("la moyenne : ", m)
