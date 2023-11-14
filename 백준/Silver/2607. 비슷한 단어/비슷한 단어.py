#비슷한 단어
def gen(word):
    m = len(word)
    res = []
    for i in range(m+1):
        tmp = []
        for j in range(m):
            if i==j: continue
            tmp.append(word[j])

        res.append(tmp)

    return res

def sim(a):
    tmp = gen(a)
    for i in tmp:
        for j in lst:
            if sorted(i)==sorted(j):
                return 1
            
    return 0

n = int(input())
st = list(input())
lst = gen(st)
d = [list(input()) for _ in range(n-1)]

cnt = 0
for i in d:
    cnt += sim(i)

print(cnt)