def cal(a,b):
    if a[0] > b[0]:
        a,b = b,a

    if a[1] < b[0]:
        return -1
    
    if a[1] == b[0]:
        return 0
    
    if a[1] > b[0]:
        return 1
    
def judge(a,b):
    p = cal((a[0],a[2]),(b[0],b[2]))
    q = cal((a[1],a[3]),(b[1],b[3]))

    if p == 0 and q == 0:
        return 'c'
    
    if p < 0 or q < 0:
        return 'd'
    
    if p*q == 0:
        return 'b'

    return 'a'

for i in range(4):
    lst = list(map(int,input().split()))
    print(judge(lst[:4],lst[4:]))