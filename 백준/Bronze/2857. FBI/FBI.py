#FBI
d = [input() for _ in range(5)]

res = []
for i in range(5):
    if 'FBI' in d[i]:
        res.append(i+1)
        
print(*res if res else ['HE GOT AWAY!'])