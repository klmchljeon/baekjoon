n = int(input())
s = input()
t = input()
cnt = 0
for i in range(n):
    cnt += s[i]!=t[i]
    
print(cnt)