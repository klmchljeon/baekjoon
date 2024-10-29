class Node:
    def __init__(self,val,idx,nxt=None,prv=None):
        self.val = val
        self.idx = idx
        self.nxt = nxt
        self.prv = prv

    def __str__(self):
        return f"{self.val} in {self.idx}"

class DLL:
    def __init__(self,head):
        self.head = head

        cnt = 1
        tmp = self.head
        while tmp.prv != None:
            tmp = tmp.prv
            cnt += 1

        self.tail = tmp
        self.len = cnt

    def append(self,node):
        self.tail.nxt = node
        node.prv = self.tail

        self.tail = node
        node.nxt = None
        self.len += 1

    def delete(self,node):
        if node.prv != None:
            node.prv.nxt = node.nxt
        else:
            self.head = node.nxt
            self.head.prv = None
        
        if node.nxt != None:
            node.nxt.prv = node.prv
        else:
            self.tail = node.prv
            self.tail.nxt = None

        self.len -= 1

n = int(input())
lst = list(map(int,input().split()))

head = Node(lst[0],1)
d = DLL(head)
for i in range(1,n):
    d.append(Node(lst[i],i+1))

while d.len != 1:
    cur = d.head
    while cur != None:
        adj = [cur.prv,cur.nxt]
        tmp = []
        for node in adj:
            if node != None and cur.val >= node.val:
                tmp.append(node)

        for node in tmp:
            cur.val += node.val
            d.delete(node)
            
        cur = cur.nxt

print(d.head.val)
print(d.head.idx)