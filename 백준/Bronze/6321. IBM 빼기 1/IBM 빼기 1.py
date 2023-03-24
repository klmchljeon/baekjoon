#IBM 빼기 1
def conv(a):
    num = ord(a) + 1
    if num > ord('Z'):
        num -= 26

    return chr(num)

n = int(input())
lst = []
for case in range(1,n+1):
    st = input()
    
    tmp = []
    for i in st:
        tmp.append(conv(i))

    res = f"String #{case}\n{''.join(tmp)}"
    lst.append(res)

print(*lst,sep='\n\n')