n = int(input())
a,b = divmod(n,8)
if not b:
    a -= 1
    b = 8

st = chr(b+ord('a')-1)
print(st+str(a+1))