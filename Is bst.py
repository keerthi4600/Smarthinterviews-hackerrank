class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key
def insert(lst,root,i,n):
    if i<n:
        temp=Node(lst[i])
        root=temp
        root.left=insert(lst,root.left,2*i+1,n)
        root.right=insert(lst,root.right,2*i+2,n)
    return root    
def isbst(root,a,b):
    if root==None:
        return True
    if root.val <a or root.val>b:
        return False
    return (isbst(root.left,a,root.val) and isbst(root.right,root.val,b))
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    root=None
    root=insert(lst,root,0,n)
    print(isbst(root,-2**31,2**31))
