def find(lst):
    p = list(range(1,n+1))
    res = 1
    for i in range(n)[::-1]:
        idx = p.index(lst.pop(0))
        p.pop(idx)

        res += idx*f(i)

    return res

def gen(num):
    lst = list(range(1,n+1))
    res = []
    for i in range(n)[::-1]:
        tmp = f(i)
        for idx in range(i+1)[::-1]:
            if num > tmp*idx:
                num -= tmp*idx
                res.append(lst.pop(idx))
                break

    return res

f = lambda x:f(x-1)*x if x>1 else 1

n = int(input())
order,*lst = map(int,input().split())
if order == 1:
    print(*gen(lst[0]))
else:
    print(find(lst))