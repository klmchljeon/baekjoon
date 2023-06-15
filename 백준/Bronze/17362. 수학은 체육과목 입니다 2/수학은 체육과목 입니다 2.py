#수학은 체육과목입니다 2
n = int(input())
div,mod = divmod(n-1,4)

if div&1:
    print(5-mod)
else:
    print(mod+1)