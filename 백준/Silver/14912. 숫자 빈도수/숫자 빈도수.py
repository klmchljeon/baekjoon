n,d = input().split()
cnt = 0
for i in range(1,int(n)+1):
    cnt += str(i).count(d)

print(cnt)