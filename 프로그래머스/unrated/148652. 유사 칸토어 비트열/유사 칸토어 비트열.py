def cal(l,r,s,e):
    if e-s == 4:
        cnt = 0
        for i in range(s,e+1):
            if i==s+2:
                continue

            if l <= i <= r:
                cnt += 1

        return cnt
    
    if e<l or r<s:
        return 0
    
    if l<=s and e<=r:
        leng = e-s+1
        cnt = 0
        while leng > 1:
            leng //= 5
            cnt += 1

        return 4**cnt
    
    itv = (e-s+1)//5
    res = 0
    for i in range(s,e+1,itv):
        if i == s + itv*2: continue

        res += cal(l,r,i,i+itv-1)

    return res

def solution(n, l, r):
    answer = cal(l,r,1,5**n)
    return answer