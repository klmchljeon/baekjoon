def IPtoInt(lst):
    tmp = lst[::-1]
    res = 0
    for i in range(8):
        res += tmp[i]*(2**8)**i

    return res

def IntToIP(num):
    tmp = []
    while num:
        num,mod = divmod(num,2**8)
        tmp.append(mod)

    res = [0]*(8-len(tmp)) + tmp[::-1]

    return '.'.join(map(str,res))

t = int(input())
for case in range(t):
    m,n = input().split()
    if m == '1':
        n = list(map(int,n.split('.')))
        print(IPtoInt(n))
    else:
        print(IntToIP(int(n)))