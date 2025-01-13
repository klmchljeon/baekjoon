st = input()
stack = []
res = 0
for i in st:
    if i == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a+b)

    elif i == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a-b)

    elif i == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a*b)

    elif i == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a//b)

    else:
        stack.append(int(i))

print(stack.pop())