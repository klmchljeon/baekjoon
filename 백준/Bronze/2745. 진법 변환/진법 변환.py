#진법 변환
lst = [str(i) for i in range(10)]
lst += [chr(ord('A')+i) for i in range(26)]

dic = dict(zip(lst,range(36)))

n,b = input().split()
n = n[::-1]
b = int(b)

res = 0
for i in range(len(n)):
    res += dic[n[i]]*b**i

print(res)