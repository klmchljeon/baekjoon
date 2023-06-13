#슈퍼 마리오
s = 0
tmp = 0
for i in range(10):
    s += int(input())
    if abs(tmp-100) >= abs(s-100):
        tmp = s

print(tmp)