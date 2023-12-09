#수 묶기
n = int(input())
minus = []
plus = []
zero = 0
one = 0

for _ in range(n):
    num = int(input())
    if num < 0:
        minus.append(num)
    elif num > 1:
        plus.append(num)
    elif num:
        one += 1
    else:
        zero += 1

minus.sort(reverse = True)
plus.sort()

res = 0
for i in (minus,plus):
    while len(i) >= 2:
        res += i.pop() * i.pop()

if zero and minus:
    minus.pop()

for i in (minus,plus):
    if i:
        res += i.pop()

res += one
print(res)