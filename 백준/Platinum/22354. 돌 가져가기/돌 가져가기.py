n = int(input())
st = input()
tmp = list(map(int,input().split()))

flag = st[0]

t = 0
d = []
for i in range(n):
    if st[i] != flag:
        d.append(t)
        t = 0

    t = max(t,tmp[i])
    flag = st[i]

if not d:
    print(0)
    exit()

d.pop(0)

n = len(d)
d.sort(reverse = True)

idx = n//2 + n%2
print(sum(d[:idx]))