def printmax(a, n, k): 
    res=[]
    max_upto=[0 for i in range(n)] 
    s=[] 
    s.append(0) 
    for i in range(1,n): 
        while (len(s) > 0 and a[s[-1]] < a[i]): 
            max_upto[s[-1]] = i - 1
            del s[-1] 
        s.append(i) 
    while (len(s) > 0): 
        max_upto[s[-1]] = n - 1
        del s[-1] 
    j = 0
    for i in range(n - k + 1): 
        while (j < i or max_upto[j] < i + k - 1): 
            j += 1
        res.append(a[j])
    print(sum(res))
t=int(input())
for i in range(t):
    n,r=map(int,input().split(' '))    
    arr = list(map(int,input().strip().split(' ')))[:n]
    printmax(arr, n, r) 
