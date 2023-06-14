#이전 순열 
n = int(input())
d = list(map(int,input().split()))

tmp = []
while d:
    if not tmp or tmp[-1] > d[-1]:
        tmp.append(d.pop())

    else:
        break

else:
    print(-1)
    exit()

for i in range(len(tmp)):
    if tmp[i] < d[-1]:
        tmp[i],d[-1] = d[-1],tmp[i]
        break

d += tmp
print(*d)