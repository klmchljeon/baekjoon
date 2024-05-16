import sys
input = sys.stdin.readline

n = int(input())
d = []
prefix = [0]

s,e = 0,0
for i in range(n):
    q,*order = map(int,input().split())
    if q == 1:
        d.append(order[0])
        prefix.append(prefix[-1]+order[0])
        e += 1

    else:
        mid = (s+e)//2
        front = prefix[mid]-prefix[s]
        back = prefix[e]-prefix[mid]
        if front <= back:
            print(front)
            s = mid

        else:
            print(back)
            while mid != e:
                d.pop()
                prefix.pop()
                e -= 1

print(*d[s:])