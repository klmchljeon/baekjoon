#괄호의 값 
def judge():
    stack = []
    for i in st:
        if i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return 0
            
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0

        else:
            stack.append(i)

    return not stack

def cal():
    res = 1
    for i in stack:
        res *= i

    return res

st = input()

if not judge():
    print(0)
    exit()

res = 0
stack = []
for i in range(len(st)):
    if st[i] in (']',')'):
        if st[i-1] in ('[','('):
            res += cal()

        stack.pop()

    else:
        stack.append(2 + (st[i]=='['))

print(res)