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
class Height: 
    def __init__(self): 
        self.height = 0
def isBalanced(root, height): 
    lh = Height() 
    rh = Height() 
    if root is None: 
        return True
    l = isBalanced(root.left, lh) 
    r = isBalanced(root.right, rh) 
    height.height = max(lh.height, rh.height) + 1
    if abs(lh.height - rh.height) <= 1: 
        return l and r 
    return False
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    r=Node(lst[0])
    for i in range(1,n):
        insert(r,Node(lst[i]))
    height=Height()
    if isBalanced(r, height): 
        print('Yes') 
    else: 
        print('No') 
  
