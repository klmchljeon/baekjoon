import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n = int(input())
    d = list(map(int,input().split()))

    cnt = 0
    cntp = 0
    prev = 1

    lst = []
    for i in d:
        if not i: continue
        lst.append(i)

    n = len(lst)
    d = lst[:]
    
    for i in d:
        if i < 0 and prev > 0:
            cnt += 1

        if i > 0:
            cntp += 1

        prev = i

    if cntp > cnt:
        print('YES')
        continue

    visit = [False]*n
    for i in range(n):
        if d[i] < 0: continue

        visit[i] = True
        x = i
        val = d[i]
        fir = False
        flag = True
        while True:
            x = x - 1
            if x<0 or visit[x]: break
            
            if val + d[x] > 0:
                fir = True
                val += d[x]
                visit[x] = True

            else:
                flag = False
                break

        if fir and flag:
            cnt -= 1
            d[i] = val
        
        x = i
        val = d[i]
        fir = False
        flag = True
        while True:
            x = x + 1
            if x>n-1 or d[x]>0: break

            if val + d[x] > 0:
                fir = True
                val += d[x]
                visit[x] = True

            else:
                flag = False
                break

        if fir and flag:
            cnt -= 1

    print('YES' if cntp > cnt else 'NO')