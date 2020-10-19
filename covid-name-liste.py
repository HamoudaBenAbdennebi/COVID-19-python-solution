N = int(input("donner N : "))
while not ((N <= 100) and (N > 0)):
    N = int(input("donner N : "))
# !declaration liste
Lname = []
Ltemp = []
# ! remplissage liste
for i in range(N):
    # !name
    print("donner le nom du patient numero", i+1, ":", end=" ")
    name = input()
    while not(len(name) != 0):
        print("donner le nom du patient numero", i+1, ":", end=" ")
        name = input()
    Lname.append(name)
    # !temp
    print("donner la temperature du patient numero", i+1, ":", end=" ")
    temp = float(input())
    while not ((temp <= 42) and (temp >= 36)):
        print("donner la temperature du patient numero", i+1, ":", end=" ")
        temp = float(input())
    Ltemp.append(temp)

# !minimum
mn = Ltemp[0]
for i in range(1, N):
    if(mn > Ltemp[i]):
        mn = Ltemp[i]
# !maximum
mx = Ltemp[0]
for i in range(1, N):
    if(mx < Ltemp[i]):
        mx = Ltemp[i]
# !moyenne
sm = 0
for i in range(N):
    sm += Ltemp[i]
m = (sm / N)
# !vunnerable
nbp = 0
print("la liste des patient vulnerables : ")
for i in range(N):
    if (Ltemp[i] >= 38):
        nbp += 1
        print(Lname[i])
print("la temperature maximale : ", mx)
print("la temperature minimale : ", mn)
print("le nombre de malades vulnerables : ", nbp)
print("la moyenne : ", m)
