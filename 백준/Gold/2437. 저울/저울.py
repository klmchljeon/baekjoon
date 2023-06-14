#저울
n = int(input())
d = list(map(int,input().split()))

d.sort()

tmp = 0
for i in d:
    if tmp+1 < i:
        print(tmp+1)
        break

    tmp += i

else:
    print(tmp+1)