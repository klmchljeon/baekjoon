def check(lst):
    for i in range(1,len(lst)-1):
        if lst[i]-lst[i+1] != lst[0]-lst[1]:
            return False
        
    return True

n = int(input())
lst = list(map(int,input().split()))
if check(lst):
    print('YES')
    print(*lst)
    print(*([0]*n))

else:
    print('NO')