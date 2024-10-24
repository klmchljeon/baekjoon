alpha = [chr(i + ord('a')) for i in range(26)]
dic = dict(zip(alpha,range(26)))

n = int(input())
st = input().split()
lst = []
for word in st:
    res = ''
    for i in range(1,len(word),2):
        x = (dic[word[i-1]] + dic[word[i]] - n)%26
        res += alpha[x]

    lst.append(res)

print(*lst)