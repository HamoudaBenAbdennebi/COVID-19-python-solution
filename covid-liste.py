# saisie de N
N = int(input("donner N : "))
while not ((N <= 100) and (N > 0)):
    N = int(input("donner N : "))
# ?declaration liste
L = []
for i in range(N):
    print("donner la temperature du patient numero", i+1, ":", end=" ")
    T = float(input())
    while not ((T <= 42) and (T >= 36)):
        print("donner la temperature du patient numero", i+1, ":", end=" ")
        T = float(input())
    L.append(T)
mn = L[0]
for i in range(1, N):
    if(mn > L[i]):
        mn = L[i]
mx = L[0]
for i in range(1, N):
    if(mx < L[i]):
        mx = L[i]
sm = 0
for i in range(N):
    sm += L[i]
m = (sm / N)
nbp = 0
print("la liste des chambres vulnerables : ",)
for i in range(N):
    if (L[i] >= 38):
        nbp += 1
        print(i+1)
print("la temperature maximale : ", mx)
print("la temperature minimale : ", mn)
print("le nombre de malades vulnerables : ", nbp)
print("la moyenne : ", m)
