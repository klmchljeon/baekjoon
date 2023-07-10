#상자 열기
n = int(input())
l = len(bin(n-1))-2

res = [[] for _ in range(l)]
for v in range(n):
    for i in range(l):
        if not v&(1<<i):
            res[i].append(v+1)
print(l)
for i in res:
    print(len(i),*i)