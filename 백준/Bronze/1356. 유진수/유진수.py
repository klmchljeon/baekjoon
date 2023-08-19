#유진수
def mul(st):
    res = 1
    for i in st:
        res *= int(i)

    return res

n = input()
for i in range(1,len(n)):
    if mul(n[i:])==mul(n[:i]):
        print('YES')
        break

else:
    print('NO')