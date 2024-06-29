def find(num,a):
    s,e = -1,len(lst[a])
    while s+1<e:
        mid = (s+e)//2

        if lst[a][mid] >= num:
            e = mid

        else:
            s = mid

    return e if e != len(lst[a]) else None

alpha = [chr(i+ord('a')) for i in range(26)]
dic = dict(zip(alpha,range(26)))

s = input()
t = input()
n = len(t)

lst = [[] for _ in range(26)]
for i in range(n):
    lst[dic[t[i]]].append(i)

idx = 0
cnt = 1
for i in s:
    tmp = find(idx,dic[i])
    if tmp == None:
        idx = 0
        cnt += 1
        tmp = find(idx,dic[i])
        if tmp == None:
            print(-1)
            break

    idx = lst[dic[i]][tmp] + 1

else:
    print(cnt)