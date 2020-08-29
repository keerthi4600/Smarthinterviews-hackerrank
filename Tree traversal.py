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
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val,end=' ')
        inorder(root.right) 
def postorder(root): 
    if root: 
        postorder(root.left) 
        postorder(root.right) 
        print(root.val,end=' ') 
def preorder(root): 
    if root: 
        print(root.val,end=' ') 
        preorder(root.left) 
        preorder(root.right)
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    r=Node(lst[0])
    for i in range(1,n):
        insert(r,Node(lst[i]))
    preorder(r)
    print()
    inorder(r)
    print()
    postorder(r)
    print()
    print()
