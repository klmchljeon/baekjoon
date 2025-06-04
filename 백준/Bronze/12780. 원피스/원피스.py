s = input()
t = input()
n = len(s)
m = len(t)
cnt = 0
for i in range(n-m+1):
    for j in range(m):
        if s[i+j] != t[j]:
            break
            
    else:
        cnt += 1
        
print(cnt)