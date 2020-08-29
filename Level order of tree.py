class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key
def insert(root,node):
    if root is None:
        root=node
    else:
        if root.val<node.val:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)
def levelorder(root):
    if root == None:
        return
    res=[]
    res.append(root)
    while res:
        g=len(res)
        while g>0:
            h=res.pop(0)
            print(h.val,end=' ')
            if h.left:
                res.append(h.left)
            if h.right:
                res.append(h.right)
            g-=1
        print(' ')
    print()    
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    r=Node(lst[0])
    for i in range(1,n):
        insert(r,Node(lst[i]))
    levelorder(r)
