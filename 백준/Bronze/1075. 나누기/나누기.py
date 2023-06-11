#나누기
n = list(input())
f = int(input())

for i in range(10):
    for j in range(10):
        n[-2] = str(i)
        n[-1] = str(j)

        num = int(''.join(n))
        if num%f == 0:
            print(i,j,sep='')
            exit()