def n_hanoi(depth,s,e,m):

    global res

    if depth == 0:

        return 

    if depth == 1:

        res += 1

        ans.append((s,e))

        return 

    

    n_hanoi(depth-1,s,m,e)

    res += 1

    ans.append((s,e))

    n_hanoi(depth-1,m,e,s)

    return 

    

def hanoi(depth,a,b,c):

    global res

    if depth==0:

        return 

    

    if depth==1:

        res += 1

        ans.append((a,'D'))

        return 

    n_hanoi(depth-2,a,b,c)

    res += 3

    ans.append((a,c))

    ans.append((a,'D'))

    ans.append((c,'D'))

    hanoi(depth-2,b,a,c)

n = int(input())

res = 0

ans = []

hanoi(n,'A','B','C')

print(res)

for i in ans:

    print(*i)