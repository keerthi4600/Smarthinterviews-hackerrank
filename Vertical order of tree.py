import operator
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
def verticalorder(root,v,d):
    if root == None:
        return
    try:
        d[v].append(root.val)
    except:
        d[v]=[root.val]
    verticalorder(root.left,v-1,d)
    verticalorder(root.right,v+1,d)
    return d
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    r=Node(lst[0])
    for i in range(1,n):
        insert(r,Node(lst[i]))
    k=verticalorder(r,0,{})
    v=dict(sorted(k.items(),key=operator.itemgetter(0)))
    for i,j in v.items():
        j.sort()
        print(*j)
    print()    
