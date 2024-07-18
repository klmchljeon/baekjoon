def check(num):
    if num%400 == 0: return 1
    if num%100 == 1: return 0
    if num%4 == 0: return 1
    return 0

t = int(input())
for case in range(t):
    lst = list(map(int,input().split(', ')))
    res = [i for i in lst if check(i)]
    print(*res)
