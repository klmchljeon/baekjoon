#님 게임 3
n = int(input())
d = list(map(int,input().split()))

tmp = 0
for i in d:
    tmp ^= i

if not tmp:
    print(0)
    exit()

cnt = 0
for i in d:
    tmp ^= i
    for j in range(i):
        tmp ^= j
        cnt += not tmp
        tmp ^= j

    tmp ^= i

print(cnt)