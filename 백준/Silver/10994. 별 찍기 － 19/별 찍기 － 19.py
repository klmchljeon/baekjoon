n = int(input())
d = [[' ']*(4*n-3) for _ in range(4*n-3)]
x,y = 0,0
size = 4*n-3
for _ in range(n):
    for i in range(x,size):
        for j in range(y,size):
            if i==x or i==size-1 or j==y or j==size-1:
                d[i][j] = '*'

    x += 2
    y += 2
    size -= 2

for i in d:
    print(''.join(i))