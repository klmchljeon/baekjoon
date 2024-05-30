n=int(input())
dis=list(map(int,input().split()))
loc=list(map(int,input().split()))

cheep = loc[n-2]
cp = [n-2]
lenlow = 0

for i in range(n-3,-1,-1):
    if loc[i]<=cheep:
        cheep = loc[i]
        cp = [i]
        lenlow = 0
    else:
        for ind in range(lenlow,-1,-1):
            if loc[i]>loc[cp[ind]]:
                cp.append(i)
                lenlow += 1
                break
            else:
                del cp[ind]
                lenlow -= 1
cost = 0
for i in range(lenlow,0,-1):
    distance = 0
    for ind in range(cp[i],cp[i-1]):
        distance+=dis[ind]
    cost+=distance*loc[cp[i]]
distance = 0
for ind in range(cp[0],n-1):
    distance+=dis[ind]
cost+=distance*loc[cp[0]]
print(cost)