def check(num):
    if n == 1: return 0
    if num == 0: return zero

    for i in dic:
        if num%i != 0: continue
        if not num//i in dic: continue
        
        if i != num//i:
            return 1
        
        if dic[i] >= 2:
            return 1

    return 0

n,q = map(int,input().split())
lst = list(map(int,input().split()))

dic = dict()
zero = 0
for i in lst:
    if not i in dic:
        dic[i] = 0

    dic[i] += 1

for query in range(q):
    order,num = map(int,input().split())
    if order == 1:
        print(check(num))

    else:
        k = lst[num-1]
        if k == 0: continue
        
        lst[num-1] = 0
        dic[k] -= 1

        if dic[k] == 0:
            dic.pop(k)
            zero = 1