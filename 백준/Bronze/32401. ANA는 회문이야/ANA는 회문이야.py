n = int(input())
s = input()

t = ''
for i in s:
    if not i in 'AN': continue
    t += i

cnt = 0
for i in range(1,len(t)-1):
    cnt += t[i-1:i+2] == 'ANA'

print(cnt)