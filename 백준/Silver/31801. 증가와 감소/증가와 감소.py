import sys
input = sys.stdin.readline
max_ = int(1e6)

def check(num):
    d = list(map(int,str(num)))
    if len(d) < 3:
        return False
    
    prev = d[0]-1
    asc = True
    cnt = 0
    for i in d:
        if asc:
            if prev < i:
                cnt += 1
    
            elif prev > i:
                asc = False

            else:
                return False

        else:
            if prev > i:
                pass

            else:
                return False

        prev = i

    if asc or cnt < 2:
        return False
    else:
        return True

lst = [False]*(max_+1)
for i in range(1,max_+1):
    lst[i] = check(i)

prefix = [0]
s = 0
for i in lst:
    s += i
    prefix.append(s)

t = int(input())
for case in range(t):
    a,b = map(int,input().split())
    print(prefix[b+1] - prefix[a])