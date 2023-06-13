#전화번호 목록
import sys
input = sys.stdin.readline

def ins(trie,word,idx=0,res=False):
    if idx == len(word):
        return res
    
    if word[idx] in trie:
        return ins(trie[word[idx]],word,idx+1,res)
    
    else:
        trie[word[idx]] = dict()
        return ins(trie[word[idx]],word,idx+1,True)

f = lambda x:-len(x)

t = int(input())
for case in range(t):
    n = int(input())

    dic = dict()
    d = [input().rstrip() for _ in range(n)]
    d.sort(key = f)

    flag = True
    for i in d:
        flag &= ins(dic,i)

    print('YES' if flag else 'NO')