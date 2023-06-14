#카드 역배치
d = list(range(21))
for _ in range(10):
    a,b = map(int,input().split())
    d[a:b+1] = d[a:b+1][::-1]

print(*d[1:])