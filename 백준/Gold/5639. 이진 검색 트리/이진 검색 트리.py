#이진 검색 트리
import sys
sys.setrecursionlimit(20000)

def bs(node=1):
    if c[node][0]:
        bs(c[node][0])
    
    if c[node][1]:
        bs(c[node][1])

    print(d[node])

def ins(num,node=1):
    if d[num] > d[node]:
        if c[node][1]:
            ins(num,c[node][1])
        else:
            c[node][1] = num

    else:
        if c[node][0]:
            ins(num,c[node][0])
        else:
            c[node][0] = num

c = [[0,0] for _ in range(10001)]

d = [0]
while True:
    try:
        d.append(int(input()))
    except:
        break

n = len(d)-1

for i in range(2,n+1):
    ins(i)

bs()