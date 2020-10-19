import numpy as np
N = int(input("donner N : "))
while not ((N <= 100) and (N > 0)):
    N = int(input("donner N : "))
# !declaration liste
Tname = np.zeros(N, dtype="str")
Ttemp = np.zeros(N)
for i in range(N):
    # !name
    print("donner le nom du patient numero", i+1, ":", end=" ")
    name = input()
    while not(len(name) != 0):
        print("donner le nom du patient numero", i+1, ":", end=" ")
        name = input()
    Tname[i] = name
    # !temp
    print("donner la temperature du patient numero", i+1, ":", end=" ")
    temp = float(input())
    while not ((temp <= 42) and (temp >= 36)):
        print("donner la temperature du patient numero", i+1, ":", end=" ")
        temp = float(input())
    Ttemp[i] = temp
# !minimum
mn = Ttemp[0]
for i in range(1, N):
    if(mn > Ttemp[i]):
        mn = Ttemp[i]
# !maximum
mx = Ttemp[0]
for i in range(1, N):
    if(mx < Ttemp[i]):
        mx = Ttemp[i]
# !moyenne
sm = 0
for i in range(N):
    sm += Ttemp[i]
m = (sm / N)
# !vunnerable
nbp = 0
print("la liste des patient vulnerables : ")
for i in range(N):
    if (Ttemp[i] >= 38):
        nbp += 1
        print(Tname[i])
print("la temperature maximale : ", mx)
print("la temperature minimale : ", mn)
print("le nombre de malades vulnerables : ", nbp)
print("la moyenne : ", m)
