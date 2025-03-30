n = int(input())
cnt = 0
for i in range(n):
    st = input()
    cnt += st[0] == 'C'
    
print(cnt)