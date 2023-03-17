#회전
n = list(input())
s = 0
for _ in range(len(n)):
    s += int(''.join(n))
    n.append(n.pop(0))

print(s)