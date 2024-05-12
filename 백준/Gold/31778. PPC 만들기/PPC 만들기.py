n,k = map(int,input().split())
lst = [int(i=='C') for i in input()]

tmp = sum(lst)
if tmp <= k or n-tmp <= k:
    lst.sort()

else:
    cntc,cntp = 0,0
    while cntp < k:
        if lst.pop():
            cntc += 1
        else:
            cntp += 1

    lst += [1]*cntc
    cntc = 0

    idx = 0
    while cntp:
        if lst[idx]:
            lst[idx] = 0
            cntp -= 1
            cntc += 1

        idx += 1

    lst += [1]*cntc

res = 0
num = n - sum(lst)
while lst:
    if lst.pop():
        res += num*(num-1)//2

    else:
        num -= 1

print(res)