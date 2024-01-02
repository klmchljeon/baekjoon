import sys
input = sys.stdin.readline

res = [0]*(1000+1)
for i in range(2,1000+1):
    cnt = 0
    for j in range(2,i+1):
        tmp = j
        while not i%tmp:
            cnt += 1
            tmp *= j

    res[i] = cnt

t = int(input())
for case in range(t):
    n = int(input())
    print(res[n])