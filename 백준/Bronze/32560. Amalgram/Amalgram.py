def count(st):
    cnt = [0]*26
    for i in st:
        cnt[dic[i]] += 1

    return cnt

alpha = [chr(i + ord('a')) for i in range(26)]
dic = dict(zip(alpha,range(26)))

a = count(input())
b = count(input())

tmp = [max(a[i],b[i]) for i in range(26)]
res = ''
for i in range(26):
    res += tmp[i]*alpha[i]

print(res)