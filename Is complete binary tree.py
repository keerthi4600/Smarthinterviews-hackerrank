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
def isCompleteBT(root): 
    if root is None: 
        return True
    queue = [] 
    flag = False
    queue.append(root) 
    while(len(queue) > 0): 
        tempNode = queue.pop(0) 
        if (tempNode.left): 
            if flag == True : 
                return False
            queue.append(tempNode.left) 
        else: 
            flag = True
        if(tempNode.right): 
            if flag == True: 
                return False
            queue.append(tempNode.right) 
        else: 
            flag = True
    return True
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    r=Node(lst[0])
    for i in range(1,n):
        insert(r,Node(lst[i]))
    if isCompleteBT(r):
        print('Yes')
    else:
        print('No')
