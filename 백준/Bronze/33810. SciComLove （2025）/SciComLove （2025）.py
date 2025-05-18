s = 'SciComLove'
t = input()
cnt = 0
for i in range(10):
    cnt += s[i]!=t[i]
    
print(cnt)