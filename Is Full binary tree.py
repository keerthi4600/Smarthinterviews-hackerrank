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
def isFullTree(root): 
    if root is None:     
        return True
    if root.left is None and root.right is None: 
        return True
    if root.left is not None and root.right is not None: 
        return (isFullTree(root.left) and isFullTree(root.right)) 
    return False
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    r=Node(lst[0])
    for i in range(1,n):
        insert(r,Node(lst[i]))
    print(isFullTree(r))
