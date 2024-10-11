#중복된 숫자
n = int(input())
d = input()
s = 0
temp = ''
for i in d:
    if i == ' ':
        s += int(temp)
        temp = ''

    else:
        temp += i
s += int(temp)

ans = n*(n-1)//2
print(s - ans)