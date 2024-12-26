#알고리즘 수업 - 병합 정렬1
import sys
sys.setrecursionlimit(int(1e5))

def merge_sort(s,e):
    if s >= e: return 

    m = (s+e)//2
    merge_sort(s,m)
    merge_sort(m+1,e)

    merge(s,m,e)
    return

def merge(s,m,e):
    global cnt

    i,j = s,m+1
    tmp = []
    while i<=m and j<=e:
        if d[i] <= d[j]:
            tmp.append(d[i]); i += 1

        else:
            tmp.append(d[j]); j += 1

    while i<=m:
        tmp.append(d[i]); i += 1
    
    while j<=e:
        tmp.append(d[j]); j += 1

    i,t = s,0
    while i<=e:
        cnt += 1
        d[i] = tmp[t]
        if cnt == k:
            print(tmp[t])
            exit()
        i += 1
        t += 1
    
    return 

n,k = map(int,input().split())
d = [0]+list(map(int,input().split()))
cnt = 0

merge_sort(1,n)
print(-1)