def solution(relation):
    answer = 0

    st = set()
    
    n = len(relation[0])
    m = len(relation)
    for i in range(1,1<<n):
        idx = []
        for j in range(n):
            if i | (1<<j) == i:
                idx.append(j)
            
        idx = set(idx)
            
        s = set()
        for a in relation:
            tmp = tuple(a[k] for k in idx)
            s.add(tmp)
            
        if len(s) == m:
            for prev in st:
                if set(prev) - idx == set():
                    break
            
            else:
                answer += 1
                st.add(tuple(sorted(idx)))
    
    return answer