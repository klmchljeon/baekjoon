import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n = int(input())
    d = [int(input()) for _ in range(n)]

    lis = [d[0]]

    def find(num):
        s,e = -1,len(lis)-1
        while s+1<e:
            m = (s+e)//2

            if lis[m] >= num:
                e = m

            else:
                s = m

        return e

    for i in d:
        if lis[-1] < i:
            lis.append(i)
        else:
            init = find(i)
            lis[init] = i

    print(len(lis))