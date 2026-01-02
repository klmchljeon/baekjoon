n = int(input())
lst = []
for i in range(n):
    st = input()
    for j in range(n):
        if st[j] != '.':
            lst.append((i,j))

m = len(lst)
res = 0
for i in range(m-2):
    for j in range(i+1,m-1):
        for k in range(j+1,m):
            dx1 = lst[i][0]-lst[j][0]
            dy1 = lst[i][1]-lst[j][1] 

            dx2 = lst[j][0]-lst[k][0]
            dy2 = lst[j][1]-lst[k][1]
            
            res += dx1*dy2 == dx2*dy1

print(res)